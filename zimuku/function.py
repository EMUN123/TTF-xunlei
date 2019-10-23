from tools.request import Request
from zimuku.parse import Parse 
from zimuku.download import Downloader
import urllib.request as download

class Function(object):

    def __init__(self, url, value):
        self.url = url
        self.value = value

    def run(self):
        # 输入搜索结果，输出所需要的搜索内容_url
        search_html = Request(self.url+'/search?q='+self.value, 'search url').request()
        dest_urls = Parse(search_html).parse_search_html()
        
        # 存储所有目标字幕的下载页
        download_urls = []
        for dest_url in dest_urls:
            # 获取每一个字幕文件的主页url
            detail_html = Request(self.url + dest_url, 'detail url').request()
            sub_urls = Parse(detail_html).parse_detail()
            for sub_url in sub_urls:
                # 获取字幕文件下载页的url
                sub_html = Request(self.url + sub_url, 'sub url').request()
                download_page_url = Parse(sub_html).parse_sub_url()
                click_download = Downloader(self.url + download_page_url).download()
       