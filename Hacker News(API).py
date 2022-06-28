import requests
import time


def main():
    response = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    )
    time.sleep(1)  # ここで1秒止まる

    dic = response.json()
    for newstopics in range(0, 50):
        # print(dic[newstopics])
        zipcode = dic[newstopics]
        contents = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{zipcode}.json?print=pretty"
        )
        data = contents.json()
        print("'title': '", data.get("title"), "', 'Link':", data.get("url", None))

        # if data["url"] == []:
        #     print("'title': '", data["title"])

        # else:
        #     print("'title': '", data["title"], "', 'link':", data["url"])


if __name__ == "__main__":
    main()
