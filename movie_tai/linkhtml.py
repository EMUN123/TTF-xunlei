'''
将链接分词后存储到html文件中便于下载
'''


class Html(object):

    def __init__(self, file_name='', links=[], img_link='', split=False, movie_name='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.links = links
        self.split = split
        self.img_link = img_link
        self.movie_name = movie_name

    def write_to_html(self):
        title = '<h2 style="color: darkorange">资源链接如下,请自行下载：</h2>\n'
        img_frame = '<img src="{}"\n>'.format(self.img_link)
        linkframe = '<a href="{}">"{}"</a>\n'
        newline = '<br>'

        '''
        读写文件时一定要注意代码转换的问题，读取时要制定encoding形式，
        而对于错误需要设置忽略，否则会无法写入
        '''
        movie_addres = 'D:/ProgramData/Python/xunlei_links/source/{}.html'.format(self.file_name)
        f = open(movie_addres, 'a', encoding='utf-8', errors='ignore')
        f.write('<br><br>')
        f.write(img_frame)
        f.write('<h1 style="font: italic;color:blue">{}</h1>'.format(self.movie_name))
        f.write(title)

        if self.split == True:
            for link in self.links:
                link_name = link.split(':')[0]
                link_url = link[len(link_name)+1:]
                try:
                    f.write(linkframe.format(link_url, link_name))
                    f.write(newline)
                    print('get {} success'.format(link_name))
                except Exception as e:
                    print (e.args)
        else:
            count = 0
            for link in self.links:
                count += 1
                f.write(linkframe.format(link, count))

        f.close()


