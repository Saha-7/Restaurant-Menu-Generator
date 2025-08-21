from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import openapi_key

import osos.envirion['openapi_key']

llm=OpenAI(temperature=0.7) # temperature controls randomness

def generate_restaurant_name_items(cuisine):
    return{
        'restaurant_name': 'Curry Delight',
        'menu_items': 'Samosa, Butter Chicken',
    }