# pages/homepage.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePage:
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    # Amazon continue shopping button
    CONTINUE_SHOPPING_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Continue shopping')]"
    )

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def handle_continue_shopping_popup(self):
        try:
            continue_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    self.CONTINUE_SHOPPING_BUTTON
                )
            )
            continue_btn.click()
            print("Continue shopping popup handled")

        except TimeoutException:
            # Popup not shown
            pass

    def type_search_input(self, search_text: str):

        # Handle popup first
        self.handle_continue_shopping_popup()

        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )

        search_box.clear()
        search_box.send_keys(search_text)

    def click_search_button(self):
        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        search_button.click()

    def search_product(self, product_name: str):
        self.type_search_input(product_name)
        self.click_search_button()

    def is_amazon_page_loaded(self) -> bool:
        return (
            "amazon" in self.driver.current_url.lower()
            and "amazon" in self.driver.title.lower()
        )