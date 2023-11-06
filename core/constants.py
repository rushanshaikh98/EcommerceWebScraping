from ecomScraper.selenium_scrapers.artizia import artizia_scraper
from ecomScraper.selenium_scrapers.farfetch import farfetch_scraper
from ecomScraper.selenium_scrapers.luisaviaroma import luisaviaroma_scraper
from ecomScraper.selenium_scrapers.nordstorm import nordstrom_scraper
from ecomScraper.selenium_scrapers.outnet import outnet_scraper
from ecomScraper.selenium_scrapers.hm import h_and_m_scraper
from ecomScraper.selenium_scrapers.real import real_scraper
from ecomScraper.selenium_scrapers.revolve import revolve_scraper
from ecomScraper.selenium_scrapers.sense import sense_scraper
from ecomScraper.selenium_scrapers.sephora import sephora_scraper
from ecomScraper.selenium_scrapers.uniqlo import uniqlo_scraper
from ecomScraper.selenium_scrapers.zara import zara_scraper

INVALID_PRODUCT_URL = "Scraping is not supported for this website by the API."
SCRAPER_INVALID_RESPONSE = "Scraper failed to send a valid response."

URL_TO_SCRAPY_SPIDER_MAPPER = {"www.matchesfashion.com": 'matches_fashion_spider',
                               'www.net-a-porter.com': "net_a_porter_spider",
                               'www.saksfifthavenue.com': "saks_fifth_avenue_spider",
                               "www.shopbop.com": "shop_bop_spider",
                               "www.modaoperandi.com": "moda_operandi_spider",
                               "bluemercury.com": "blue_mercury_spider",
                               "www.intermixonline.com": "intermix_online_spider",
                               "www.mytheresa.com": "myth_eresa_spider",
                               "poshmark.com": "poshmark_spider",
                               "www.thereformation.com": "the_reformation_spider",
                               "www.violetgrey.com": "violet_grey_spider"}


URL_TO_SELENIUM_SCRAPER_MAPPER = {
    'www.theoutnet.com': outnet_scraper,
    'www.aritzia.com': artizia_scraper,
    'www.farfetch.com': farfetch_scraper,
    'www2.hm.com': h_and_m_scraper,
    'www.luisaviaroma.com': luisaviaroma_scraper,
    'www.zara.com': zara_scraper,
    'www.uniqlo.com': uniqlo_scraper,
    'www.therealreal.com': real_scraper,
    'www.ssense.com': sense_scraper,
    'www.revolve.com': revolve_scraper,
    'www.sephora.com': sephora_scraper,
    'www.nordstrom.com': nordstrom_scraper
}
