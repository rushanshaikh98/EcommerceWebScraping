import json

import scrapy

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, xpath_selector
from ecomScraper.items import EcomscraperItem


logger = setup_logger('shop_bop_spider info logger', 'logs/scrapy/shop_bop_spider.log')


class ShopBopSpider(scrapy.Spider):
    name = "shop_bop_spider"
    allowed_domains = ["www.shopbop.com"]

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        BRAND_SELECTOR_PATH = "span.brand-name::text"
        NAME_SELECTOR_PATH = "//div[@id='product-title']//text()"
        PRICE_SELECTOR_PATH = "span.pdp-price::text"
        # IMAGES_SELECTOR_PATH = "//div[@id='product-image-container']//div[@class='DesktopGallery__LazyComponentWrapper-sc-1jxrbk9-1 eEJoHM']//img/@src"
        PRODUCT_DETAILDS_SCRIPT_TAG_SELECTOR_PATH = "//*[@id='pdp']/div[1]/script[2]//text()"

        brand = css_selector(response, BRAND_SELECTOR_PATH, 'BRAND NAME', logger)
        name = xpath_selector(response, NAME_SELECTOR_PATH, 'PRODUCT NAME', logger)
        price = css_selector(response, PRICE_SELECTOR_PATH, 'PRODUCT PRICE', logger)
        script_text_data = xpath_selector(response, PRODUCT_DETAILDS_SCRIPT_TAG_SELECTOR_PATH, 'PRODUCT IMAGES', logger)

        images = []
        if script_text_data:
            json_data = json.loads(script_text_data)
            images_dicts = json_data['product']['styleColors'][0]['images']
            images = [image_dict['url'] for image_dict in images_dicts]

        item = EcomscraperItem()
        item['product_name'] = name
        item['brand_name'] = brand
        item['product_image'] = images
        item['product_price'] = price

        yield item
        print({"status": "success", "data": item})
