from scrapy.http import FormRequest
from scrapy.item import Item, Field
from scrapy.selector import HtmlXPathSelector

from scrapy.spider import BaseSpider

class QuotesSpider(BaseSpider):
    name = "smr"

    def start_requests(self):
        urls = [
            'https://www.siliconmilkroundabout.com/companies',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        companies = response.xpath("/html/body/div[3]/div[6]").extract()
#            for company in companies:
#                url = urljoin(response.url, p)



    def parse_company(self, response):
        yield {

        }
