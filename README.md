# DATA354 - Chatbot Basé sur des Articles

Ce projet implémente un chatbot interactif capable de répondre à des questions en se basant sur des articles provenant du site web Ecofin. Il utilise des technologies comme **LangChain**, **OllamaLLM**, et **Streamlit** pour fournir des réponses détaillées et spécifiques, tout en mentionnant les sources utilisées.

## Fonctionnalités 

- **Recherche d'articles** : Récupère des articles pertinents en fonction de la question posée.
- **Résumé des articles** : Résume les articles pour extraire les informations clés.
- **Réponses détaillées** : Fournit des réponses spécifiques basées sur les articles.
- **Sources incluses** : Mentionne toujours les sources utilisées pour la réponse.
- **Interface utilisateur** : Une interface web simple et intuitive via **Streamlit**.


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
pip install -r [requirements.txt]

## Structure du projet

DATA354/
├── [vector.py]           # Gestion des vecteurs et des documents
├── [main.py]             # Script principal pour le chatbot sur le terminal
├── [main2.py]            # Script principal pour lancer le chatbot sur streamlit (streamlit run main2.py)
├── [Scraper.ipynb]       # Script principal pour lancer le chatbot sur streamlit (streamlit run main2.py)
├── [README.md]           # Documentation du projet
├── [requirements.txt]    # Liste des dépendances Python
├── [my_data_cleaned.csv] # Données utilisées pour le chatbot
