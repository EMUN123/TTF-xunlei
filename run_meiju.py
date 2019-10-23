from tools.request import Request
from meiju_ttmj.dest import Destination
from meiju_ttmj.search import Search
from meiju_ttmj.links import Links
'''
天天美剧内容资源全，从天天美剧获取需要的美剧资源
'''
'''
终于搞清了类的调用和参数的传递了。。。
'''


def main():

    search = input('请输入您想搜索的美剧，注意声明全名和季数哦: ')

    url = 'https://www.ttkmj.net'
    main_url = Search(url, search).search()
    print(main_url)
    dest_html = Request(main_url, 'search result').request()
    dest_url = Destination(dest_html).parse_result()
    print(dest_url)
    links_html = Request(dest_url, 'target page').request()
    links = Links(links_html).parse_links()
    print(links)
    # 最后写入到目标文件夹中完成保存，学会读写文本：文件夹+操作方式
    f = open('./source/{}.html'.format(search), 'w')
    for link in links:
        f.write(link)
        f.write('\n')
    f.close()


if __name__ == "__main__":
    main()
