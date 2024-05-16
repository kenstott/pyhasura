import logging
import os

from dotenv import load_dotenv
from pyhasura import HasuraClient
from pprint import pp

load_dotenv()  # Load environment variables from .env

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

hasura_client = HasuraClient(
    uri=os.environ.get("HASURA_URI"),
    admin_secret=os.environ.get("HASURA_ADMIN_SECRET2"),
    logging_=logging)

configuration = {
    "connection_info": {
        "database_url": {
            "from_env": "PG_DATABASE_URL1"
        },
        "isolation_level": "read-committed",
        "use_prepared_statements": False
    }
}

metadata = hasura_client.add_dbml_model_as_source(
    'global-retail-sales.dbml',
    kind='postgres',
    configuration=configuration,
    output_file='new-metadata.json'
)
