# tests/test_amazon.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.homepage import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url.lower()
    print("\nOpened Amazon HomePage Successfully")


def test_search_product(driver):
    # Directly perform the search using Selenium
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
    search_box.send_keys("wireless mouse" + Keys.ENTER)

    # Wait for search results to appear
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a h2 span")))

    print("\nSearch completed successfully")


def test_find_product_amazon(driver):
    # Perform search manually to ensure results appear
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
    search_box.send_keys("wireless mouse" + Keys.ENTER)

    # Wait for product results
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a h2 span")))

    productlistingpage = ProductListingPage(driver)
    productlistingpage.find_product_title()
    val = productlistingpage.all_products()

    assert val, "No products found on Amazon search results!"


def test_brand_filter(driver):
    productlistingpage = ProductListingPage(driver)
    productlistingpage.select_brand_filter()
    assert productlistingpage.check_product_titles_for_brand_filter("Logitech"), 'Brand filter did not apply!'