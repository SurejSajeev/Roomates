from langchain_openai import OpenAI
from langchain_experimental.graph_transformers.llm import LLMGraphTransformer
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from langchain_community.graphs.neo4j_graph import Neo4jGraph
import getpass
import os
import json  # Import json module for converting dictionaries to strings


# Load text data
text = "text_data.txt"

loader = TextLoader(text)
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
texts = text_splitter.split_documents(documents)

# Load environment variable for OpenAI API key
os.environ["OPENAI_API_KEY"] = getpass.getpass()


relationships = [
    {
        "text": "Sarah is an employee at prismaticAI, a leading technology company based in Westside Valley.",
        "head": "Sarah",
        "head_type": "Person",
        "relation": "WORKS_FOR",
        "tail": "prismaticAI",
        "tail_type": "Company",
    },
    {
        "text": "Michael is also an employee at prismaticAI, where he works as a data scientist.",
        "head": "Michael",
        "head_type": "Person",
        "relation": "WORKS_FOR",
        "tail": "prismaticAI",
        "tail_type": "Company",
    }
]

# Convert relationships to string content for Document
docs = [Document(page_content=json.dumps(content)) for content in relationships]

# Initialize LLM
llm = OpenAI(temperature=0)

# Extract Knowledge Graph
llm_transformer = LLMGraphTransformer(llm=llm)
graph_documents = llm_transformer.convert_to_graph_documents(docs)


graph_store = Neo4jGraph(url="neo4j://your_neo4j_url", username="your_username", password="your_password")
graph_store.write_graph(graph_documents)