from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Search(object):
    def __init__(self, url, text):
        self.url = url
        self.text = text

    def search(self):
        browser = webdriver.Chrome()
        browser.get(self.url)
        browser.minimize_window()

        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="s"]'))

        # 获取搜索结果
        browser.find_element_by_xpath('//*[@id="s"]').send_keys(self.text)
        search_click = browser.find_element_by_xpath(
            '''//*[@id="db-nav-movie"]/div[1]/div/div[2]/form
            /fieldset/div[2]/input'''
        )
        search_click.click()
        EC.presence_of_all_elements_located(
            (By.XPATH, '//*[@id="breadcrumbs"]/div/a')
            )
        return browser.current_url
