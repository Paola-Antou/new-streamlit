import streamlit as st



def afficher_tutoriel():


# Configuration de la page
    st.set_page_config(
        page_title="Mon Application Streamlit",
        page_icon=":rocket:",
    )

    st.title("Tutoriel de :red[Création d'un modèle de traduction Fon-Français]")
    st.header("Objectifs")
    st.write("- Configuration de l'environnement de développement: Guidez les utilisateurs pour installer et configurer les bibliothèques et les outils nécessaire.")
    st.write("- Acquisition et prétraitement des données: Fournissez des instructions sur le nettoyage des ensembles de données français-fon, ainsi que sur leur prétraitement pour les rendre compatibles avec l'entrée du modèle.")         
    st.write("- Construction du modèle de traduction: Montrez comment construire le modèle de traduction, en choisissant une architecture appropriée comme un modèle de sequence-to-sequence avec les réseaux de neurones récurrents (RNN) ou les transformers.")
    st.write("- Entraînement du modèle: Présentez les étapes pour entraîner le modèle de traduction à l'aide des données prétraitées et expliquez les hyperparamètres à ajuster et les métriques à surveiller pendant l'entraînement.")
    st.write("- Évaluation du modèle: Détaillez comment évaluer les performances du modèle à l'aide de mesures telles que le BLEU score et comment interpréter les résultats.")

     



if __name__ == "__main__":
    afficher_tutoriel()
