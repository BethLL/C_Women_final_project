from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login(driver, email, password):
    driver.get("https://demo.guru99.com/insurance/v1/index.php")
    driver.maximize_window()

    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()

    success1 = driver.get_screenshot_as_file("login_screenshot.png")
    if success1:
        print("Login screenshot saved successfully.")
    else:
        print("Failed to save login screenshot.")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/form/input")))
    print("Login successful")

def logout(driver):
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/form/input"))
    )
    logout_button.click()

    email_label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='login-form']/div[1]/label"))
    )
    fetched_text = email_label.text
    assert fetched_text == "Email", f"Expected 'Email', but got '{fetched_text}'"

    success2 = driver.get_screenshot_as_file("logout_screenshot.png")
    if success2:
        print("Logout screenshot saved successfully.")
    else:
        print("Failed to save logout screenshot.")

    print("Logout successful")

def test_login_and_logout():
    driver = webdriver.Chrome()
    try:
        email_login = "fake@htmail.com"
        password_login = "test123"

        login(driver, email_login, password_login)
        time.sleep(3)
        logout(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_and_logout()
