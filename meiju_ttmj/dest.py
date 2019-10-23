from bs4 import BeautifulSoup


class Destination(object):
    '''
    获取搜索结果排名第一的地址
    '''
    def __init__(self, html):
        self.html = html

    def parse_result(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        dest_url = soup.find_all('h4')[0].find('a')['href']
        return dest_url
