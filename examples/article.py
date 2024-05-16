import os
from dotenv import load_dotenv
from pyhasura import HasuraClient
from pprint import pprint
import logging

import psycopg2


def create_conn():
    conn = psycopg2.connect(
        dbname="crisp-sheepdog-47_db_7805648",
        user="kenstott",
        password="rN8qOh6AEMCP",
        host="ep-yellow-salad-961725.us-west-2.aws.neon.tech",
        port=5432,
        sslmode="require"
    )
    return conn


# Usage example
if __name__ == "__main__":
    connection = create_conn()
    print("Connected to the PostgreSQL server.")
    # Perform your database operations here
    connection.close()

load_dotenv()  # Load environment variables from .env
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

hasura_client = HasuraClient(
    uri=os.environ.get("HASURA_URI"),
    admin_secret=os.environ.get("HASURA_ADMIN_SECRET"),
    logging_=logging)

database_out = hasura_client.execute("""
query find_Cart_Items_test @retain(replayFrom: "-14") @anomalies(modelOut: SELECTION_SET) {
  cart_items {
    quantity
    cart {
      is_complete
      user {
        name
      }
    }
  }
}
""")

pprint(hasura_client.get_extensions())

model = hasura_client.get_extensions().get('anomalies').get('model').replace('"', '\\"')
current_1 = f'''
query find_Cart_Items_test @anomalies(modelIn: SELECTION_SET) {{
  cart_items {{
    quantity
      cart {{
        is_complete
          user {{
            name
          }}
      }}
    }}
}}
'''

current_2 = f'''
query find_Cart_Items_test @anomalies(modelIn: SELECTION_SET) {{
  cart_items(where: {{ cart: {{ user: {{ name: {{ _eq: "Abby"}}}}}}}}) {{
    quantity
      cart {{
        is_complete
          user {{
            name
          }}
      }}
    }}
}}
'''

hasura_client.execute(current_1)
anomalies = hasura_client.get_extensions().get('anomalies')
pprint(anomalies)
# {'cart_items': [{'__index__': 12,
#                  '__score__': -0.0010950574686063863,
#                  'cart': {'is_complete': True, 'user': {'name': 'Marion'}},
#                  'quantity': -1},
#                 {'__index__': 13,
#                  '__score__': -0.05523051792219258,
#                  'cart': {'is_complete': True, 'user': {'name': 'Sean'}},
#                  'quantity': -2}]}

hasura_client.execute(current_2)
anomalies = hasura_client.get_extensions().get('anomalies')
pprint(anomalies)
# {'cart_items': []}
