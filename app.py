import requests


def main():
    response = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    )
    print(response)
    print(response.text)

    # 辞書として表示
    dic = response.json()
    print(dic)
    # typeを使ってjsonを調べる
    print(type(response.json()))


if __name__ == "__main__":
    main()
