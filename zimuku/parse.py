from bs4 import BeautifulSoup
import re

class Parse(object):

    def __init__(self, html):
        self.html = html

    # 拆解请求输入的序号列,返回序号列表，存储整形
    def parse_input(self, input_str):
        dest_url_index = []
        for i in input_str[::2]:
            dest_url_index.append(eval(i))
        return dest_url_index
    
    def parse_search_html(self):
        #参数初始化
        dest_urls = []
        index = 0
        soup = BeautifulSoup(self.html, 'html.parser')
        titles = soup.find_all('p', 'tt clearfix')
        # 打印所有搜索结果
        for title in titles:
            index += 1
            name = title.find('b')
            print('{}: {}'.format(index, name))
        # 请求输入，返回请求index
        dest_index = input('请输入所需要的字幕的序号，中间请用单个逗号或者空格隔开： ')
        dset_url_index = self.parse_input(dest_index)  # 不需要再传入self参数
        for index in dset_url_index:
            dest_url = titles[index-1].find('a').get('href')
            dest_urls.append(dest_url)
        return dest_urls
    
    # 9.14 12:41 完美的处理了所有的异常情况！while用于处理唯一条件，if和try——except适合处理多种情况的条件
    '''
    由普遍到特殊，由基础到高级，一步一步来，慢慢处理，总会成功
    '''
    def parse_detail(self):
        seq = 0
        sub_urls = []
        soup = BeautifulSoup(self.html)
        # 处理没有字母选择框的情况
        try:
            options = soup.find('select', 'form-control').find_all('option')[1:]
            # 打印可以选择的字幕组：同样返回一个需要的序号数列
            for option in options:
                seq += 1
                option = option.get_text()
                print('{}: {}'.format(seq, option))
            # 请求输入，获得需要的字幕组
            index = eval(input('请输入你选择的字幕组的序号： '))
            flag = options[index-1].get_text()
        except:
            flag = 'EMPTY'
        # 开始解析页面内容, 返回各字幕下载页的url
        sub_titles = soup.find_all('td', 'first')
        for sub_title in sub_titles:
            sub_name = sub_title.find('b').get_text()
            # 处理特例：去除有字幕选择框但是未知来源的字幕组
            try:
                sub_provider = sub_title.find('span', 'label label-danger').get_text()
            except:
                print('未知来源字幕组字幕项：{}'.format(sub_name))
                continue  # continue在这里效果不错，在没有字幕框的条件下筛选了具有已知来源的字幕，改为pass则可以下载无字幕框条件下的所有字幕
            # 返回已知的字幕组字幕
            if sub_provider == flag or flag == 'EMPTY':
                regex = re.compile(r'<a href="(.*?)" target=.*?' )
                sub_url = re.findall(regex, str(sub_title))  # BeautifulSoup返回的是独特的Tag类型，需要用str进行转化
                for sub_url in sub_url:
                    print(sub_name)  # 打印符合条件的字幕名称
                    sub_urls.append(sub_url)
            else:
                pass
        return sub_urls

    def parse_sub_url(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        download_page_url = soup.find('a', id='down1').get('href')
        return download_page_url    

    def parse_download_page(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        download_urls = soup.find_all('li')
        for download_url in download_urls:
            download_url =  download_url.find('a', rel='nofollow').get('href')
            yield download_url
        