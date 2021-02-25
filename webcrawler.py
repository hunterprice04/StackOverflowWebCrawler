import requests
from bs4 import BeautifulSoup
from sodata import Page, Post


def getIntFromString(string: str) -> int:
    if string[len(string) - 1] == 'k':
        return int(string[:-1]) * 1000
    else:
        return int(string)


def parsePage(url: str) -> Page:
    # initialize data structures
    ret_page = Page()
    question = Post()

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # get title of page and number of views
    ret_page.url = url
    ret_page.title = soup.find("a", class_="question-hyperlink").getText()
    ret_page.views = getIntFromString(soup.find(class_="grid--cell ws-nowrap mb8")
                                      .getText().split()[1])

    # get list of all upvotes and posts on page
    up_votes = [getIntFromString(v.getText()) for v in soup.findAll(itemprop="upvoteCount")]
    post_bodies = soup.findAll(class_="s-prose js-post-body")
    posts = [p.getText() for p in post_bodies]


    # print(code_snippets)
    # first post should always be the question
    question.up_votes = up_votes
    question.text = posts[0]

    # remaining posts should be the answers
    for post, uv in zip(posts[1:], up_votes[1:]):
        ans = Post()
        ans.text = post
        ans.up_votes = uv
        ret_page.answers.append(ans)

    # add code snippets to data structure
    # TODO: correctly add code to correct data structure
    code_snippets = []
    i = 0
    print(soup.findAll("code"))
    for c in soup.findAll("code"):
        if '\n' in c.getText():
            for j in range(i, len(posts)):
                if c.getText() in posts[j]:
                    if j == 0:
                        question.code.append(c.getText())
                    else:
                        ret_page.answers[j-1].code.append(c.getText())
                else:
                    i += 1

            # code_snippets.append(c.getText())
    print(question.code)
    print(len(ret_page.answers))
    for p in ret_page.answers:
        print(p.code)
        print("+========================")

    ret_page.question = question
    return ret_page
