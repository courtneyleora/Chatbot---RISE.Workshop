from tkinter import *
import time
import random
import requests
import json
import re

def response(r):
    language_code = 'en'
    search_query = r
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

    response = json.loads(response.text)

    output = []


    if response['pages'] != []:
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

        # removes tags 

        excerpt_text_no_tags = re.sub('<span.*?>|&.*;|</span>', '', excerpt_text)
        description_text = page['description']
        output.append({'excerpt': excerpt_text_no_tags, 'description': description_text, 'article_url': article_url})

    else: 
      output.append({'excerpt': '', 'description': '', 'article_url': ''})

    return output



BG_PINK = '#f2ebf0'

BG_COLOR = '#f2cbe6'

TEXT_COLOR = '#fa64ca'

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
        line = Label(self.window, width=450, bg=BG_PINK)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,font=FONT, padx=5, pady=5)

        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_PINK, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#f2ebf0", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_PINK, command=lambda: self._on_enter_pressed(None))

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
        msg2 = f"{'Cleo'}: {chat_bot(msg)}\n\n" 
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

def remove_punc(pstr):
    punc = r'''!()-[]{};:'",<>./?@\#$%^&*_~'''
    for ele in pstr:
        if ele in punc:
            pstr = pstr.replace(ele, "")
    return pstr

def chat_bot(user_input):
    gratitude = ['thanks', 'thank you']
    greetings = ['hi', 'hello', 'howdy', 'sup', 'hey']
    farewells = ['adios', 'au revoir', 'goodbye', 'bye']
    user_input = remove_punc(user_input.lower())
    time.sleep(0.5)

    
    if user_input in greetings:
        pick1 = random.randint(0, len(greetings)-1)
        return greetings[pick1].capitalize()
    elif user_input == 'what is your name':
        return 'My name is Cleo!'
    elif user_input in gratitude:
        return 'Happy to be of service!'
    elif user_input in 'bye':
        pick = random.randint(0, len(farewells)-1)
        return farewells[pick].capitalize()
    else:
        search_results = response(user_input)
        search_results_ls = ''
        if search_results[0]['description'] == '':
            full_response = 'Welp, this is awkward, I\'ve got nothing'
        else:
            for i in search_results:
                search_results_ls += i['description'] + ':' + i['excerpt'] + '...\n'
                search_results_ls += 'For more information visit: ' + i['article_url']
            full_response = 'Hmm, let me look into it. Here is what I found:\n' + search_results_ls
        return full_response # returns the output from the webscrape



if __name__ == "__main__":
    app = ChatApplication()
    app.run()


