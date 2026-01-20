import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="Observatoire ODD Afrique", layout="wide")

st.title("🌍 Observatoire des ODD et du Numérique")
st.markdown("Visualisation en temps réel des données collectées (Banque Mondiale & ONU)")

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv('data/donnees_globales_odd.csv')

try:
    df = load_data()

    # Barre latérale pour les filtres
    st.sidebar.header("Filtres")
    indicateur_choisi = st.sidebar.selectbox("Choisir un indicateur", df['indicateur'].unique())
    
    # Filtrer les données
    df_filtered = df[df['indicateur'] == indicateur_choisi]

    # Affichage des métriques clés
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Nombre de pays", len(df_filtered['id_iso'].unique()))
    with col2:
        st.metric("Année la plus récente", df_filtered['annee'].max())

    # Création du graphique (Carte)
    fig = px.choropleth(df_filtered, 
                        locations="id_iso", 
                        color="valeur",
                        hover_name="id_iso",
                        title=f"Répartition de : {indicateur_choisi}",
                        color_continuous_scale=px.colors.sequential.Viridis)
    
    st.plotly_chart(fig, use_container_width=True)

    # Affichage du tableau de données
    if st.checkbox("Afficher les données brutes"):
        st.write(df_filtered)

except FileNotFoundError:
    st.error("Le fichier de données n'existe pas encore. Lancez d'abord votre script de collecte !")