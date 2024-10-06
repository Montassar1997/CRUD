import streamlit as st
from pyngrok import ngrok
import random

# Choisissez un port aléatoire ou spécifique
port = random.randint(1024, 49151)  # Port aléatoire entre 1024 et 49151
# port = 8501  # Si vous voulez utiliser un port spécifique, décommentez cette ligne et définissez le port

# Ouvrir un tunnel avec ngrok
public_url = ngrok.connect(port=port)
st.write(f"Application disponible à l'URL suivante : {public_url}")

# Titre de l'application
st.title('Application CRUD')

# Initialisation des données (simple liste pour cet exemple)
data = []

# Formulaire pour ajouter des utilisateurs
with st.form(key='crud_form'):
    id_input = st.text_input('ID')
    nom_input = st.text_input('Nom')
    prenom_input = st.text_input('Prénom')
    carte_input = st.text_input('Carte d\'identité')

    submit_button = st.form_submit_button(label='Ajouter')

# Ajouter les données au tableau
if submit_button:
    data.append({
        'ID': id_input,
        'Nom': nom_input,
        'Prénom': prenom_input,
        'Carte d\'identité': carte_input
    })
    st.success(f'Utilisateur {nom_input} {prenom_input} ajouté avec succès !')

# Section de filtrage
st.subheader('Filtrer les utilisateurs')
nom_filtre = st.text_input('Filtrer par Nom')
prenom_filtre = st.text_input('Filtrer par Prénom')

# Application des filtres
if nom_filtre or prenom_filtre:
    filtered_data = [item for item in data if 
                     (nom_filtre.lower() in item['Nom'].lower() if nom_filtre else True) and
                     (prenom_filtre.lower() in item['Prénom'].lower() if prenom_filtre else True)]
else:
    filtered_data = data

# Afficher les données filtrées
st.subheader('Liste des utilisateurs filtrés')
for item in filtered_data:
    st.write(f"ID: {item['ID']}, Nom: {item['Nom']}, Prénom: {item['Prénom']}, Carte d'identité: {item['Carte d\'identité']}")

# Lien ngrok pour accéder à l'application
st.write(f"Application Streamlit disponible à cette URL : {public_url}")
