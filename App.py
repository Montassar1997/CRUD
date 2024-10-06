import streamlit as st



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
nom_filtre = st.text_input('Filtrer par Nom')
prenom_filtre = st.text_input('Filtrer par Prénom')

# Appliquer les filtres
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
