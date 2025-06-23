from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Your credentials
USERNAME = 'yuunmebot'
PASSWORD = 'yuunmebot12345'

# Comment bank
comment_bank = [
    "This is insane 🔥",
    "Always leveling up 💯",
    "Massive respect 🙏",
    "Next level stuff",
    "Insane fits 🧢",
    "Big inspiration 💥"
]

# Setup Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Step 1: Go to Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Step 2: Log in
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)

time.sleep(7)

# Step 3: Go to Offgod's profile
driver.get("https://www.instagram.com/yalocaloffgod/")
time.sleep(5)

# Step 4: Scroll a bit to load posts
driver.execute_script("window.scrollTo(0, 1000);")
time.sleep(3)

# Step 5: Click the first post
try:
    post_links = driver.find_elements(By.CSS_SELECTOR, 'article a')
    if post_links:
        post_links[0].click()
        time.sleep(3)
    else:
        print("❌ No posts found.")
        driver.quit()
        exit()
except Exception as e:
    print(f"❌ Error loading posts: {e}")
    driver.quit()
    exit()

# Step 6: Comment on up to 3 posts
for i in range(3):
    try:
        comment_area = driver.find_element(By.CSS_SELECTOR, "textarea")
        comment_area.click()
        time.sleep(1)

        comment = random.choice(comment_bank)
        comment_area.send_keys(comment)
        comment_area.send_keys(Keys.RETURN)

        print(f"✅ Commented on post {i+1}: {comment}")
        time.sleep(random.randint(5, 8))

        # Click next post
        next_button = driver.find_element(By.XPATH, "//div[contains(@class,'_aaqg')]/button")
        next_button.click()
        time.sleep(3)

    except Exception as e:
        print(f"⚠️ Error on post {i+1}: {e}")
        break

# Step 7: Quit browser
driver.quit()
