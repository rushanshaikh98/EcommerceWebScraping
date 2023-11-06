import scrapy

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from ecomScraper.items import EcomscraperItem

logger = setup_logger('saks_fifth_avenue_spider info logger', 'logs/scrapy/saks_fifth_avenue_spider.log')


class SaksFifthAvenueSpider(scrapy.Spider):
    name = "saks_fifth_avenue_spider"
    allowed_domains = ["www.saksfifthavenue.com"]

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        BRAND_SELECTOR_PATH = "h1.product-brand-name.d-none.d-sm-block a::text"
        NAME_SELECTOR_PATH = "h1.product-name.h2.d-none.d-sm-block::text"
        PRICE_SELECTOR_PATH = "span.value.bfx-price::attr(content)"
        IMAGES_SELECTOR_PATH = "ul.primary-thumbnails img::attr(src)"

        brand = css_selector(response, BRAND_SELECTOR_PATH, 'BRAND NAME', logger)
        name = css_selector(response, NAME_SELECTOR_PATH, 'PRODUCT NAME', logger)
        price = css_selector(response, PRICE_SELECTOR_PATH, 'PRODUCT PRICE', logger)
        images = css_get_all_selector(response, IMAGES_SELECTOR_PATH, 'PRODUCT IMAGES', logger)

        item = EcomscraperItem()
        item['product_name'] = name
        item['brand_name'] = brand
        item['product_image'] = images
        item['product_price'] = price

        yield item
        print({"status": "success", "data": item})
