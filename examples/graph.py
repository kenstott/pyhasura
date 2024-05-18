from graphql import is_leaf_type, is_wrapping_type
from neo4j import GraphDatabase
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

nodes, relationships = hasura_client.get_schema_relationships()
pp(nodes)
pp(relationships)

hasura_client.metadata_to_neo4j(
    os.environ.get("NEO4J_URI"),
    os.environ.get("NEO4J_USERNAME"),
    os.environ.get("NEO4J_PASSWORD"))

