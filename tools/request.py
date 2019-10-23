import requests


class Request(object):

    def __init__(self, url,url_info=''):
        self.url = url
        self.url_info = url_info
        # 增加重试的时间和基础
        self.max_retries = 3
        self.retry = 0
        self.headers = {
            # 基础不牢，地动山摇
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKi ./'
            '/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }

    def request(self):
        if self.retry <= self.max_retries:
            s = requests.session()
            s.keep_alive = False
            try:
                '''
                解决网页编码问题：
                设置好encoding形式很总要，设计中文时一律utf-8，提前做好html编码形式的转换 
                一劳永逸
                '''
                response = s.get(self.url, headers=self.headers)
                response.encoding = 'utf-8'
                if response.status_code == 200:
                    print(self.url_info + ' success')
                    if response.text != None:
                        return response.text
            except Exception as e:
                self.retry += 1
                print('{} error:{} retring:{}'.format(self.url_info, response.status_code, self.retry))
                self.request()
        else:
            print(self.url_info + ' failed after 3 tries')
                        
