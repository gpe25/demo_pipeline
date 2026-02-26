import pandas as pd
from src.config.config_path import STOCK_RAW, STOCK_TRF
from src.config.config_param import CSV_EXPORT


# Pas d'actions particulières à effectuer
# Traitements + contrôles + gestion des erreurs à ajouter par la suite
# si besoin

def run():
    try:
        df = pd.read_csv(STOCK_RAW)

        # Arrondi à 2 chiffres pour quantite
        df['quantite'] = df['quantite'].round(2)

        # Renommage quantite en stock
        df = df.rename({'quantite': 'stock'})

        # Sauvegarde du fichier transformé
        df.to_csv(STOCK_TRF, **CSV_EXPORT)

        return (True, df)
    except Exception as e:
        return (False, e)
