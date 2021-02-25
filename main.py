from webcrawler import parsePage
import pandas as pd


def main():
    url = "https://stackoverflow.com/questions/38922754/how-to-use-threetenabp-in-android-project"
    parsePage(url)

    # use when reading from csv file of SO id's or urls
    # df = pd.read_csv("../QueryResults.csv")
    # df.drop_duplicates(subset=['Id'])
    # ids = df['Id'].tolist()
    # url = 'https://stackoverflow.com/questions/'
    # i = 0
    # for id in ids:
    #     print(str(i) + " " + str(id),end=" ")
    #     i += 1
    #     if i > 100:
    #         break
    #     try:
    #         wc.parsePage(url + str(id) + "/")
    #     except:
    #         continue


if __name__ == '__main__':
    main()
