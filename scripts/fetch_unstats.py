import requests
import pandas as pd
from config_observatoire import PAYS_AFRIQUE

def recuperer_donnees_onu():
    print("📡 Connexion à l'API de l'ONU (UNSD)...")
    
    # Exemple : Indicateur 1.1.1 (Seuil de pauvreté international)
    # Le code de série pour l'ONU est souvent différent
    series_code = "SI_POV_DAYL" 
    
    resultats_onu = []
    
    for iso in PAYS_AFRIQUE:
        # L'API ONU utilise souvent des codes numériques M49, 
        # mais acceptent aussi certains filtres ISO
        url = f"https://unstats.un.org/SDGAPI/v1/sdg/Series/Data?seriesCode={series_code}&areaCode={iso}"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            # On récupère la donnée la plus récente dans les records
            if data and 'data' in data[0]:
                dernière_valeur = data[0]['data'][-1] # Le dernier de la liste
                resultats_onu.append({
                    'id_iso': iso,
                    'indicateur': 'ONU_Pauvrete_Extrem',
                    'valeur': dernière_valeur['value'],
                    'annee': dernière_valeur['timePeriodStart']
                })
        except Exception as e:
            print(f"⚠️ Pas de données ONU pour {iso}")
            
    return resultats_onu

if __name__ == "__main__":
    data = recuperer_donnees_onu()
    print(data)