import logging
import os
from dotenv import load_dotenv
from pyhasura import HasuraClient, Casing
from jsondiff import diff
from pprint import pp

load_dotenv()  # Load environment variables from .env
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

hasura_client = HasuraClient(
    uri=os.environ.get("HASURA_URI"),
    admin_secret=os.environ.get("HASURA_ADMIN_SECRET2"),
    logging_=logging)

db_name = "crisp-sheepdog-47_db_3216533"
user = "kenstott"
password = "rN8qOh6AEMCP"
host = "ep-yellow-salad-961725.us-west-2.aws.neon.tech"
port = 5432
_uri = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'

# upload data to database
tables = hasura_client.upload_csv_folder('retailer', uri=_uri, casing=Casing.camel)

# track all the tables we uploaded
result = hasura_client.track_pg_tables(tables, schema="public")
hasura_client.reload_schema()
pp(result)


old_metadata = hasura_client.get_metadata()

# generate relationships
new_metadata = hasura_client.relationship_analysis('new-metadata.json', entity_synonyms={"Stores": ["warehouse"]})

# update hasura with new relationships
hasura_client.replace_metadata(metadata=new_metadata)

pp(diff(old_metadata, new_metadata))
