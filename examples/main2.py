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

hasura_client.execute("""
        query findSales {
  Sales(limit: 100000) {
    currencyCode
    customerKey
    deliveryDate
    lineItem
    orderDate
    orderNumber
    productKey
    quantity
    storeKey
  }
}

    """)
result = hasura_client.anomalies(threshold=0, deep={})
pprint(result)

