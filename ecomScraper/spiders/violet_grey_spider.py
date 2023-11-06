import scrapy

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from ecomScraper.items import EcomscraperItem

logger = setup_logger('violet_grey_spider info logger', 'logs/scrapy/violet_grey_spider.log')


class VioletGreySpider(scrapy.Spider):
    name = "violet_grey_spider"
    allowed_domains = ["www.violetgrey.com"]

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': "violet_grey (+http://www.yourdomain.com)"
        }
    }

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        BRAND_SELECTOR_PATH = "body div div main div div div div a::text"
        NAME_SELECTOR_PATH = "body div div main div div div div h1::text"
        PRICE_SELECTOR_PATH = "body div div main div div div div div span::text"
        IMAGES_SELECTOR_PATH = "div[data-test='thumbnail'] img::attr(srcset)"

        brand = css_selector(response, BRAND_SELECTOR_PATH, 'BRAND NAME', logger)
        name = css_selector(response, NAME_SELECTOR_PATH, 'PRODUCT NAME', logger)
        price = css_selector(response, PRICE_SELECTOR_PATH, 'PRODUCT PRICE', logger)
        images = css_get_all_selector(response, IMAGES_SELECTOR_PATH, 'PRODUCT IMAGES', logger)

        absolute_image_src = [(image.split())[-2].strip() for image in images]

        item = EcomscraperItem()
        item['brand_name'] = brand.strip() if brand is not None else None
        item['product_name'] = name.strip() if name is not None else None
        item['product_price'] = price.strip() if price is not None else None
        item['product_image'] = absolute_image_src

        yield item
        print({"status": "success", "data": item})
