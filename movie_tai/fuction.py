from movie_tai.search import Search
from movie_tai.parse import Parse
from tools.request import Request
from movie_tai.linkhtml import Html
import os

'''
接受主程序传入的电影序列字符串，解析字符串并且进行调度
最终完成程序的执行
'''

'''
strip系列方法都只能处理两端，对中间的空字符串无能为力
应使用replace方法或者split+join组合方法去掉中间字符串
'''

class Function(object):
    
    def __init__(self, url='',value='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.value = value

    # 打印电影列表
    def print_movie_list(self):
        self.search_html = Search(self.url, self.value).search()
        self.movie_list = Parse(html=self.search_html).parse()
        for movie in self.movie_list:
            print(movie)

    # 接受input内容，完成文本解析,返回存储序列号的列表类型，注意不能返回字符串类型
    def parse_index(self):
        self.index_list = []
        self.indexes = self.indexstr.replace(' ','')
        for index in self.indexes:
            index = eval(index)
            self.index_list.append(index)

    def delete_file(self):
        # 删除重名html文件
        file_address = './source/{}.html'.format(self.value)
        if os.path.exists(file_address):
            os.remove(file_address)
            print('find the same file, deleting...')
        else:
            print('creating new file')

    # 执行调度，完成   
    def run(self): 
        self.print_movie_list()
        self.indexstr = input('请输入您需要的电影序号，多个请用空格隔开：')
        self.parse_index()
        self.delete_file()

        for index in self.index_list:
            self.movie_url = Search(url_index=index, search_html=self.search_html).get_index_url()
            self.movie_html = Request(self.movie_url, 'movie url').request()
            
            self.movie_content  = Parse(movie_html=self.movie_html)
            self.links =  self.movie_content.parse_movie_links()
            self.img = self.movie_content.get_img_url()
            self.movie_name = self.movie_content.get_movie_name()

            self.html = Html(file_name=self.value, links=self.links, img_link=self.img, movie_name=self.movie_name, split=True)
            self.html.write_to_html()