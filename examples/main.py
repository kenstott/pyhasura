import logging
import os
from pprint import pprint

from dotenv import load_dotenv
from pyhasura import HasuraClient, ExportFormat, Casing

load_dotenv()  # Load environment variables from .env
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

hasura_client = HasuraClient(
    uri=os.environ.get("HASURA_URI"),
    admin_secret=os.environ.get("HASURA_ADMIN_SECRET2"),
    logging_=logging)

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
