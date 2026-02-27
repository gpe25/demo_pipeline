import pandas as pd
from src.config.config_path import EXP_OUTPUT
from src.config.config_param import CSV_EXPORT
import numpy as np


def run(dfs_trf):
    try:
        # code_site communs
        sites_communs = (list(
            set(dfs_trf['stocks']['code_site'])
            & set(dfs_trf['ventes']['code_site'])
            & set(dfs_trf['appros']['code_site'])))

        # Filtrage dataframe sur sites communs
        # + récupération de l'ensemble des clés [code_article - code_site]
        cle = ['code_article', 'code_site']
        for i, (trt, df) in enumerate(dfs_trf.items()):
            dfs_trf[trt] = df[df['code_site'].isin(sites_communs)]
            if i == 0:
                articles_sites = dfs_trf[trt][cle].drop_duplicates()
            else:
                articles_sites = (pd.concat(
                    [articles_sites, dfs_trf[trt][cle]], axis=0)
                    .drop_duplicates())

        # Création table calendrier sur période commune
        date_min = max(dfs_trf['ventes']['date'].min(),
                       dfs_trf['appros']['date'].min())
        date_max = min(dfs_trf['ventes']['date'].max(),
                       dfs_trf['appros']['date'].max())

        # Création de la table calendrier
        df_calendrier = pd.DataFrame(
            {'date': pd.date_range(start=date_min, end=date_max)})

        # Ajouter semaine et année
        df_calendrier['semaine_iso'] = (df_calendrier['date']
                                        .dt.isocalendar().week)
        df_calendrier['annee_iso'] = (df_calendrier['date']
                                      .dt.isocalendar().year)

        # Concaténation année + semaine
        df_calendrier['annee_sem'] = (df_calendrier['annee_iso']
                                      .astype(str)
                                      + '-'
                                      + df_calendrier['semaine_iso']
                                      .astype(str).str.zfill(2))

        # Combinaisons de toutes les clés [article + site] & semaines
        semaines = df_calendrier['annee_sem'].drop_duplicates()
        combi_cpl = articles_sites.merge(semaines, how='cross')

        # Concaténation ventes & appros
        cle = ['date', 'code_article', 'code_site']
        df_temp = dfs_trf['ventes'].merge(dfs_trf['appros'],
                                          on=cle,
                                          how='outer')

        cols = ['ventes', 'appros']
        df_temp[cols] = df_temp[cols].fillna(0)

        # Concaténation sortie & table calendrier
        df_temp['date'] = pd.to_datetime(df_temp['date'], errors='coerce')
        df_temp = df_temp.merge(df_calendrier[['date', 'annee_sem']],
                                on='date',
                                how='inner')

        # Agrégat par semaine
        cle = ['annee_sem', 'code_article', 'code_site']
        df_sortie = df_temp.groupby(cle).agg({'ventes': 'sum',
                                              'appros': 'sum'}).reset_index()

        # Ajout de l'ensemble des combinaisons possibles
        df_sortie = combi_cpl.merge(df_sortie, on=cle, how='left')

        # Concaténation sortie & stocks
        cle = ['code_article', 'code_site']
        df_sortie = df_sortie.merge(dfs_trf['stocks'], on=cle, how='outer')

        cols = ['ventes', 'appros', 'stock_init']
        df_sortie[cols] = df_sortie[cols].fillna(0)

        # Calcul stock réel
        df_sortie['ventes_cum'] = df_sortie.groupby(cle)['ventes'].cumsum()
        df_sortie['appros_cum'] = df_sortie.groupby(cle)['appros'].cumsum()

        df_sortie['stock'] = round((df_sortie['stock_init']
                                    - df_sortie['ventes_cum']
                                    + df_sortie['appros_cum']), 2)

        df_sortie["cpt_sem"] = df_sortie.groupby(cle).cumcount() + 1
        df_sortie["ventes_prev"] = round(df_sortie["ventes_cum"]
                                         / df_sortie["cpt_sem"], 2)

        # Calcul indicateur de couverture
        df_sortie["couverture"] = np.where(
            df_sortie['ventes_prev'] > 0,
            round(df_sortie['stock']/df_sortie['ventes_prev'], 2),
            np.nan)

        # Enregistrement du fichier de sortie
        cols = ['annee_sem', 'code_article', 'code_site', 'ventes', 'appros',
                'stock', 'ventes_prev', 'couverture', 'stock_init',
                'ventes_cum', 'appros_cum']
        df_sortie[cols].to_csv(EXP_OUTPUT, **CSV_EXPORT)

        return (True, 'Fin')
    except Exception as e:
        return (False, e)
