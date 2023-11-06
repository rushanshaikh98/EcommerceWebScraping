# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcomscraperItem(scrapy.Item):
    # define the fields for your item here like:
    brand_name = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_image = scrapy.Field()
