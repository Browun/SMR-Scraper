from selenium import webdriver
from selenium.webdriver.common.keys import Keys

elements =[["roleType","d"], ["tagType","p"], ["dayType","ss"]]

driver = webdriver.Firefox()
driver.get("https://www.siliconmilkroundabout.com/companies")
for element in elements:
    elem = driver.find_element_by_id(element[0])
    elem.send_keys(element[1])
    elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
