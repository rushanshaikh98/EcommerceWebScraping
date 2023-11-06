import scrapy

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from ecomScraper.items import EcomscraperItem


logger = setup_logger('myth_eresa_spider info logger', 'logs/scrapy/myth_eresa_spider.log')


class MythEresaSpider(scrapy.Spider):
    name = "myth_eresa_spider"
    allowed_domains = ["www.mytheresa.com"]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_TIMEOUT': 5
    }

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        BRAND_SELECTOR_PATH = ".productinfo__designer::text"
        NAME_SELECTOR_PATH = ".productinfo__name::text"
        PRICE_SELECTOR_PATH = "span.pricing__prices__original::text"
        IMAGES_SELECTOR_PATH = "div.photocarousel__items img::attr(src)"

        brand = css_selector(response, BRAND_SELECTOR_PATH, 'BRAND NAME', logger)
        name = css_selector(response, NAME_SELECTOR_PATH, 'PRODUCT NAME', logger)
        price = css_selector(response, PRICE_SELECTOR_PATH, 'PRODUCT PRICE', logger)
        images = css_get_all_selector(response, IMAGES_SELECTOR_PATH, 'PRODUCT IMAGES', logger)
        print(images)
        # print(brand, name, price.strip())

        item = EcomscraperItem()
        item['brand_name'] = brand.strip() if brand is not None else None
        item['product_name'] = name.strip() if name is not None else None
        item['product_price'] = price.strip() if price is not None else None
        item['product_image'] = images

        yield item
        print({"status": "success", "data": item})
