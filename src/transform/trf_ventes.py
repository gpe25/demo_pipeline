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
        df = df.rename({'quantite': 'ventes'}, axis=1)

        # Conversion date en datetime
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # Sauvegarde du fichier transformé
        df.to_csv(VENTES_TRF, **CSV_EXPORT)

        return (True, df)
    except Exception as e:
        return (False, e)
