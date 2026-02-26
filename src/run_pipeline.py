from .transform.trf_stocks import run as run_stock
from .transform.trf_appros import run as run_appros
from .transform.trf_ventes import run as run_ventes
import sys


def main():
    # Lancement des traitements de transformation
    traitements = [
         ('stocks', run_stock),
         ('appros', run_appros),
         ('ventes', run_ventes)
         ]

    dfs_trf = {}

    for trt, fct in traitements:
        res = fct()
        if res[0]:
            print(f"Fichier {trt} traités avec succès")
            dfs_trf[trt] = res[1]
        else:
            print(f"""Erreur lors du traitement {trt} : \n{res[1]}""")
            print('Arrêt du traitement')
            sys.exit()


if __name__ == "__main__":
    main()
