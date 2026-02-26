from transform.trf_stocks import run as run_stock


def main():
    df_stock = run_stock()
    print("Pipeline exécuté avec succès")


if __name__ == "__main__":
    main()
