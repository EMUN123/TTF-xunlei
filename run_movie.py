from movie_tai.fuction import Function
import os

url = 'http://www.taiyingshi.vip'
value = input('请输入您需要的电影名称： ')

def main():
    global url  # local variable 'url' referenced before assignment，需要声明全局变量
    global value

    function = Function(url=url, value=value)
    function.run()

if __name__ == "__main__":
    main()