from bs4 import BeautifulSoup
import requests

url = 'https://www.siliconmilkroundabout.com/companies'

def get_company_page(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    print(soup)
    # images = soup.find_all('img')
    # image_list = [image['src'] for image in images]
    # target_image = "Banner_I"

get_company_page(url)
