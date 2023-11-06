from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.selenium_selectors import find_element_by_css_selector, find_elements_by_css_selector, \
    find_element_by_class_name

logger = setup_logger('luisaviaroma_scraper info logger', 'logs/selenium/luisaviaroma.log')


def luisaviaroma_scraper(url: str):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/83.0.4103.116 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.maximize_window()
    browser.get(url)

    BRAND_SELECTOR_PATH = "_3xn2Q0OBek"
    NAME_SELECTOR_PATH = "_ii5gBPNiQY"
    PRICE_SELECTOR_PATH = "div[itemprop='offers'] strong"
    IMAGES_SELECTOR_PATH = "div._2MXcmjsm-X img"

    brand = find_element_by_class_name(browser, BRAND_SELECTOR_PATH, "BRAND NAME", logger)
    name = find_element_by_class_name(browser, NAME_SELECTOR_PATH, "PRODUCT NAME", logger)
    price = find_element_by_css_selector(browser, PRICE_SELECTOR_PATH, "PRODUCT PRICE", logger)
    images = find_elements_by_css_selector(browser, IMAGES_SELECTOR_PATH, "PRODUCT IMAGE", logger)

    absolute_image_src = ["https:" + image.get_attribute('srcset').split()[-2] for image in images]

    item = {
        'brand_name': brand,
        'product_name': name,
        'product_price': price,
        'product_image': absolute_image_src
    }
    browser.close()
    return {"status": "success", "data": item}
