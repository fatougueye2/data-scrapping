# moteur BeautifulSoup recupere les pages html 
def fetch_unesco_excel(url):
    # Lit directement un fichier Excel en ligne
    df = pd.read_excel(url)
    # On nettoie pour garder : id_iso, indicateur, valeur, annee
    return df.to_dict('records')