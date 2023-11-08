from pathlib import Path

import pandas as pd
from langchain.llms import OpenAI
from langchain.chains.base import Chain
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA, load_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from giskard import Model

from src.utils import get_hyperparameters_from_file

# load hyper-parameters from `hyper-parameters.yaml`
hyper_parameters = get_hyperparameters_from_file()
IPCC_REPORT_URL = hyper_parameters["IPCC_REPORT_URL"]
LLM_NAME = hyper_parameters["LLM_NAME"]
PROMPT_TEMPLATE = hyper_parameters["PROMPT_TEMPLATE"]
TEXT_COLUMN_NAME = hyper_parameters["TEXT_COLUMN_NAME"]


def get_langchain_model() -> Chain:

    llm = OpenAI(model=LLM_NAME, temperature=0)
    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["question", "context"])
    climate_qa_chain = RetrievalQA.from_llm(
        llm=llm,
        retriever=get_context_storage().as_retriever(), prompt=prompt)
    return climate_qa_chain

def get_context_storage() -> FAISS:
    """
    Initialize a vector storage of embedded IPCC report chunks (context).
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, add_start_index=True)
    docs = PyPDFLoader(IPCC_REPORT_URL).load_and_split(text_splitter)
    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    return db


# Define a custom Giskard model wrapper for the serialization.
class FAISSRAGModel(Model):
    def model_predict(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[TEXT_COLUMN_NAME].apply(lambda x: self.model.run({"query": x}))

    def save_model(self, path: str):
        
        out_dest = Path(path)

        # Save the chain object
        self.model.save(out_dest.joinpath("model.json"))

        # Save the FAISS-based retriever
        db = self.model.retriever.vectorstore
        db.save_local(out_dest.joinpath("faiss"))

    @classmethod
    def load_model(cls, path: str) -> Chain:
        src = Path(path)

        # Load the FAISS-based retriever
        db = FAISS.load_local(src.joinpath("faiss"), OpenAIEmbeddings())

        # Load the chain, passing the retriever
        chain = load_chain(src.joinpath("model.json"), retriever=db.as_retriever())
        return chain