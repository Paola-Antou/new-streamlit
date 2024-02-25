import streamlit as st



def afficher_tutoriel():


# Configuration de la page
    st.set_page_config(
        page_title="Mon Application Streamlit",
        page_icon=":rocket:",
    )

    st.header(':blue[😀Nous revoilà!]')
    st.info("Pour cette deuxième partie où nous allons évaluer notre modèle et voir si elle marche réellement et pour cela nous irons dans google colab où nous executerons les étapes 1 à 11 et ensuite nous suivre les étape suivantes: ")
     
    st.subheader("Étape 1 : Monter Google Drive dans l'environnement Colab.")
    st.write("Lorsque vous exécutez ce code dans un notebook Google Colab, il vous sera demandé d'autoriser l'accès à Google Drive. Une fois autorisé, votre Google Drive sera monté dans le répertoire /content/drive de l'environnement Colab :")
    """```python
    from google.colab import drive
    drive.mount('/content/drive')
    """
     
    st.subheader("Etape 2 :  Création d'une variable")
    st.write("Ce code définit une variable path_drive contenant le chemin d'accès au fichier checkpoint_best.pt dans Google Drive")
    """```python
    path_drive = "/content/drive/MyDrive/checkpoint_best.pt"
    %env path_drive=$path_drive

    !echo $
    """
        
    st.subheader("Etape 3 :  Evaluation du modèle")

    """```python
    # Evaluer notre modèle avec le métruc BLEU
    !~/.local/bin/fairseq-generate data-bin/fonfr.tokenized.fon-fr \
        --path $path_drive \
        --batch-size 128 --beam 5 --remove-bpe
        """
    st.success(""" P-5584	-0.0285 -0.0454 -0.0429 -0.0382 -0.0578 -0.0499 -0.0129 -0.0126 -0.0483 -0.0429 -0.0318 -0.0129 -0.0442 -0.0129 -0.0385 -0.0493 -0.0189 -0.0341
2024-02-24 12:39:56 | INFO | fairseq_cli.generate | NOTE: hypothesis and token scores are output in base 2
2024-02-24 12:39:56 | INFO | fairseq_cli.generate | Translated 7,968 sentences (49,924 tokens) in 18.1s (440.11 sentences/s, 2757.54 tokens/s)
Generate test with beam=5: BLEU4 = 73.62, 78.5/74.1/72.8/73.7 (BP=0.985, ratio=0.985, syslen=41956, reflen=42594)""")
    
    st.info("BLEU4 = 73.62 montre la performance du modèle")

    st.subheader("Etape 4 :  Installer tensorboardX")
    """```python
    !pip install tensorboardX
    """
    st.subheader("Etape 5 :  Faire une traduction")
    st.write("Maintenant nous allon faire une traduction pour comment le modèle fonctionne à partir des données tests")
    """```python
    !echo "ahan syɛnsyɛn tɛ un ɖo na xwle we" | ~/.local/bin/fairseq-interactive data-bin/fonfr.tokenized.fon-fr \
        --path $path_drive/checkpoints_fon_fr/checkpoint_best.pt \
        --beam 5 --source-lang fon --target-lang fr
    """
    st.subheader("Félicitation!👍, vous venez d'évaaluer votre modèle🥳. ")



if __name__ == "__main__":
    afficher_tutoriel()
