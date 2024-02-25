import streamlit as st



def afficher_tutoriel():


# Configuration de la page
    st.set_page_config(
        page_title="Mon Application Streamlit",
        page_icon=":rocket:",
    )

    st.header(':blue[👨🏾‍💻Prérequis]')

    st.write("- Assurez-vous d'avoir compte Kaggle pour entrainer le modèle de traduction en utilisant leur notebook qui nous permettra d'utiliser GPU")
    st.info("Ne pas oublier de faire la vérification avec le telephone après la création du compte")
    st.write("- Assurez-vous d'avoir des bases en Python")
    st.write("- Assurez-vous d'avoir des données prêtes pour l'entrainement, la validation et les tests et qu'elles sont dans un format approprié pour les étapes de prétraitement et d'entrainement")
    st.write("- Assurez-vous d'avoir une bonne connexion internet") 
    st.subheader('Et voila! Nous sommes prêt à commencer😎')





if __name__ == "__main__":
    afficher_tutoriel()
