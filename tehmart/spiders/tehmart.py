import scrapy
from ..items import TehmartItem
from scrapy.linkextractors import LinkExtractor


class TehmartSpider(scrapy.Spider):
    name = 'tehmart'
    start_urls = [
        'https://www.tehmart.ir/'
    ]

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            if '/product/' in link.url:
                yield response.follow(link.url, self.parse_genre)

    def parse_genre(self, response):
        for product in response.xpath('//*[@id="productsList"]/div/div/div/a'):
            url = product.xpath('@href').get()
            yield response.follow(url, self.parse_product)
        next_page = response.xpath('//li[@class="pagination-next"]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse_genre)

    def parse_product(self, response):
        items = TehmartItem()
        items['name'] = response.xpath(
            '//*[(@id = "productInfoName")]/text()').get()
        items['price'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "productSpecialPrice", " " ))]/text()').get()
        items['price_before_discount'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "productOldPrice", " " ))]/text()').get()
        items['description'] = response.xpath('string(//*[@id="productDescription"])').get()
        product_specifications_dic = {}
        for t in response.xpath('//*[@class="field-row"]'):
            product_specifications_dic[
                t.xpath('string(td[@class="field-name"])').get()] \
                = t.xpath('string(td[@class="field-value"])').get()
        items['specifications'] = product_specifications_dic
        yield items
