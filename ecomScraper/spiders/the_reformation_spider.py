import scrapy

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from ecomScraper.items import EcomscraperItem

logger = setup_logger('the_reformation_spider info logger', 'logs/scrapy/the_reformation_spider.log')


class TheReformationSpider(scrapy.Spider):
    name = "the_reformation_spider"
    allowed_domains = ["www.thereformation.com"]

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        NAME_SELECTOR_PATH = "h1[data-product-component='name']::text"
        PRICE_SELECTOR_PATH = "div[data-product-container='pdp'] span[itemprop='price'] span:nth-child(1)::text"
        IMAGES_SELECTOR_PATH = "div.product-gallery-grid--pdp img::attr(cl-data-src)"

        brand = "the reformation"
        name = css_selector(response, NAME_SELECTOR_PATH, 'PRODUCT NAME', logger)
        price = css_selector(response, PRICE_SELECTOR_PATH, 'PRODUCT PRICE', logger)
        images = css_get_all_selector(response, IMAGES_SELECTOR_PATH, 'PRODUCT IMAGES', logger)

        item = EcomscraperItem()
        item['brand_name'] = brand.strip() if brand is not None else None
        item['product_name'] = name.strip() if name is not None else None
        item['product_price'] = price.strip() if price is not None else None
        item['product_image'] = images

        yield item
        print({"status": "success", "data": item})
