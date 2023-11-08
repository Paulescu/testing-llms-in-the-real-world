from typing import Dict
import yaml
from pathlib import Path

from src.paths import ROOT_DIR

def get_hyperparameters_from_file() -> Dict:
    """
    Loads values from hyper-parameters.yaml file and returns as a dictionary.
    """
    with open(ROOT_DIR / 'hyper-parameters.yaml', 'r') as file:
        hyper_parameters = yaml.safe_load(file)

    return hyper_parameters


# # Create a Giskard client after having install the Giskard server (see documentation)
# def push_test_to_giskard_server(test_suite):

#     import os
#     url = os.environ['GISKARD_SERVER_URL']
#     api_key = os.environ['GISKARD_API_KEY']  # This can be found in the Settings tab of the Giskard Hub
#     hf_token = os.environ['HF_TOKEN']  # If the Giskard Hub is installed on HF Space, this can be found on the Settings tab of the Giskard Hub

#     client = GiskardClient(
#         url=url, # giskard server url
#         api_key=api_key, # giskard api key
#         hf_token=hf_token  # Use this token to access a private HF space.
#     )

#     my_project = client.get_project("llm_testing")

#     # Upload to the project you just created
#     test_suite.upload(client, my_project)