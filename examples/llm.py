import os

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_community.tools import BaseGraphQLTool
from langchain_openai import OpenAI
import logging
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
llm = OpenAI(temperature=0)

tools = load_tools(
    ["graphql"],
    graphql_endpoint="http://localhost:4000/graphql",
    custom_headers={"x-hasura-admin-secret": os.environ.get('HASURA_ADMIN_SECRET2')}
)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

graphql_fields = """
query findSales {
  Sales(limit: 1000000, where: { orderNumber: { _gt: 0}}) {
    lineItem
    customer {
      name
      city
    }
    orderDate
    quantity
    customer {
      name
      zipCode
    }
    product {
      brand
      productName
      unitPriceUSD
    }
    orderNumber
  }
}
"""

# suffix = f"""Give me a list of sales, limit 2, and order number > 366000. Include the order date, order number, the quantity sold and any product details (format as a markdown table) which were sold"""
suffix = "what graphql type has information about sales?"
agent.run(suffix)
