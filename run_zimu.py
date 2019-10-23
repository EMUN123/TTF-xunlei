from zimuku.function import Function

def main():
    url = 'http://www.zimuku.la'
    value = input("请输入你所需要的字幕的剧集： ")
    sub = Function(url, value)
    sub.run()

if __name__ == "__main__":
    main()