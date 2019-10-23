from bs4 import BeautifulSoup

'''
查找720p资源
'''
'''
get('href')比['href']更保险，后者容易报错
'''


class Links(object):

    def __init__(self, html):
        self.html = html

    def parse_links(self):
        links = []
        soup = BeautifulSoup(self.html, 'html.parser')
        link_elements = soup.find_all('a')
        for link_element in link_elements:
            if '720p' in link_element.get_text():
                if link_element.get('href') is not None:
                    links.append(link_element.get('href'))
            else:
                pass
        return links

        