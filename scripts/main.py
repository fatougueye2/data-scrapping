import pandas as pd
# On importe nos deux moteurs
from scripts.test_collecte import recuperer_donnees_worldbank 
# (Note: il faudra ajouter 'def' autour de ton code précédent pour qu'il soit importable)
from scripts.fetch_unstats import recuperer_donnees_onu

def execution_globale():
    print("--- DÉBUT DE LA COLLECTE MULTI-SOURCES ---")
    
    # 1. Collecte Banque Mondiale
    data_wb = recuperer_donnees_worldbank()
    
    # 2. Collecte ONU
    data_onu = recuperer_donnees_onu()
    
    # 3. Fusion et sauvegarde
    df_total = pd.DataFrame(data_wb + data_onu)
    df_total.to_csv('data/donnees_globales_odd.csv', index=False, encoding='utf-8-sig')
    
    print(f"✅ Succès ! {len(df_total)} lignes enregistrées au total.")

if __name__ == "__main__":
    execution_globale()