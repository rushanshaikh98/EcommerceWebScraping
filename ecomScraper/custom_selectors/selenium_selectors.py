import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def find_element_by_css_selector(driver, element_css, element: str, logger: logging.Logger):
    try:
        value = driver.find_element(By.CSS_SELECTOR, element_css).get_attribute("innerText")
    except NoSuchElementException:
        logger.info("Unable to locate '%s' with '%s' selector '%s' in URL '%s': Element not found in the webpage",
                    element, 'css', element_css, driver.current_url)
        value = None
    return value


def find_elements_by_css_selector(driver, elements_css, element: str, logger: logging.Logger):
    value = driver.find_elements(By.CSS_SELECTOR, elements_css)
    if not value:
        logger.info("Unable to locate '%s' with '%s' selector '%s' in URL '%s': Element not found in the webpage",
                    element, 'css', elements_css, driver.current_url)
    return value


def find_element_by_class_name(driver, element_css_name, element: str, logger: logging.Logger):
    try:
        value = driver.find_element(By.CLASS_NAME, element_css_name).get_attribute("innerText")
    except NoSuchElementException:
        logger.info("Unable to locate '%s' with '%s' selector '%s' in URL '%s': Element not found in the webpage",
                    element, 'classname', element_css_name, driver.current_url)
        value = None
    return value


def find_elements_by_class_name(driver, elements_css_name, element: str, logger: logging.Logger):
    value = driver.find_elements(By.CLASS_NAME, elements_css_name)
    if not value:
        logger.info("Unable to locate '%s' with '%s' selector '%s' in URL '%s': Element not found in the webpage",
                    element, 'css', elements_css_name, driver.current_url)
    return value


def find_element_by_xpath(driver, element_xpath, element: str, logger: logging.Logger):
    try:
        value = driver.find_element(By.XPATH, element_xpath).get_attribute("innerText")
    except NoSuchElementException:
        logger.info("Unable to locate '%s' with '%s' selector '%s' in URL '%s': Element not found in the webpage",
                    element, 'css', element_xpath, driver.current_url)
        value = None
    return value


def find_elements_by_xpath(driver, xpath, element: str, logger: logging.Logger):
    value = driver.find_elements(By.XPATH, xpath)
    if not value:
        logger.info("Unable to locate '%s' with '%s' selector '%s' in URL '%s': Element not found in the webpage",
                    element, 'css', xpath, driver.current_url)
    return value
