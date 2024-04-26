import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configure Chrome to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

# Initialize WebDriver with headless Chrome
driver = webdriver.Chrome(options=chrome_options)

# Open the webpage
driver.get("https://hindpage.site/direct/index.php?url=aHR0cHM6Ly9teS5mYXJpaGFqcGwxNXljb20ud29ya2Vycy5kZXYvMDovd2lzZSUyMDEzLzEwMS9VbmNoYXJ0ZWQuMjAyMi43MjBwLkJsdVJheS5IaW5kaS1FbmdsaXNoLngyNjQuRVN1Yi5ta3Y=&redirectid=1714127733")

# Wait for the page to load (optional)
# driver.implicitly_wait(10)  # Wait for 10 seconds for elements to appear

# Print page loaded
print("Page loaded.")

# Print page title
print("Page title:", driver.title)

try:
    # This XPath selects the button with id 'download-btn1' and text 'Server 1'
    button_xpath = "//a[@id='download-btn1' and contains(text(),'Server 1')]"

    # Find the button element using XPath
    button_element = driver.find_element(By.XPATH, button_xpath)

    # Click the button
    button_element.click()

    # Print button clicked
    print("Button clicked. Downloading...")

    # Wait for 30 minutes before quitting
    time.sleep(1800)  # 30 minutes = 30 * 60 seconds

except Exception as e:
    # Print error if button is not found or any other exception occurs
    print("Error:", e)

# Close the browser
driver.quit()
