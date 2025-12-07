import yfinance as yf
from datetime import datetime
import time

FOREX_PAIRS = {
    "EURUSD=X": {"nom": "EUR/USD", "description": "Euro / Dollar Américain"},
    "GBPUSD=X": {"nom": "GBP/USD", "description": "Livre Sterling / Dollar Américain"},
    "USDJPY=X": {"nom": "USD/JPY", "description": "Dollar Américain / Yen Japonais"},
}

def afficher_banniere():
    print("\n" + "=" * 70)
    print(" " * 20 + "FOREX PRICE TRACKER")
    print("=" * 70)
    print(f"Démarré le : {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
    print(f"Suivi de {len(FOREX_PAIRS)} paires Forex")
    print("=" * 70 + "\n")

def obtenir_prix_actuel(symbole):
    ticker = yf.Ticker(symbole)
    data = ticker.history(period="1d", interval="1m")
    if data.empty:
        return None
    return data["Close"].iloc[-1]

def tracker_forex():
    afficher_banniere()
    print("Récupération des données en cours...\n")
    time.sleep(1)

    for symbole, infos in FOREX_PAIRS.items():
        prix = obtenir_prix_actuel(symbole)
        print("-" * 70)
        print(f"{infos['nom']} ({infos['description']})")
        if prix:
            print(f"Prix actuel : {prix:.5f}")
        else:
            print("Prix indisponible")
        time.sleep(0.5)

    print("\nAnalyse terminée.")
    print("=" * 70)

def main():
    try:
        tracker_forex()
    except KeyboardInterrupt:
        print("\nProgramme interrompu.")
    except Exception as e:
        print(f"\nErreur inattendue : {e}")

if __name__ == "__main__":
    main()








