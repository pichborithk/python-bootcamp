from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configuration to keep chrome driver open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/SAMSUNG-34-Inch-Ultra-Wide-FreeSync-LC34G55TWWNXZA/dp/B08MVBYWGQ/?th=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# price_cents = driver.find_element(By.CSS_SELECTOR, value=".a-price > span > span.a-price-fraction")
price_cents = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[3]')

print(f"The price is {price_dollar.text}.{price_cents.text}")

# samsung_store = driver.find_element(By.LINK_TEXT, "Visit the SAMSUNG Store")
# samsung_store.click()

amazon_search = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
amazon_search.send_keys("Ultra-Wide Monitor 34-Inch")
amazon_search.send_keys(Keys.ENTER)

# driver.close()  # Close a tab
driver.quit()  # Quit driver
