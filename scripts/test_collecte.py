import requests
import pandas as pd
import os
# On importe nos réglages depuis l'autre fichier
from config_observatoire import PAYS_AFRIQUE, INDICATEURS

resultats_finaux = []

print(f"🚀 Lancement de la collecte pour {len(PAYS_AFRIQUE)} pays...")

for nom_affichage, code_technique in INDICATEURS.items():
    print(f"📡 Récupération de l'indicateur : {nom_affichage}...")
    for iso in PAYS_AFRIQUE:
        url = f"https://api.worldbank.org/v2/country/{iso}/indicator/{code_technique}?format=json&per_page=1"
        try:
            res = requests.get(url).json()
            if len(res) > 1 and res[1] is not None:
                donnee = res[1][0]
                resultats_finaux.append({
                    'id_iso': iso,
                    'indicateur': nom_affichage,
                    'valeur': donnee['value'],
                    'annee': donnee['date']
                })
        except Exception as e:
            print(f"❌ Erreur pour {iso} : {e}")

# Sauvegarde propre
if not os.path.exists('data'):
    os.makedirs('data')

df = pd.DataFrame(resultats_finaux)
df.to_csv('data/donnees_globales_odd.csv', index=False, encoding='utf-8-sig')

print("\n✨ TERMINÉ ! Le fichier 'data/donnees_globales_odd.csv' a été mis à jour.")