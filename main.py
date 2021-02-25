from webcrawler import WebCrawler


def main():
    url = "https://stackoverflow.com/questions/38922754/how-to-use-threetenabp-in-android-project"
    wc = WebCrawler()
    wc.parsePage(url)


if __name__ == '__main__':
    main()
