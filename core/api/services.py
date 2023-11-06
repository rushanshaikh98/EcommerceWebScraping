import subprocess
import urllib.parse

from flask import request
from flask_api import status
from flask_restful import Resource

from core.constants import SCRAPER_INVALID_RESPONSE, INVALID_PRODUCT_URL, URL_TO_SCRAPY_SPIDER_MAPPER, \
    URL_TO_SELENIUM_SCRAPER_MAPPER


class ProductDetailAPI(Resource):
    def post(self):
        input_json = request.get_json()
        try:
            url = input_json["url"]
            domain_name = urllib.parse.urlparse(url).hostname
            if domain_name in URL_TO_SCRAPY_SPIDER_MAPPER:
                data = subprocess.run(
                    ['scrapy', 'crawl', URL_TO_SCRAPY_SPIDER_MAPPER[domain_name], "-a", f'product_url={url}'],
                    capture_output=True, text=True)
                if not (data.stdout and (result := eval(data.stdout))):
                    result = {"status": "error", "details": SCRAPER_INVALID_RESPONSE}
                return result if result['status'] == 'success' else result

            elif domain_name in URL_TO_SELENIUM_SCRAPER_MAPPER:
                return URL_TO_SELENIUM_SCRAPER_MAPPER[domain_name](url)

            return {"data": [],
                    "message": INVALID_PRODUCT_URL,
                    "status": "FALSE"}, status.HTTP_400_BAD_REQUEST

        except (KeyError, AttributeError):
            return {"status": "error"}, status.HTTP_400_BAD_REQUEST
