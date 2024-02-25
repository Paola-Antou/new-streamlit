import streamlit as st



def afficher_tutoriel():


# Configuration de la page
    st.set_page_config(
        page_title="Mon Application Streamlit",
        page_icon=":rocket:",
    )

    st.header(':blue[😀Commençons!]')
    st.info("Pour atteindre cet objectif, nous allons procéder comme suit : nous créerons un nouveau notebook sur Kaggle, définirons la langue comme Python et l'accélérateur comme GPU. Ensuite, nous suivrons les étapes énumérées ci-dessous :")
     
    st.subheader("Étape 1 : Importation des bibliothèques nécessaires")
    st.write("Assurez-vous d'avoir les bibliothèques nécessaire. Vous pouvez le charger comme ceci :")
    """```python
    from sklearn.model_selection import train_test_split 
    import pandas as pd 
    import string 
    import re
    """

    st.subheader("Étape 2 : Chargement des données")
    st.write("Nous chargeons les données à partir du fichier 'data.csv' et sélectionnons les données correspondant à la langue 'Fon'.")
    """```python df = pd.read_csv('data.csv')

    df_fon = df[df['Target_Language'] == 'Fon']"""

    st.subheader("Étape 3 : Affichage des premières lignes du DataFrame")
    st.write("Nous allons maintenant afficher les premières lignes du DataFrame créer précedemment à l'aide de vos données.")

    """```python df_fon_head = df_fon.head()
    st.write(df_fon_head)"""

    st.subheader("Étape 4 : Prétraitement des données")
    st.write("Nous allons maintenant effectuer le prétraitement des données.")

    """```python 
    
    # Conversion de toutes les lettres en minuscules
    df_fon['Target'] = df_fon['Target'].apply(lambda x: str(x).lower())
    df_fon['French'] = df_fon['French'].apply(lambda x: str(x).lower())

    # Suppression des apostrophes des phrases
    df_fon['Target'] = df_fon['Target'].apply(lambda x: re.sub("'", "", x))
    df_fon['French'] = df_fon['French'].apply(lambda x: re.sub("'", "", x))

    # Suppression de toute ponctuation
    exclude = set(string.punctuation)
    df_fon['Target'] = df_fon['Target'].apply(lambda x: ''.join(ch for ch in x if ch not in exclude))
    df_fon['French'] = df_fon['French'].apply(lambda x: ''.join(ch for ch in x if ch not in exclude))

    # Suppression des chiffres des phrases
    digit = str.maketrans('', '', string.digits)
    df_fon['Target'] = df_fon['Target'].apply(lambda x: x.translate(digit))
    df_fon['French'] = df_fon['French'].apply(lambda x: x.translate(digit))

    # Affichage des premières lignes du DataFrame après prétraitement
    st.write("Voici les premières lignes du DataFrame après prétraitement :")
    st.write(df_fon.head())"""

    st.write("Nous aurons en sortie:")
    st.success("""
    /tmp/ipykernel_34/2459096507.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    df_fon['Target'] = df_fon['Target'].apply(lambda x: str(x).lower())
    /tmp/ipykernel_34/2459096507.py:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    df_fon['French'] = df_fon['French'].apply(lambda x: str(x).lower())
    /tmp/ipykernel_34/2459096507.py:8: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    df_fon['Target'] = df_fon['Target'].apply(lambda x: re.sub("'","",x))
    /tmp/ipykernel_34/2459096507.py:9: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    df_fon['French'] = df_fon['French'].apply(lambda x: re.sub("'","",x))
    /tmp/ipykernel_34/2459096507.py:13: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    df_fon['Target'] = df_fon['Target'].apply(lambda x: ''.join(ch for ch in x if ch not in exclude))
    /tmp/ipykernel_34/2459096507.py:14: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    df_fon['French'] = df_fon['French'].apply(lambda x: ''.join(ch for ch in x if ch not in exclude))
    /tmp/ipykernel_34/2459096507.py:18: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    df_fon['Target'] = df_fon['Target'].apply(lambda x: x.translate(digit))
    /tmp/ipykernel_34/2459096507.py:19: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    df_fon['French'] = df_fon['French'].apply(lambda x: x.translate(digit))
""")
    
    st.subheader("Étape 5 : Division des données en ensembles d'entraînement, de validation et de test")
    st.write("Nous allons maintenant diviser les données en ensembles d'entraînement, de validation et de test.")

    """```python
    
    # Division des données en ensemble d'entraînement et le reste 
    train_data, rest_data = train_test_split(df_fon, test_size=0.3, random_state=42)

    # Division du reste en ensembles de validation et de test
    validation_data, test_data = train_test_split(rest_data, test_size=0.5, random_state=42)
    """
    st.success("test_size=0.3 signifie que les données sont divisés avec 70% pour les données d'entrainement et 30% pour le reste. test_size=0.5 montre que le reste été diviser en deux pour les donnée de validation et de test")

    st.subheader("Étape 6 : Génération des fichiers texte")
    st.write("Les fichiers texte pour l'ensemble d'entraînement, de validation et de test ont été générés avec succès.")
    """```python
    def text_to_file(_df,filename):
    french_texts = _df['French']
    target_texts = _df['Target']

    with open(f"{filename}.fr", 'w') as file:
        # file.writelines(french_texts)
        for text in french_texts:
            file.write(text + '\n')

    with open(f"{filename}.fon", 'w') as file:
        # file.writelines(target_texts)
        for text in target_texts:
            file.write(text + '\n')

text_to_file(train_data,'train')
text_to_file(validation_data,'validation')
text_to_file(test_data,'test')
    """
    
    st.subheader("Étape 7 : Clonage du référentiel Fairseq (à faire manuellement)")
    st.write("Vous devez cloner manuellement le référentiel Fairseq depuis GitHub.")
    """```python
    !git clone https://github.com/pytorch/fairseq
    """

    st.subheader("Étape 8 : Exploration du contenu du répertoire Fairseq (après clonage)")
    st.write("Une fois que vous avez cloné le référentiel Fairseq, vous pouvez explorer son contenu.")
    """```python
    !ls fairseq/
    """

    st.subheader("Étape 9 : Installation de Fairseq (après clonage)")
    st.write("Une fois que vous avez cloné le référentiel Fairseq, vous pouvez l'installer localement.")

    st.write("Pour installer Fairseq, assurez-vous d'être dans le répertoire où vous avez cloné Fairseq.")

    st.write("Ensuite, vous pouvez exécuter la commande suivante dans votre terminal :")
    st.code("!pip install --editable ./fairseq/. --user", language="shell")

    st.write("Cela installera Fairseq localement sur votre système.")

    st.subheader("Étape 10 : Prétraitement et binarisation des données avec Fairseq")
    st.write("Une fois que vous avez installé Fairseq localement et organisé vos données, vous pouvez les prétraiter et les binariser.")

    st.write("Pour prétraiter et binariser les données avec Fairseq, vous pouvez exécuter la commande suivante dans votre terminal :")
    st.code("!~/.local/bin/fairseq-preprocess --source-lang fon --target-lang fr \
        --trainpref data/train --validpref data/validation --testpref data/test \
        --destdir data-bin/fonfr.tokenized.fon-fr \
        --workers 20", language="shell")

    st.write("Assurez-vous d'être dans le répertoire approprié où se trouvent vos données.")
    st.write("Cela prétraitera et binarisera vos données pour qu'elles soient prêtes à être utilisées avec Fairseq.")

    st.subheader("Étape 11 : Installation des bibliothèques FastBPE, SacreMoses et Subword NMT")
    st.write("Vous pouvez installer les bibliothèques FastBPE, SacreMoses et Subword NMT en exécutant la commande suivante dans votre terminal :")
    st.code("!pip install fastBPE sacremoses subword_nmt", language="shell")

    st.write("Cela installera les bibliothèques nécessaires pour votre projet.")

    st.subheader("Entraînement du modèle")
    st.write("Pour entraîner votre modèle, vous pouvez exécuter la commande suivante dans votre terminal :")

    """```python
    !CUDA_VISIBLE_DEVICES=0
    !~/.local/bin/fairseq-train \
        data-bin/fonfr.tokenized.fon-fr \
        --arch transformer --share-decoder-input-output-embed \
        --optimizer adam --adam-betas '(0.9, 0.98)' --clip-norm 0.0 \
        --lr 5e-4 --lr-scheduler inverse_sqrt --warmup-updates 4000 \
        --dropout 0.3 --weight-decay 0.0001 \
        --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
        --max-tokens 4096 \
        --eval-bleu \
        --no-epoch-checkpoints \
        --eval-bleu-args '{"beam": 5, "max_len_a": 1.2, "max_len_b": 10}' \
        --eval-bleu-detok moses \
        --eval-bleu-remove-bpe \
        --eval-bleu-print-samples \
        --best-checkpoint-metric bleu --maximize-best-checkpoint-metric \
        --max-epoch 500"""

    
    st.info("Astuce : Pour éviter que votre entraînement ne soit interrompu lorsque vous passez à autre chose, il vous suffit d'appuyer sur le bouton 'Enregistrer' sur la page, de sélectionner le notebook sur lequel vous travaillez. Ensuite, une icône apparaîtra en bas de la page que vous pourrez utiliser pour ajouter votre notebook, et grâce au menu du bouton à trois points juste à côté, relancer l'entraînement. Ce nouvel entraînement ne s'arrêtera pas tant que l'entraînement initial se poursuivra.")
    st.success("Télecharger à la fin au niveau du output le fichier checkpoint_best.pt et stocker le sur drive.")
    st.subheader("Félicitation!👍, vous venez d'entrainer votre modèle🥳. ")





if __name__ == "__main__":
    afficher_tutoriel()
