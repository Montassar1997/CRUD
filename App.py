import streamlit as st
from pyngrok import ngrok

# Ouverture du tunnel pour ngrok
public_url = ngrok.connect(8501)
st.write(f'Application accessible à cette adresse : {public_url}')

# Titre de l'application
st.title('Application CRUD')

# Initialisation des données (vous pouvez utiliser une base de données à la place)
data = []

# Formulaire d'ajout des utilisateurs
with st.form(key='crud_form'):
    id_input = st.text_input('ID')
    nom_input = st.text_input('Nom')
    prenom_input = st.text_input('Prénom')
    carte_input = st.text_input('Carte d\'identité')

    submit_button = st.form_submit_button(label='Ajouter')

# Ajout des données à la liste
if submit_button:
    data.append({
        'ID': id_input,
        'Nom': nom_input,
        'Prénom': prenom_input,
        'Carte d\'identité': carte_input
    })
    st.success(f'Utilisateur {nom_input} {prenom_input} ajouté avec succès !')

# Filtrage des utilisateurs
st.subheader('Filtrer les utilisateurs')
nom_filtre = st.text_input('Filtrer par
