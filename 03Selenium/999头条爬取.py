from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import csv,json

url = "http://www.toutiao.com"
driver = webdriver.Firefox()
driver.get(url)
search_text = driver.find_element_by_xpath('//input[@class="tt-input__inner"]')
search_text.clear()
search_text.send_keys(u"numpy")
search_text.send_keys(Keys.RETURN)
time.sleep(3)
# name =driver.window_handles
# driver.switch_to_window(name[0])

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if u"numpy" in driver.title:
        #网页翻页
        for i in range(8):
            js = "var q=document.documentElement.scrollTop=100000"
            driver.execute_script(js)
            time.sleep(2)
            i += 1
        text_urls = [i.get_attribute('href') for i in driver.find_elements_by_xpath('//a[@class="link title"]')]
        # html = driver.page_source
        # soup = BeautifulSoup(html, 'html.parse', from_encoding='utf-8')
        split_urls = [re.search((r'\d+'), text_url).group() for text_url in text_urls]
        result = []
        for split_url in split_urls:
            # result['title'] = driver.find_element_by_xpath('//a[@href="/group/' + split_url + '/"]/span[@class="J_title"]').text
            # result['text_url'] = 'https://www.toutiao.com/a'+split_url+'/'
            title = driver.find_element_by_xpath('//a[@href="/group/' + split_url + '/"]/span[@class="J_title"]').text
            text_url = 'https://www.toutiao.com/a'+split_url+'/'
            result.append((title, text_url))

        with open('result.json', 'w') as file:
            json.dump(result, fp=file, indent=4, ensure_ascii=False)

        headers = ['title', 'text_url']
        rows = result

        with open('result.csv', 'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(rows)

        driver.close()
    else:
        driver.close()


