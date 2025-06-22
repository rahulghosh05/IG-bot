import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# === SETTINGS ===
USERNAME = "your_username_here"
PASSWORD = "your_password_here"
ARTIST_USERNAME = "artist_username_here"  # e.g. "kendricklamar"

comment_bank = [
    "It is my dream to work with you. I’ll do whatever it takes to make it happen.",
    "I’ll DM you every day until you notice me — just one shot, that’s all I’m asking.",
    "Every single post inspires me more. I’m ready to collab when you are.",
    "This is a manifestation comment. One day, we’re going to work together.",
    "I would drop everything for the chance to create something with you.",
    "If I had one wish, it would be to collab with you. No joke.",
    "You are the artist that made me start dreaming bigger. Let’s create together.",
    "I’ll be here. Commenting, watching, waiting for that moment we make something real.",
    "There’s nothing I want more than to build something legendary with you.",
    "You don’t know me yet — but I’m going to earn a collab with you.",
    "I will DM you until it happens. I’m hungry for this.",
    "I’m not here to be a fan. I’m here to be a future collab.",
    "Imagine your art and mine colliding — it’s not a dream, it’s a goal.",
    "Commenting daily until we link. Manifesting this collab into existence.",
    "I truly believe we’d make something unforgettable together.",
    "I don’t care how long it takes. I’ll earn this collab.",
    "This is bigger than admiration. This is creative obsession.",
    "If persistence counts for anything, I hope you see this one day.",
    "This is my shot — my dream collab is with YOU.",
    "When we do collab, this comment will be the prophecy.",
    "I'm not just a follower. I'm a future collaborator.",
    "Call it what you want — I call it dedication. Let’s work.",
    "One day soon, this comment will be the start of our collab story.",
    "I’ll keep knocking until the door opens. Let’s make art.",
    "All I ask for is one chance to show you what we can create together."
]

# === SCRIPT ===
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Login
driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
time.sleep(7)

# Go to artist profile
driver.get(f"https://www.instagram.com/{ARTIST_USERNAME}/")
time.sleep(5)

# Click on first 3 posts and comment
posts = driver.find_elements(By.CLASS_NAME, "_aagw")[:3]

for i, post in enumerate(posts):
    try:
        post.click()
        time.sleep(4)

        comment_area = driver.find_element(By.CSS_SELECTOR, "textarea")
        comment_area.click()
        time.sleep(1)

        comment = random.choice(comment_bank)
        comment_area.send_keys(comment)
        time.sleep(1)
        comment_area.send_keys(Keys.RETURN)
        print(f"✅ Commented on post {i+1}: {comment}")
        time.sleep(random.randint(10, 20))

        driver.find_element(By.CSS_SELECTOR, "[aria-label='Close']").click()
        time.sleep(3)
    except Exception as e:
        print(f"⚠️ Error on post {i+1}: {e}")
        continue

driver.quit()
