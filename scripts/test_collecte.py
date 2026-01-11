import requests
import pandas as pd
from bs4 import BeautifulSoup


pays_cibles = ['SEN', 'KEN', 'MAR', 'ZAF', 'COD', 'CIV', 'NGA', 'ETH']

# On définit les codes Banque Mondiale pour chaque ODD de ton image
indicateurs_odd = {
    'ODD_1': 'SI.POV.DDAY',     # Pauvreté
    'ODD_4': 'SE.PRM.CMPT.ZS',  # Éducation
    'ODD_5': 'SG.GEN.PARL.ZS',  # Égalité (Femmes au parlement)
    'ODD_7': 'EG.ELC.ACCS.ZS',  # Énergie
    'ODD_13': 'EN.ATM.CO2E.PC'  # Climat
}

resultats_finaux = []

for nom_odd, code_wb in indicateurs_odd.items():
    print(f"📡 Récupération de : {nom_odd}...")
    for iso in pays_cibles:
        url = f"https://api.worldbank.org/v2/country/{iso}/indicator/{code_wb}?format=json&per_page=1"
        res = requests.get(url).json()
        
        if len(res) > 1 and res[1] is not None:
            valeur = res[1][0]['value']
            annee = res[1][0]['date']
            resultats_finaux.append({
                'id_iso': iso,
                'odd': nom_odd,
                'valeur': valeur,
                'annee': annee
            })

# Sauvegarde globale
df_total = pd.DataFrame(resultats_finaux)
df_total.to_csv('data/donnees_globales_odd.csv', index=False)
print("✨ Toutes les données ODD ont été centralisées dans 'donnees_globales_odd.csv' !")