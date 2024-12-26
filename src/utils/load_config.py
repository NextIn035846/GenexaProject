import yaml
from langchain.embeddings.openai import OpenAIEmbeddings
from pyprojroot import here
import shutil
import os
from pathlib import Path

path_V = Path('configs/App_config.yml')

class LoadConfig:
    """
    A class for loading configuration settings and managing directories.

    This class loads various configuration settings from the 'app_config.yml' file,
    including language model (LLM) configurations, retrieval configurations, summarizer
    configurations, and memory configurations. It also sets up OpenAI API credentials
    and performs directory-related operations such as creating and removing directories.

    ...

    Attributes:
        llm_engine : str
            The language model engine specified in the configuration.
        llm_system_role : str
            The role of the language model system specified in the configuration.
        persist_directory : str
            The path to the persist directory where data is stored.
        custom_persist_directory : str
            The path to the custom persist directory.
        embedding_model : OpenAIEmbeddings
            An instance of the OpenAIEmbeddings class for language model embeddings.
        data_directory : str
            The path to the data directory.
        k : int
            The value of 'k' specified in the retrieval configuration.
        embedding_model_engine : str
            The engine specified in the embedding model configuration.
        chunk_size : int
            The chunk size specified in the splitter configuration.
        chunk_overlap : int
            The chunk overlap specified in the splitter configuration.
        max_final_token : int
            The maximum number of final tokens specified in the summarizer configuration.
        token_threshold : float
            The token threshold specified in the summarizer configuration.
        summarizer_llm_system_role : str
            The role of the summarizer language model system specified in the configuration.
        temperature : float
            The temperature specified in the LLM configuration.
        number_of_q_a_pairs : int
            The number of question-answer pairs specified in the memory configuration.

    Methods:
        load_openai_cfg():
            Load OpenAI configuration settings.
        create_directory(directory_path):
            Create a directory if it does not exist.
        remove_directory(directory_path):
            Removes the specified directory.
    """

    def __init__(self) -> None:
        with open('configs/App_config.yml','r') as cfg:
            app_config = yaml.safe_load(cfg)

        # LLM configs
        self.Summary = app_config["Summary_Prompt"]
        self.Dedline = app_config["Deadlines"]
        self.Requirements = app_config['Requirements']
        self.Scope = app_config['Scope']
        self.Sections = app_config['Sections']
        self.Formating = app_config['Formating']


#if __name__ == "__main__":
    #value_P = LoadConfig()

    #print(value_P.llm_engine)