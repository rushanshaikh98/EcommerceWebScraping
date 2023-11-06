import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ecomScraper.custom_logging import setup_logger
from ecomScraper.custom_selectors.selenium_selectors import find_element_by_css_selector, find_elements_by_css_selector, \
    find_element_by_xpath

logger = setup_logger('nordstrom_scraper info logger', 'logs/selenium/nordstrom.log')


def nordstrom_scraper(url: str):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/83.0.4103.116 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.get(url)

    time.sleep(5)

    BRAND_SELECTOR_PATH = "a.WMXkS span"
    NAME_SELECTOR_PATH = "//div[@id='product-page-product-title-lockup']//h1[@class='dls-t8nrr7']"
    PRICE_SELECTOR_PATH = ".PLdP6.GmKV9.KCp6h.IHuaj.QkVyF .ggbBg.y3xFi .qHz0a.EhCiu.dls-1n7v84y"
    IMAGES_SELECTOR_PATH = "span.D1B50 img"

    try:
        # image = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, IMAGES_SELECTOR_PATH)))
        brand = find_element_by_css_selector(browser, BRAND_SELECTOR_PATH, "BRAND NAME", logger)
        name = find_element_by_xpath(browser, NAME_SELECTOR_PATH, "PRODUCT NAME", logger)
        price = find_element_by_css_selector(browser, PRICE_SELECTOR_PATH, "PRODUCT PRICE", logger)
        images = find_elements_by_css_selector(browser, IMAGES_SELECTOR_PATH, "PRODUCT IMAGE", logger)
        absolute_image_src = [image.get_attribute('src') for image in images]

        item = {
            'brand_name': brand,
            'product_name': name,
            'product_price': price,
            'product_image': absolute_image_src
        }
        browser.close()
        return {"status": "success", "data": item}
    except Exception as err:
        print(err)
        return {"status": "error", "data": {}}
