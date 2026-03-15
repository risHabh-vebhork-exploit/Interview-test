from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# To Start browser
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://adnabu-store-assignment1.myshopify.com")

wait = WebDriverWait(driver, 10)


# For entereing  store password
password_field = wait.until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_field.send_keys("AdNabuQA")

enter_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Enter']"))
)
enter_button.click()


# Open search modal
search_icon = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "summary.header__icon--search"))
)
search_icon.click()


# Search for the  product
search_box = wait.until(
    EC.presence_of_element_located((By.ID, "Search-In-Modal"))
)
search_box.send_keys("Snowboard Liquid")

search_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Search']"))
)
search_button.click()


# Select product from search results
product = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "The Collection Snowboard: Liquid"))
)
product.click()


# Add product to cart
add_to_cart = wait.until(
    EC.element_to_be_clickable((By.NAME, "add"))
)
add_to_cart.click()


# To check product added to cart
cart = wait.until(
    EC.presence_of_element_located((By.ID, "cart-icon-bubble"))
)

print("Product successfully added to cart")


# Keep browser open for observation
input("Press Enter to close browser...")

driver.quit()
