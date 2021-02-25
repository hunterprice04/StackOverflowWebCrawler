import string

import requests
from bs4 import BeautifulSoup


class WebCrawler:
    tags = ['android']

    # def __init__(self):
    #     pass

    def setTag(self, tags: list):
        self.tags = tags

    def parsePage(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        # get title of page and number of views
        title = soup.find("a", class_="question-hyperlink").getText()
        views = soup.find(class_="grid--cell ws-nowrap mb8").getText().split()[1]
        up_votes = [v.getText() for v in soup.findAll(itemprop="upvoteCount")]
        print(up_votes)
        # get list of all posts on page
        posts = [p.getText() for p in soup.findAll(class_="s-prose js-post-body")]
        # first post should always be the question

        # remaining posts should be the answers
        for p in posts:
            print(p)
            print("+========================")


class Page:
    title = ""
    question = None
    answers = []


class Question:
    question_text = ""
    question_code = []


class Answer:
    answer_text = ""
    answer_code = []
