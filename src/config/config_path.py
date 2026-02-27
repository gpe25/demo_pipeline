from pathlib import Path

# Dossier racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# NB : tous les chemins relatifs par rapport à BASE_DIR

# Dossiers utilisés :
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_TRF = BASE_DIR / "data" / "interim"
DATA_OUT = BASE_DIR / "data" / "output"

# Fichiers sources utilisés :
APPROS_RAW = DATA_RAW / "appros.csv"
STOCK_RAW = DATA_RAW / "stock.csv"
VENTES_RAW = DATA_RAW / "ventes.csv"

# Fichiers transformés :
APPROS_TRF = DATA_TRF / "appros.csv"
STOCK_TRF = DATA_TRF / "stock.csv"
VENTES_TRF = DATA_TRF / "ventes.csv"

# Fichier de sortie :
EXP_OUTPUT = DATA_OUT / "output.csv"
