import pandas as pd
from scripts.test_collecte import recuperer_donnees_worldbank
from scripts.fetch_unstats import recuperer_donnees_onu
from scripts.fetch_unesco import recuperer_donnees_unesco # <-- Import de la nouvelle fonction

def execution_globale():
    print("--- DÉBUT DE LA COLLECTE MULTI-SOURCES ---")
    
    # Source 1 : Banque Mondiale
    data_wb = recuperer_donnees_worldbank()
    
    # Source 2 : ONU
    data_onu = recuperer_donnees_onu()
    
    # Source 3 : UNESCO (Lien vers leur fichier Excel)
    url_unesco = "https://api.unesco.org/data/v1/export/excel" # Exemple d'URL
    data_unesco = recuperer_donnees_unesco(url_unesco)
    
    # FUSION de toutes les sources
    toutes_les_donnees = data_wb + data_onu + data_unesco
    
    df_final = pd.DataFrame(toutes_les_donnees)
    df_final.to_csv('data/donnees_globales_odd.csv', index=False)
    
    print(f"✅ Terminé ! {len(df_final)} lignes prêtes pour Power BI et Streamlit.")

if __name__ == "__main__":
    execution_globale()