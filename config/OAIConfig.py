import os
import sys

filepath = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(filepath, os.pardir)
sys.path.append(project_root)

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

from .load_env import ENV

env = ENV()
keyVaultName = env.KEY_VAULT_NAME
KVUri = f"https://{keyVaultName}.vault.azure.net"
secretName = env.OPENAI_KEY

### Azure OpenAI ###
API_VERSION = env.AZ_OAI_VERSION
API_BASE = env.AZ_OAI_BASE
MODEL_DEPLOYMENT = env.AZ_OAI_MODEL

credential = DefaultAzureCredential(additionally_allowed_tenants=['*'])
client = SecretClient(vault_url=KVUri, credential=credential)
OPENAI_API_KEY = client.get_secret(secretName).value
