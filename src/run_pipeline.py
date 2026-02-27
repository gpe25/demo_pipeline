from .transform.trf_stocks import run as run_stock
from .transform.trf_appros import run as run_appros
from .transform.trf_ventes import run as run_ventes
from .export.exp_output import run as run_output
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

    # Génération fichier de sortie
    res = run_output(dfs_trf)
    if res[0]:
        print("Fichier de sortie généré avec succès")
    else:
        print(f"""Erreur lors de la génération du fichier de sortie :/
\n{res[1]}""")


if __name__ == "__main__":
    main()
