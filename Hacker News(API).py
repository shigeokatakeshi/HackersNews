import requests
import time


def main():
    response = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    )
    time.sleep(1)  # ここで1秒止まる

    dic = response.json()
    number_d = input("Hacker Newsトップのニュースをいくつ表示しますか？：")
    for top_page_news in range(0, int(number_d)):
        # print(dic[newstopics])
        news_id = dic[top_page_news]
        contents = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{news_id}.json?print=pretty"
        )
        data = contents.json()
        print("'title': '", data.get("title"), "', 'Link':", data.get("url", None))

        time.sleep(1)  # ここで1秒止まる
        # if data["url"] == []:
        #     print("'title': '", data["title"])

        # else:
        #     print("'title': '", data["title"], "', 'link':", data["url"])


if __name__ == "__main__":
    main()
