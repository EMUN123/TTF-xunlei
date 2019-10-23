import os
import re

# in the following codes, I almost made every important mistakes about re...
file_list = os.listdir(r'C:\Users\HZB\Downloads')
file_str = "match".join(file_list)
'''
re can't deel with "()" in english, we need to switch it into sth else
'''
file_str = file_str.replace('(', '')
file_str = file_str.replace(')', '')
print(file_str)
'''
re can't affectively compile blankspace and tabs
'''

'''
re also can't direct compile '$ < > /'... and maybe other special characters
as they stand for different meanings in re
'''

'''
we need to use [\u4e00-\u9fa5]+ to match Chinese characters
'''

'''
we add 'r' before the pattern to be compiled is just to avoid 
'''
regex = re.compile(r'match([\u4e00-\u9fa5]+.*?).crdownload')
if regex.findall(file_str):
    print('yes')