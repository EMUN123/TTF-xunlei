from bs4 import BeautifulSoup
import re

'''
只考虑第一页的内容
'''
class Parse(object):
    
    def __init__(self, html='', movie_html='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.html = html
        self.movie_html = movie_html

    def parse(self):

        movie_list = []
        movie_info = {}
        count = 0

        soup = BeautifulSoup(self.html, 'html.parser')
        items = soup.find_all('div', 'item')
        for item in items:
            try:
                name = item.find('div', 'name').find('a').get_text().strip()
            except:
                name = 'None'
            try:
                year = item.find('div', 'year').get_text()
            except:
                year = 'None'
            try:
                actors = item.find('div', 'actors').get_text()
            except:
                actors = 'None'
            try:
                director = item.find('div', 'director').get_text()
            except:
                director = 'None'
            try:
                cate = item.find('div', 'cate').get_text()
            except:
                cate = 'None'
            count += 1
            movie_info = {
                '名称': '{}'.format(name),
                '类别': '{}'.format(cate),
                '年份': '{}'.format(year),
                '导演': '{}'.format(director),
                '主演': '{}'.format(actors)
            }
            yield '{}: {}'.format(count, movie_info)
            
    def parse_movie_links(self):
        soup = BeautifulSoup(self.movie_html,'html.parser')
        link_elements = soup.find_all('td', 'link')
        for link_element in link_elements:
            link = link_element.find('a').get('href')
            source_name = link_element.find('a').get_text()
            link_info = '{}:{}'.format(source_name, link)
            yield link_info

    def get_movie_name(self):
        soup = BeautifulSoup(self.movie_html,'html.parser')
        movie_name = soup.find('div', id='title').find('h1').get_text()
        return movie_name

    def get_img_url(self):
        '''
        match-group方法详解：
        group(0)返回所有符合对象，group(n)返回第n个括号里的对象
        其用法与match对象[n]和[0]相同
        '''
        '''
        最常用方法findall：只返回括号里的内容，多个括号里的内容按照列表方式存储
        此处应该使用findall方法进行无差别查找
        '''
        pattern = re.compile('.*?<img src="(.*?)".*?>')
        try:
            img_element = re.findall(pattern, self.movie_html)
            return img_element[0] #仅有一个，那就返回仅有的哪一个，不能够返回列表形式
        except Exception as e:
            print(e.args)
