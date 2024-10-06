import sqlite3
import streamlit as st

# Connexion à la base de données SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Création de la table (si elle n'existe pas déjà)
cursor.execute('''
CREATE TABLE IF NOT EXISTS personnes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom TEXT NOT NULL,
    Prenom TEXT NOT NULL,
    Carte_d_identite TEXT NOT NULL
)
''')

# Fonction pour créer une nouvelle personne
def create_person(nom, prenom, carte_d_identite):
    cursor.execute('''
    INSERT INTO personnes (Nom, Prenom, Carte_d_identite) 
    VALUES (?, ?, ?)
    ''', (nom, prenom, carte_d_identite))
    conn.commit()

# Fonction pour lire les informations d'une personne
def read_person(id):
    cursor.execute('SELECT * FROM personnes WHERE ID = ?', (id,))
    return cursor.fetchone()

# Fonction pour lire toutes les personnes
def read_all_persons():
    cursor.execute('SELECT * FROM personnes')
    return cursor.fetchall()

# Fonction pour mettre à jour les informations d'une personne
def update_person(id, nom, prenom, carte_d_identite):
    cursor.execute('''
    UPDATE personnes SET Nom = ?, Prenom = ?, Carte_d_identite = ? WHERE ID = ?
    ''', (nom, prenom, carte_d_identite, id))
    conn.commit()

# Fonction pour supprimer une personne
def delete_person(id):
    cursor.execute('DELETE FROM personnes WHERE ID = ?', (id,))
    conn.commit()

# Interface Streamlit
st.title("Gestion des Personnes")

menu = ["Ajouter", "Voir", "Mettre à jour", "Supprimer"]
choix = st.sidebar.selectbox("Menu", menu)

if choix == "Ajouter":
    st.subheader("Ajouter une personne")
    with st.form(key="add_form"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        carte_d_identite = st.text_input("Carte d'identité")
        submit_button = st.form_submit_button(label="Ajouter")
        
        if submit_button:
            create_person(nom, prenom, carte_d_identite)
            st.success(f"{nom} {prenom} a été ajouté avec succès.")

elif choix == "Voir":
    st.subheader("Voir les personnes")
    personnes = read_all_persons()
    for personne in personnes:
        st.write(f"ID: {personne[0]}, Nom: {personne[1]}, Prénom: {personne[2]}, Carte d'identité: {personne[3]}")

elif choix == "Mettre à jour":
    st.subheader("Mettre à jour une personne")
    id = st.number_input("Entrez l'ID de la personne", min_value=1, step=1)
    person = read_person(id)
    
    if person:
        with st.form(key="update_form"):
            nom = st.text_input("Nom", value=person[1])
            prenom = st.text_input("Prénom", value=person[2])
            carte_d_identite = st.text_input("Carte d'identité", value=person[3])
            submit_button = st.form_submit_button(label="Mettre à jour")
            
            if submit_button:
                update_person(id, nom, prenom, carte_d_identite)
                st.success(f"Les informations de {nom} {prenom} ont été mises à jour.")
    else:
        st.warning("Personne non trouvée.")

elif choix == "Supprimer":
    st.subheader("Supprimer une personne")
    id = st.number_input("Entrez l'ID de la personne à supprimer", min_value=1, step=1)
    submit_button = st.button("Supprimer")
    
    if submit_button:
        delete_person(id)
        st.success(f"La personne avec l'ID {id} a été supprimée.")

# Fermeture de la connexion à la base de données
conn.close()
