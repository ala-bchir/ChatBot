# 🧠 Présentation du projet ChatBot Amundi

## 🎯 Objectif

L’objectif était de **prototyper un chatbot** capable de répondre à des questions fréquentes sur l’entreprise **Amundi**, en s’appuyant sur des documents internes .

> 🔍 **Important** : Ce prototype n’est pas un chatbot complet.  
Il utilise uniquement les informations disponibles sur la **page “About Us” du site officiel d’Amundi**.

---

## 🧩 Fonctionnement technique

Le projet repose sur une **architecture RAG (Retrieval-Augmented Generation)**, qui combine la recherche de documents et la génération de texte.

Voici les étapes principales :

1. **Chargement de données**  
   - Les données sont actuellement limitées à un fichier texte contenant le contenu de la page "About Us" d’Amundi.

2. **Vectorisation avec FAISS**  
   - Le texte est découpé, transformé en vecteurs (embeddings) via `OpenAIEmbeddings`, puis indexé avec **FAISS** pour une recherche rapide.

3. **Recherche de contexte**  
   - Lorsqu’une question est posée, le chatbot récupère les passages les plus pertinents du texte (via FAISS).

4. **Génération de la réponse avec GPT-3.5**  
   - Le contexte extrait est envoyé à **GPT-3.5** (via l’API OpenAI), qui génère une réponse claire et cohérente.

---

## 💬 Exemple d’interaction

Voici quelques exemples de questions que l’on peut poser au chatbot :

- **Quelle est l’activité principale d’Amundi ?**  
- **Dans combien de  pays Amundi est-elle présente ?**  
- **Qui est la directrice générale d’Amundi ?**  
- **Quelle est la date de création d’Amundi ?**

> 🧠 Les réponses sont générées uniquement à partir des données fournies au modèle (extraits de la page "About Us").


---

## 🧪 Technologies utilisées

| Outil/Librairie        | Rôle                                                  |
|------------------------|--------------------------------------------------------|
| **LangChain**          | Chaînage d’étapes RAG (chargement, vectorisation…)    |
| **FAISS**              | Moteur de recherche vectorielle                        |
| **OpenAI (GPT-3.5)**   | Génération de réponse à partir du contexte             |
| **Streamlit**          | Interface web simple et rapide pour tester le bot      |
| **GitHub / Streamlit Cloud** | Hébergement du projet et déploiement en ligne         |

---

## 🌐 Interface utilisateur

L’interface est minimaliste :  
- Un champ pour poser une question  
- Une zone d’affichage de la réponse  
- Un fonctionnement immédiat via navigateur (aucune installation requise côté utilisateur)

---

## ✅ Ce que le projet montre

- Une compréhension de l’architecture **RAG**
- L'intégration de **GPT-3.5** dans une logique d’assistant intelligent basé sur documents
- La mise en place d’un outil déployable et utilisable en ligne

---

## 🙋‍♂️ Auteur

Projet réalisé par **Alaeddine  Bchir**  
Master Informatique – Université Paris Cité  
Spécialisation Intelligence Artificielle & Systèmes Distribués



