import os
import streamlit as st
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import openai


# Charger clé API
load_dotenv()
#openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Titre app
st.set_page_config(page_title="Chatbot Amundi")
st.title("🤖 Chatbot sur Amundi")

# Chargement et découpage des documents
@st.cache_resource
def load_db():
    loader = TextLoader("docs/amundi_intro.txt")
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    return db

db = load_db()

# Création du modèle de réponse
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    retriever=db.as_retriever(),
    return_source_documents=True
)

# Interface utilisateur
question = st.text_input("Pose une question sur Amundi 👇")

if question:
    with st.spinner("Recherche de réponse..."):
        result = qa_chain({"query": question})
        st.markdown("### 📌 Réponse :")
        st.write(result["result"])

        with st.expander("📄 Source(s) utilisée(s)"):
            for doc in result["source_documents"]:
                st.write(doc.page_content)
