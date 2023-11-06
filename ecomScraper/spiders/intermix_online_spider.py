import scrapy

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from ecomScraper.items import EcomscraperItem

logger = setup_logger('intermix_online_spider info logger', 'logs/scrapy/intermix_online_spider.log')


class IntermixOnlineSpider(scrapy.Spider):
    name = "intermix_online_spider"
    allowed_domains = ["www.intermixonline.com"]

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        BRAND_SELECTOR_PATH = ".product-brandname::text"
        NAME_SELECTOR_PATH = ".product-name::text"
        PRICE_SELECTOR_PATH = ".product-price span::text"
        IMAGES_SELECTOR_PATH = "div.swiper-container.product-main-images img::attr(src)"

        brand = css_selector(response, BRAND_SELECTOR_PATH, 'BRAND NAME', logger)
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
