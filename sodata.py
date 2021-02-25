class Page:
    url: str = ""
    title: str = ""
    views: int = 0
    question = None
    answers = []


class Post:
    up_votes: int = 0
    text: str = ""
    code: list = []
