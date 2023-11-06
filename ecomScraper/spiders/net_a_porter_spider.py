import scrapy

from ..custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from ..items import EcomscraperItem


logger = setup_logger('net_a_porter_spider info logger', 'logs/scrapy/net_a_porter_spider.log')


class NetAPortersSpider(scrapy.Spider):
    name = "net_a_porter_spider"
    allowed_domains = ["www.net-a-porter.com"]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_TIMEOUT': 5
    }

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        BRAND_SELECTOR_PATH = "h1.ProductInformation86__designer *::text"
        NAME_SELECTOR_PATH = "p.ProductInformation86__name::text"
        PRICE_SELECTOR_PATH = "span.PriceWithSchema9__value.PriceWithSchema9__value--details *::text"
        IMAGES_SELECTOR_PATH = "div.ImageCarousel86__thumbnails img.Image18__image.Image18__image--noScript::attr(src)"

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
