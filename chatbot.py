import random
import json
import re
import requests




def response(q):
    language_code = 'en'
    search_query = q
    number_of_results = 1
    headers = {
        # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
        'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)'
    }

    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = 'search/page'
    url = f'{base_url}{language_code}/{endpoint}'
    parameters = {'q': search_query, 'limit': number_of_results}
    res = requests.get(url, headers=headers, params=parameters)
    response = json.loads(res.text)

    output = []
    if response.get('pages', []):
        for page in response['pages']:
            display_title = page.get('title', 'No title')
            article_url = f'https://{language_code}.wikipedia.org/wiki/{page.get("key", "")}'

            try:
                article_description = page['description']
            except KeyError:
                article_description = 'a Wikipedia article'

            try:
                thumbnail_url = 'https:' + page['thumbnail']['url']
            except KeyError:
                thumbnail_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/200px-Wikipedia-logo-v2.svg.png'

            excerpt_text = page['excerpt']
            excerpt_text_no_tags = re.sub('<span.*?>|&.*;|</span>', '', excerpt_text)
            description_text = page.get('description', 'No description available')
            output.append({'excerpt': excerpt_text_no_tags, 'description': description_text, 'article_url': article_url})
    else:
        output.append({'excerpt': '', 'description': '', 'article_url': ''})

    return output

def remove_punc(pstr):
    punc = r'''!()-[]{};:'",<>./?@\#$%^&*_~'''
    for ele in pstr:
        if ele in punc:
            pstr = pstr.replace(ele, "")
    return pstr

import random
import requests
import re
import json
from tkinter import *
import time
BG_GRAY = '#ABB2B9'

BG_COLOR = '#17202A'

TEXT_COLOR = '#EAECEE'

FONT = 'Helvetica 14'

FONT_BOLD = 'Helvetica 13 bold'

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=1000, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,font=FONT, padx=5, pady=5)

        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: self._on_enter_pressed(None))

        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        msg2 = f"{'Chatty'}: {response(msg)}\n\n" 
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


def response(q):
    language_code = 'en'
    search_query = q
    number_of_results = 1
    headers = {
        # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
        'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)'
    }

    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = 'search/page'
    url = f'{base_url}{language_code}/{endpoint}'
    parameters = {'q': search_query, 'limit': number_of_results}
    res = requests.get(url, headers=headers, params=parameters)
    response = json.loads(res.text)

    output = []
    if response.get('pages', []):
        for page in response['pages']:
            display_title = page.get('title', 'No title')
            article_url = f'https://{language_code}.wikipedia.org/wiki/{page.get("key", "")}'

            try:
                article_description = page['description']
            except KeyError:
                article_description = 'a Wikipedia article'

            try:
                thumbnail_url = 'https:' + page['thumbnail']['url']
            except KeyError:
                thumbnail_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/200px-Wikipedia-logo-v2.svg.png'

            excerpt_text = page['excerpt']
            excerpt_text_no_tags = re.sub('<span.*?>|&.*;|</span>', '', excerpt_text)
            description_text = page.get('description', 'No description available')
            output.append({'excerpt': excerpt_text_no_tags, 'description': description_text, 'article_url': article_url})
    else:
        output.append({'excerpt': '', 'description': '', 'article_url': ''})

    return output


def remove_punc(pstr):
    punc = r'''!()-[]{};:'",<>./?@\#$%^&*_~'''
    for ele in pstr:
        if ele in punc:
            pstr = pstr.replace(ele, "")
    return pstr

def printSlowly(str):
    for i in str:
        time.sleep(0.05)
        print(i, end='')
    print()
    
def chat_bot():
    wake = input('\nGreet the bot to wake: ').lower()

    greetings = ['hello', 'hi', 'howdy', 'hey', 'sup']
    farewells = ['adios', 'au revoir', 'goodbye', 'bye']

    if wake not in greetings:
        print("I'm sorry, I didn't recognize your greeting.")
        return

    name = input("Please enter your name: ").capitalize()
    printSlowly(f"\nHello {name}! My name is CLEO :)\nType \"bye\" to exit the chat...\n")

    user_input = ''
    while user_input != 'bye':
        user_input = input("\nQuestion: \n")
        user_input = remove_punc(user_input.lower())

        if user_input == 'bye':
            pick = random.randint(0, len(farewells) - 1)
            printSlowly(farewells[pick])
        else:
            printSlowly('Here is what I found:')
            search_results = response(user_input)

            for i in search_results:
                print(i['description'], ':', i['excerpt'], '...')
                print('For more information visit', i['article_url'])

chat_bot()
            
    # if __name__ == "__main__":
    #     app = ChatApplication()
    #     app.run()