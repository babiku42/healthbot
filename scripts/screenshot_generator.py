# scripts/screenshot_generator.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set URL of your deployed app
URL = "https://chatbotforhealth.streamlit.app/"

# Set output screenshot path relative to project root
OUTPUT_PATH = "assets/health_chatbot_screenshot.png"

# Setup headless Chrome browser
options = Options()
options.headless = True
options.add_argument("--window-size=1280,1024")
driver = webdriver.Chrome(options=options)

try:
    print(f"Opening {URL}")
    driver.get(URL)

    # Wait for Streamlit app to load
    time.sleep(10)

    # Save screenshot
    driver.save_screenshot(OUTPUT_PATH)
    print(f"Screenshot saved to {OUTPUT_PATH}")
finally:
    driver.quit()
