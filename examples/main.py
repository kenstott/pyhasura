import os
from dotenv import load_dotenv
from pyhasura import gql_client, HasuraClient, ExportFormat
from pprint import pprint

load_dotenv()  # Load environment variables from .env

hasura_client = HasuraClient(uri=os.environ.get("HASURA_URI"), admin_secret=os.environ.get("HASURA_ADMIN_SECRET"))
result = hasura_client.execute("""
        query findCarts {
            carts {
                is_complete
                cart_items {
                    quantity
                    product {
                        price
                    }
                }
            }
            cart_items {
                id
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

result = hasura_client.optimal_number_of_clusters(1,8)
pprint(result)
result = hasura_client.clusters(result)
pprint(result)
