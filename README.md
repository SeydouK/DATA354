# DATA354 - Chatbot Basé sur des Articles

Ce projet implémente un chatbot interactif capable de répondre à des questions en se basant sur des articles provenant du site web Ecofin. Il utilise des technologies comme **LangChain**, **OllamaLLM**, et **Streamlit** pour fournir des réponses détaillées et spécifiques, tout en mentionnant les sources utilisées.

## Fonctionnalités 

- **Recherche d'articles** : Récupère des articles pertinents en fonction de la question posée.
- **Résumé des articles** : Résume les articles pour extraire les informations clés.
- **Réponses détaillées** : Fournit des réponses spécifiques basées sur les articles.
- **Sources incluses** : Mentionne toujours les sources utilisées pour la réponse.
- **Interface utilisateur** : Une interface web simple et intuitive via **Streamlit**.

## Structure du projet

DATA354/
├── [vector.py](http://_vscodecontentref_/2)          # Gestion des vecteurs et des documents
├── [main.py](http://_vscodecontentref_/3)            # Script principal pour le chatbot sur le terminal
├── [main2.py](http://_vscodecontentref_/4)           # Script principal pour lancer le chatbot sur streamlit (streamlit run main2.py)
├── [Scraper.ipynb](http://_vscodecontentref_/5)           # Script principal pour lancer le chatbot sur streamlit (streamlit run main2.py)
├── [README.md](http://_vscodecontentref_/6)          # Documentation du projet
├── [requirements.txt](http://_vscodecontentref_/7)   # Liste des dépendances Python
├── [my_data_cleaned.csv](http://_vscodecontentref_/8) # Données utilisées pour le chatbot

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.8 ou supérieur
- Les bibliothèques Python nécessaires :
  - `langchain`
  - `streamlit`
  - `pandas`
  - Toute autre dépendance mentionnée dans le projet

Installez les dépendances avec la commande suivante :
```bash
pip install -r [requirements.txt](http://_vscodecontentref_/1)
