
from langchain_experimental.text_splitter import SemanticChunker
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from paths import *

# Load documents from a directory
loader = DirectoryLoader(DATA_ROOT + "Wiki-texts/Cranmer/", glob="**/*.txt")

print("dir loaded loader")

documents = loader.load()

print(len(documents))

# # Create embeddings clear
embeddings = OllamaEmbeddings(model="nomic-embed-text", show_progress=True)

# # Create Semantic Text Splitter
# text_splitter = SemanticChunker(embeddings, breakpoint_threshold_type="interquartile")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=300,
    add_start_index=True,
)

# # Split documents into chunks
texts = text_splitter.split_documents(documents)

# # Create vector store
vectorstore = Chroma.from_documents(
    documents=texts, 
    embedding= embeddings,
    persist_directory="./db-wiki-cranmer")

print("vectorstore created")