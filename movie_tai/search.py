from tools.request import Request
from bs4 import BeautifulSoup


class Search(object):
    '''
    了解必选参数，可选参数，以及关键字参数的区别和用法，重要一刻
    '''
    def __init__(self, url='', value='', url_index=1, search_html='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.value = value
        self.index = url_index-1
        self.html = search_html

    def search(self):
        search_url = self.url + '/search/?kw=' + self.value
        search_html = Request(search_url, 'search url').request()
        return search_html

    def get_index_url(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        try:
            self.url = soup.find_all('div', 'item')[self.index].find('a').get('href')
            return self.url
        except Exception as e:
            print("can't follow the index url of the movie")
            return e.args

        


        
