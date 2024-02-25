import streamlit as st



def afficher_tutoriel():


# Configuration de la page
    st.set_page_config(
        page_title="Mon Application Streamlit",
        page_icon=":rocket:",
    )
    st.header(':blue[😬Limitation]')


    tutoriel = """
    Lorsque le modèle de traduction automatique rencontre des mots sur lesquels il n'a jamais été entraîné, cela entraîne des erreurs dans la traduction. Ces mots inconnus peuvent provenir de termes spécifiques à un domaine, de noms propres... L'incapacité du modèle à traiter ces mots inconnus peut entraîner des traductions incorrectes, voire incompréhensibles.

    Plusieurs approches peuvent être utilisées pour résoudre ce problème :

    1. **Utilisation de glossaires et de ressources lexicales spécifiques :** Incorporer des glossaires et des ressources lexicales spécialisées dans le domaine de la traduction peut aider le modèle à mieux comprendre et traduire les termes spécifiques.

    2. **Expansion du vocabulaire du modèle :** Entraîner le modèle sur un ensemble de données plus large et diversifié peut aider à exposer le modèle à une plus grande variété de mots et de contextes, ce qui peut améliorer sa capacité à traiter les mots inconnus.

    3. **Translittération ou utilisation de stratégies de décomposition :** Pour les mots provenant de langues ou de scripts différents, la translittération ou la décomposition en unités plus petites peuvent être utilisées pour aider le modèle à comprendre et traduire ces mots inconnus.

    En combinant ces approches et en continuant à développer des méthodes d'adaptation et d'amélioration des modèles de traduction automatique, il est possible de réduire les erreurs de traduction causées par les mots inconnus et d'améliorer la qualité globale des traductions automatiques.
    """

    st.markdown(tutoriel)
    st.subheader('Nous revoila avec de nouveau défis à relever, Bonne chance 🫡')





if __name__ == "__main__":
    afficher_tutoriel()
