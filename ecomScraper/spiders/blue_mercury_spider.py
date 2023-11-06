from urllib.parse import urljoin

import scrapy

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from ecomScraper.items import EcomscraperItem

logger = setup_logger('blue_mercury_spider info logger', 'logs/scrapy/blue_mercury_spider.log')


class ShopBopSpider(scrapy.Spider):
    name = "blue_mercury_spider"
    allowed_domains = ["www.bluemercury.com"]

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        BRAND_SELECTOR_PATH = "h2.ProductInfo__Vendor a::text"
        NAME_SELECTOR_PATH = "h1.ProductInfo__Title::text"
        PRICE_SELECTOR_PATH = "span.MainProductPrice-item::text"
        IMAGES_SELECTOR_PATH = "button.MainProductGallery__ThumbnailButton::attr(data-main-srcset)"

        brand = css_selector(response, BRAND_SELECTOR_PATH, 'BRAND NAME', logger)
        name = css_selector(response, NAME_SELECTOR_PATH, 'PRODUCT NAME', logger)
        price = css_selector(response, PRICE_SELECTOR_PATH, 'PRODUCT PRICE', logger)
        images = css_get_all_selector(response, IMAGES_SELECTOR_PATH, 'PRODUCT IMAGES', logger)

        absolute_image_src = [urljoin(response.url, (image.split())[0].strip()) for image in images]

        item = EcomscraperItem()
        item['brand_name'] = brand.strip() if brand is not None else None
        item['product_name'] = name.strip() if name is not None else None
        item['product_price'] = price.strip() if price is not None else None
        item['product_image'] = absolute_image_src

        yield item
        print({"status": "success", "data": item})
