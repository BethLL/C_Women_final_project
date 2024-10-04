import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/insurance/v1/index.php")
    driver.maximize_window()

    register_button = driver.find_element(By.XPATH, "/html/body/div[3]/a")
    register_button.click()
    time.sleep(5)

    form_data = {
        ("user_firstname", "Lucia"),
        ("user_surname", "Palomares"),
        ("user_phone", "1234567890"),
        ("user_dateofbirth_1i", "1990"),
        ("user_dateofbirth_2i", "January"),
        ("user_dateofbirth_3i", "1"),
        ("user_licenceperiod", "5"),
        ("user_occupation_id", "Nurse"),
        ("user_address_attributes_street", "123 Road St"),
        ("user_address_attributes_city", "Hamilton"),
        ("user_address_attributes_county", "Canada"),
        ("user_address_attributes_postcode", "12345"),
        ("user_user_detail_attributes_email", "fake@htmail.com"),
        ("user_user_detail_attributes_password", "test123"),
        ("user_user_detail_attributes_password_confirmation", "test123")
    }

    for field_id, value in form_data:
        driver.find_element(By.ID, field_id).send_keys(value)
        time.sleep(1)

    driver.find_element(By.ID, "licencetype_f").click()
    time.sleep(3)

    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    success3 = driver.get_screenshot_as_file("registration_screenshot.png")
    if success3:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")

    element = driver.find_element(By.XPATH, "/html/body/div[3]/h3")
    fetched_text = element.text
    assert fetched_text == "Login", f"Expected 'Login', but got '{fetched_text}'"
    print("Test passed successfully")

def test_edit_profile():
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/insurance/v1/index.php")
    driver.maximize_window()

    email_login = "fake@htmail.com"
    password_login = "test123"

    driver.find_element(By.ID, "email").send_keys(email_login)
    driver.find_element(By.ID, "password").send_keys(password_login)
    success4 = driver.get_screenshot_as_file("login_again_screenshot.png")
    if success4:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")

    driver.find_element(By.NAME, "submit").click()

    edit_profile = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Edit Profile"))
    )
    edit_profile.click()
    time.sleep(3)

    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN).perform()

    time.sleep(3)
    form_data = {
        "user_surname": "Gonzalez",
        "user_phone": "9876543210",
        "user_address_attributes_street": "456 New St",
        "user_address_attributes_city": "Ottawa",
        "user_address_attributes_county": "Ontario",
        "user_address_attributes_postcode": "K1A 0A1",
    }

    for field_id, value in form_data.items():
        element = driver.find_element(By.ID, field_id)
        element.clear()
        element.send_keys(value)
        time.sleep(1)
    success5 = driver.get_screenshot_as_file("edition_screenshot.png")
    if success5:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")

    driver.find_element(By.NAME, "commit").click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//*[@id='tabs-5']/h1")
    fetched_text = element.text
    assert fetched_text == "Editing user profile", f"Expected 'Editing user profile', but got '{fetched_text}'"

    print("Test passed successfully")
    driver.quit()


if __name__ == "__main__":
    test_registration()
    test_edit_profile()