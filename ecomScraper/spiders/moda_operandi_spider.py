import scrapy

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from ecomScraper.items import EcomscraperItem


logger = setup_logger('moda_operandi_spider info logger', 'logs/scrapy/moda_operandi_spider.log')


class ModaOperandSpider(scrapy.Spider):
    name = "moda_operandi_spider"
    allowed_domains = ["www.modaoperandi.com"]

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):

        BRAND_SELECTOR_PATH = "a.ProductDetails__designer::text"
        NAME_SELECTOR_PATH = "h1.ProductDetails__name::text"
        PRICE_SELECTOR_PATH = "span.PDPProductPrice__current-price::text"
        IMAGES_SELECTOR_PATH = "div.DesktopProductMediaGallery__images-only img::attr(src)"

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
