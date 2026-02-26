import pandas as pd
from src.config.config_path import VENTES_RAW, VENTES_TRF
from src.config.config_param import CSV_EXPORT


# Pas d'actions particulières à effectuer
# Traitements + contrôles + gestion des erreurs à ajouter par la suite
# si besoin

def run():
    try:
        df = pd.read_csv(VENTES_RAW)

        # Arrondi à 2 chiffres pour quantité
        df['quantite'] = df['quantite'].round(2)

        # Renommage quantite en stock
        df = df.rename({'quantite': 'ventes'})

        # Conversion date en datetime
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # Ajout année & semaine (norme ISO)
        df['annee_iso'] = df['date'].dt.isocalendar().year
        df['semaine_iso'] = df['date'].dt.isocalendar().week

        # Concaténation année + semaine
        df['annee_semaine'] = (df['annee_iso'].astype(str)
                               + '-'
                               + df['semaine_iso'].astype(str).str.zfill(2))

        # Sauvegarde du fichier transformé
        df.to_csv(VENTES_TRF, **CSV_EXPORT)

        return (True, df)
    except Exception as e:
        return (False, e)
