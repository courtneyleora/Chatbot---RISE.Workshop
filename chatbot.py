import random
import requests
from tkinter import *
import re

def response(q):
    language_code = 'en'
    search_query = q
    number_of_results = 1
    headers = {
    # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)'
    }

    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = '/search/page'
    url = base_url + language_code + endpoint
    parameters = {'q': search_query, 'limit': number_of_results}
    response = requests.get(url, headers=headers, params=parameters)


    # Get article title, description, and URL from the search results
    import json

    response = json.loads(response.text)
    output = []
    for page in response['pages']:
        display_title = page['title']
        article_url = 'https://' + language_code + '.wikipedia.org/wiki/' + page['key']
    try:
        article_description = page['description']
    except:
        article_description = 'a Wikipedia article'
    try:
        thumbnail_url = 'https:' + page['thumbnail']['url']
    except:
        thumbnail_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/200px-Wikipedia-logo-v2.svg.png'
        

    excerpt_text = page['excerpt']
    excerpt_text_no_tags = re.sub('<span.*?>|&.*;|</span>', '', excerpt_text)
    description_text = page['description']
    output.append({'excerpt': excerpt_text_no_tags, 'description': description_text, 'article_url': article_url})
    
    return output 

import time 

def remove_punc(pstr):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in pstr:
        if ele in punc:
            pstr = pstr.replace(ele, "")
    return pstr
def chat_bot():           
    print("\nHello human! My name is CLEO :)\n")
    print("\nType \"bye\" to exit the chat...\n")
    
    user_input = input("\nType here to greet back (case sensitive):\n").lower()
    user_input = remove_punc(user_input)
    time.sleep(0.5)

    greetings = ['Hello,','Hi','Howdy','Hello','Hey','Sup']
    farewells = ['Adios amiga', 'Au Revoir', 'Goodbye', 'Bye']
    
    while user_input != "bye":
        if user_input == 'bye':
            pick = random.randint(0, len(farewells)-1)
            print(farewells[pick])
        elif user_input in greetings:
            pick = random.randint(0, len(greetings)-1)
            print(greetings[pick],"\nWhat is your name?\n")
            name = input("\nEnter your name...\n")
            print(f'\nHi {name}!\n\nHow can I help you?\n')
            query = input("\nType here...\n")
            print(response(query))
        print(farewells[pick])    
chat_bot()