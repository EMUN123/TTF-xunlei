from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import re
import time

class Downloader(object):

    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url

    def download(self):
        '''
        we use selenium to click and download as there is 
        an unresolved problem about page jump
        '''
        driver = webdriver.Chrome()
        driver.get(self.url)
        
        # when we need to click, it's more efficient to use clickable than presence
        download_click = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div/table/tbody/tr/td[1]/div/ul/li[1]/a')))
        download_click.click()
        time.sleep(2)
        
        # check .crdownload file in chrome download directory, if not, then download success, browser window closed
        try:
            for i in range(60):
                # in the following codes, I almost made every important mistakes about re...
                file_list = os.listdir(r'C:\Users\HZB\Downloads')  # change username here
                file_str = "match".join(file_list)
                '''
                re can't deel with "()" in english, we need to switch it into sth else
                '''
                file_str = file_str.replace('(', '')
                file_str = file_str.replace(')', '')
                
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
                we add 'r' before the pattern to be compiled is just to avoid Escapes '\'
                in python like '\n, \t, ...',  '\' in re is not Escapes.'r' means raw
                string is only for Escapes'\' to stand for normal symbol '\', and '\' in re is not one kind of them, also
                'r' can not mean totally raw for all characters lie '$ # > <', which have
                special meaning in re. We can also use '\\' to avoid misunderstanding of symbol
                '\' and Escapes '\'
                '''
                regex = re.compile(r'match([\u4e00-\u9fa5]+.*?).crdownload')  # so here '\' will  not means for '\u'
                if regex.findall(file_str):
                    print('downloading...')
                    time.sleep(0.5)  # check for every 0.5s if the file is downloaded...
                else:
                    time.sleep(1)
                    print('download success!')
                    break
                    driver.close()
        except:
            # after checking 60times in 30s
            print('sorry, downloading overtime, please check your Internet...')
            print('you can also try to clean the unfinished downloads in Chrome~')
            driver.close()

            
        # further optimization: use re to extract the file before .crdownload
        # and then we use the file name to check the file existence 
        # if it exists, then downloading is successul
        # thus we can reduce errors in Chromm downloading and the introduce 
        # multi-thread to speed up downloading

        # also try to minimize our window         