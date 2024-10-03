from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_and_logout():
    # Test Case 1: logging in
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/insurance/v1/index.php")
    driver.maximize_window()

    email_login = "fake@htmail.com"
    password_login = "test123"

    driver.find_element(By.ID, "email").send_keys(email_login)
    driver.find_element(By.ID, "password").send_keys(password_login)
    driver.find_element(By.NAME, "submit").click()
    success = driver.get_screenshot_as_file("screenshot.png")
    if success:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")

    time.sleep(3)
    print("Login successful")

    # Test Case 2: logging out
    logout = driver.find_element(By.XPATH, "/html/body/div[3]/form/input")
    logout.click()

    element = driver.find_element(By.XPATH, "//*[@id='login-form']/div[1]/label")
    fetched_text = element.text
    assert fetched_text == "Email", f"Expected 'Email', but got '{fetched_text}'"
    time.sleep(3)
    print("Logout successful")

    driver.quit()
