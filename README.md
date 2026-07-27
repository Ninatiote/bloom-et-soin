# Bloom & Soin — Boutique en ligne (démo)

Site de vente en ligne pour une marque de beauté/bien-être, construit avec **Streamlit**.
Cette version est une démo avec 5 produits d'exemple — elle sert de base à personnaliser
avec ta vraie marque, tes vrais produits, et (plus tard) un vrai système de paiement.

## Fonctionnalités incluses

- Catalogue produits avec images, prix, descriptions
- Panier (ajout / retrait de quantités)
- Formulaire de commande (nom, email, adresse)
- Ambiance visuelle personnalisée (couleurs, typographie)

## Lancer le site en local

1. Installer les dépendances :
   ```
   pip install -r requirements.txt
   ```
2. Lancer l'application :
   ```
   streamlit run app.py
   ```
3. Le site s'ouvre automatiquement dans ton navigateur (en général sur `http://localhost:8501`).

## Déployer en ligne (comme ton dashboard foot)

1. Créer un nouveau dépôt GitHub et y pousser ces fichiers (`app.py`, `requirements.txt`).
2. Aller sur [streamlit.io/cloud](https://share.streamlit.io), se connecter avec GitHub.
3. Cliquer sur "New app", sélectionner le dépôt, et choisir `app.py` comme fichier principal.
4. Déployer : le site est en ligne en quelques minutes, avec une URL publique à partager.

## Prochaines étapes possibles

- Remplacer les produits d'exemple par tes vrais produits (nom, prix, description, photos)
- Personnaliser les couleurs / le style selon ton identité de marque
- Ajouter un vrai paiement en ligne (Stripe)
- Enregistrer les commandes dans une base de données ou un fichier (au lieu de juste les afficher)
- Ajouter l'envoi d'un email de confirmation automatique
