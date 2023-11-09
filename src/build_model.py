from pathlib import Path
import logging

from dotenv import load_dotenv
import pandas as pd

from giskard import Dataset

from src.model import get_langchain_model, FAISSRAGModel
from src.utils import get_hyperparameters_from_file
from src.paths import MODEL_DIR, DATASET_DIR

# load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)

# load hyper-parameters from `hyper-parameters.yaml`
hyper_parameters = get_hyperparameters_from_file()
TEXT_COLUMN_NAME = hyper_parameters["TEXT_COLUMN_NAME"]


def run():

    # Get QA langchain model
    logger.info('Loading QA langchain model')
    climate_qa_chain = get_langchain_model()

    # Test the chain.
    logger.info('Testing the chain')
    test_question = "Is sea level rise avoidable? When will it stop?"
    test_response = climate_qa_chain(test_question)
    logger.info(f'Test: \n Question: {test_question} \n Answer: {test_response}')

    # Wrapping QA chain for Giskard
    logger.info('Wrapping QA chain for Giskard')
    giskard_model = FAISSRAGModel(
        model=climate_qa_chain,  # A prediction function that encapsulates all the data pre-processing steps and that could be executed with the dataset used by the scan.
        model_type="text_generation",  # Either regression, classification or text_generation.
        name="Climate Change Question Answering",  # Optional.
        description="This model answers any question about climate change based on IPCC reports",  # Is used to generate prompts during the scan.
        feature_names=[TEXT_COLUMN_NAME],  # Default: all columns of your dataset.
    )

    # Optional: Wrap a dataframe of sample input prompts to validate the model wrapping and to narrow specific tests' queries.
    giskard_dataset = Dataset(
        pd.DataFrame(
            {
                TEXT_COLUMN_NAME: [
                    "According to the IPCC report, what are key risks in the Europe?",
                    # "Is sea level rise avoidable? When will it stop?",
                ]
            }
        )
    )

    # save giskard model and dataset artifacts, so our CI/CD pipeline can pick them up
    giskard_model.save(MODEL_DIR)
    giskard_dataset.save(DATASET_DIR, 0)
    
    logger.info("Model and dataset artifacts were successfully dumped for CI/CD.")

if __name__ == '__main__':
    run()
