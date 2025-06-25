from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- Replace with your dummy credentials ---
USERNAME = "your_dummy_username"
PASSWORD = "your_dummy_password"
TARGET_USER = "cbitosc"

def login(driver):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").submit()
    time.sleep(7)

def search_and_follow(driver):
    driver.get(f"https://www.instagram.com/{TARGET_USER}/")
    time.sleep(5)

    # Try to follow
    try:
        follow_btn = driver.find_element(By.XPATH, "//button[text()='Follow']")
        follow_btn.click()
        time.sleep(2)
    except:
        print("Already following or button not found.")

    # Grab stats
    stats = driver.find_elements(By.CLASS_NAME, "_ac2a")
    data = [el.text for el in stats[:3]]

    with open("output.txt", "w") as f:
        f.write(f"Instagram Data for @{TARGET_USER}\n")
        f.write(f"Posts: {data[0]}\nFollowers: {data[1]}\nFollowing: {data[2]}\n")

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Headless mode (no browser UI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        login(driver)
        search_and_follow(driver)
    finally:
        driver.quit()
