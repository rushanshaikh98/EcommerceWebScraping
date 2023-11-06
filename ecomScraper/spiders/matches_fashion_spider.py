from urllib.parse import urljoin

import scrapy

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from ecomScraper.items import EcomscraperItem

logger = setup_logger('matches_fashion_spider info logger', 'logs/scrapy/matches_fashion_spider.log')


class MatchesFashionSpider(scrapy.Spider):
    name = "matches_fashion_spider"
    allowed_domains = ["www.matchesfashion.com"]

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        BRAND_SELECTOR_PATH = "h1.chakra-heading.pdp-headline.css-183qeze a.chakra-link.css-xgrtoc *::text"
        NAME_SELECTOR_PATH = "h1.chakra-heading.pdp-headline.css-183qeze span.chakra-text.css-uyrcxy::text"
        PRICE_SELECTOR_PATH = "span.chakra-text.css-k1gaaj::text"
        IMAGES_SELECTOR_PATH = "div.carousel__slider-tray-wrapper.carousel__slider-tray-wrap--horizontal img::attr(src)"

        brand = css_selector(response, BRAND_SELECTOR_PATH, 'BRAND NAME', logger)
        name = css_selector(response, NAME_SELECTOR_PATH, 'PRODUCT NAME', logger)
        price = css_selector(response, PRICE_SELECTOR_PATH, 'PRODUCT PRICE', logger)
        images = css_get_all_selector(response, IMAGES_SELECTOR_PATH, 'PRODUCT IMAGES', logger)

        absolute_image_src = [urljoin(response.url, image) for image in images]

        item = EcomscraperItem()
        item['brand_name'] = brand
        item['product_name'] = name
        item['product_price'] = price
        item['product_image'] = absolute_image_src

        yield item
        print({"status": "success", "data": item})
