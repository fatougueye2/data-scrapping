import pandas as pd
import os
# On importe ta liste de pays pour filtrer l'Afrique
from config_observatoire import PAYS_AFRIQUE

def recuperer_donnees_unesco_local():
    print("📊 Filtrage des données UNESCO pour l'Afrique...")
    chemin_fichier = "inputs/unesco_primaire.csv"
    
    if not os.path.exists(chemin_fichier):
        print("⚠️ Fichier inputs/unesco_primaire.csv non trouvé.")
        return []

    try:
        # Lecture du CSV
        df = pd.read_csv(chemin_fichier)
        
        # 1. FILTRAGE : On ne garde que les pays présents dans ta liste PAYS_AFRIQUE
        df_afrique = df[df['geoUnit'].isin(PAYS_AFRIQUE)].copy()
        
        # 2. NETTOYAGE : Sélection et renommage des colonnes
        df_afrique = df_afrique[['geoUnit', 'year', 'value']]
        df_afrique.columns = ['id_iso', 'annee', 'valeur']
        
        # 3. IDENTIFICATION : On précise quel est cet indicateur
        df_afrique['indicateur'] = 'UNESCO_Taux_Achevement_Primaire'
        
        # 4. ARRONDIS : On arrondit à 2 chiffres après la virgule
        df_afrique['valeur'] = df_afrique['valeur'].round(2)
        
        print(f"✅ {len(df_afrique)} lignes ajoutées pour l'UNESCO.")
        return df_afrique.to_dict('records')
    
    except Exception as e:
        print(f"❌ Erreur UNESCO : {e}")
        return []