import pandas as pd
from src.config.config_path import APPROS_RAW, APPROS_TRF
from src.config.config_param import CSV_EXPORT


# Pas d'actions particulières à effectuer
# Traitements à ajouter par la suite si besoin

def run():
    try:
        df = pd.read_csv(APPROS_RAW)

        # Conversion code_article en int
        df['code_article'] = (pd.to_numeric(
            df['code_article'], errors='coerce')
            .astype('Int64'))
        # Suppression des erreurs de conversion
        df = df[~df['code_article'].isna()]

        # Conversion date en datetime
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # Agrégation des approvisionnements par jour et par clé article / site
        cle = ['date', 'code_article', 'code_site']
        df_agg = df.groupby(cle)['quantite'].sum().reset_index()

        # Ajout semaine
        
        # Sauvegarde du fichier transformé
        df_agg.to_csv(APPROS_TRF, **CSV_EXPORT)
        return (True, df_agg)
    except Exception as e:
        return (False, e)
