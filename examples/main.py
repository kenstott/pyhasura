import logging
import os
from pprint import pprint
import jsondiff

from dotenv import load_dotenv
from pyhasura import HasuraClient, ExportFormat, Casing

load_dotenv()  # Load environment variables from .env
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

hasura_client = HasuraClient(
    uri=os.environ.get("HASURA_URI"),
    admin_secret=os.environ.get("HASURA_ADMIN_SECRET2"),
    logging_=logging)

# db_name = "crisp-sheepdog-47_db_3216533"
# user = "kenstott"
# password = "rN8qOh6AEMCP"
# host = "ep-yellow-salad-961725.us-west-2.aws.neon.tech"
# port = 5432
# _uri = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'

# upload data to database
# tables = hasura_client.upload_csv_folder('retailer', uri=_uri, casing=Casing.camel)

# track all the tables we uploaded
# result = hasura_client.track_pg_tables(tables, schema="public")
# hasura_client.reload_schema()
# pprint(result)

# remember current relationships
old_metadata = {"metadata": hasura_client.get_metadata()}

# generate relationships
new_metadata = hasura_client.relationship_analysis('new-metadata.json')

# look at the difference
diff = jsondiff.diff(old_metadata, new_metadata)
pprint(diff)
exit(0)

result = hasura_client.execute("""
query findCarts {
    carts {
      created_at
      is_complete
      user {
        name
      }
      cart_items {
        quantity
        product {
          name
          price
        }
      }
    }
}
""")

pprint(result)

result = hasura_client.convert_output_format(ExportFormat.ARROW)
pprint(result)
result = hasura_client.convert_output_format(ExportFormat.CSV)
pprint(result)
result = hasura_client.convert_output_format(ExportFormat.PARQUET)
pprint(result)
result = hasura_client.convert_output_format(ExportFormat.DATAFRAME)
pprint(result)
result = hasura_client.convert_output_format(ExportFormat.FLAT)
pprint(result)

result = hasura_client.write_to_file(output_format=ExportFormat.ARROW)
pprint(result)
result = hasura_client.write_to_file(output_format=ExportFormat.CSV)
pprint(result)
result = hasura_client.write_to_file(output_format=ExportFormat.PARQUET)
pprint(result)
result = hasura_client.write_to_file(output_format=ExportFormat.FLAT)
pprint(result)
result = hasura_client.write_to_file(output_format=ExportFormat.NATURAL)
pprint(result)

result = hasura_client.anomalies()
pprint(result)
result = hasura_client.anomalies(threshold=.03)
pprint(result)

result = hasura_client.anomalies_training()
pprint(result)
result = hasura_client.anomalies(training_files=result, threshold=0)
pprint(result)

result = hasura_client.optimal_number_of_clusters(1, 8)
pprint(result)
result = hasura_client.clusters(result)
pprint(result)

result = hasura_client.anomalies_training(base64_encoded_data=True)
pprint(result)
hasura_client.execute("""
        query findCarts {
            carts(where: { user: { name: { _eq: "Abby"}}}) {
    created_at
    is_complete
    user {
      name
    }
    cart_items {
      quantity
      product {
        name
        price
      }
    }
  } 
        }
    """)
result = hasura_client.anomalies(training_base64=result, threshold=0)
pprint(result)

result = hasura_client.anomalies_training(database_output=True, selection_set_hash=str(uuid.uuid4()))
result = hasura_client.anomalies(selection_set_hash=result["selectionSetHash"], threshold=0)
pprint(result)
