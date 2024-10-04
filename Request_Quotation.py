from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def request_quotation(driver, email_login, password_login):
    driver.get("https://demo.guru99.com/insurance/v1/index.php")
    driver.maximize_window()

    driver.find_element(By.ID, "email").send_keys(email_login)
    driver.find_element(By.ID, "password").send_keys(password_login)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@id='newquote']").click()
    time.sleep(1)

    input_field = {
        "quotation_incidents": "2",
        "quotation_vehicle_attributes_registration": "ABC123",
        "quotation_vehicle_attributes_mileage": "5000",
        "quotation_vehicle_attributes_value": "50000"
    }

    dropdown_menu = {
        "quotation_breakdowncover": "European",
        "quotation_vehicle_attributes_parkinglocation": "Public Place",
        "quotation_vehicle_attributes_policystart_1i": "2023",
        "quotation_vehicle_attributes_policystart_2i": "July",
        "quotation_vehicle_attributes_policystart_3i": "15"
    }

    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN).perform()

    for field_id, value in input_field.items():
        element = driver.find_element(By.ID, field_id)
        element.clear()
        element.send_keys(value)
        time.sleep(1)

    for field_id, value in dropdown_menu.items():
        element = driver.find_element(By.ID, field_id)
        Select(element).select_by_visible_text(value)
        time.sleep(1)

    radio_button = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='Yes']")
    radio_button.click()
    success6 = driver.get_screenshot_as_file("request_screenshot.png")
    if success6:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(1)

    element = driver.find_element(By.XPATH, "/html/body/b[1]")
    fetched_text = element.text
    assert fetched_text == "You have saved this quotation!", f"Expected 'You have saved this quotation!', but got '{fetched_text}'"
    print("Quotation request submitted successfully")

    driver.back()
    driver.save_screenshot("quotation_screenshot.png")
    time.sleep(2)


def retrieve_quotation(driver, quotation_id):
    driver.find_element(By.LINK_TEXT, "Retrieve Quotation").click()
    time.sleep(1)
    retrieve_quotation = driver.find_element(By.NAME, "id")
    retrieve_quotation.send_keys(quotation_id)
    time.sleep(1)

    retrieve_button = driver.find_element(By.ID, "getquote")
    retrieve_button.click()
    success7 = driver.get_screenshot_as_file("retrieve_quotation_screenshot.png")
    if success7:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")
    time.sleep(2)

    quotation = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[4]/td[1]/b")
    assert quotation.is_displayed(), "Saved quotation not found in the list"

    print("Quotation retrieved successfully")


def test_quotation_generation_and_retrieval():
    driver = webdriver.Chrome()
    email_login = "fake@htmail.com"
    password_login = "test123"
    quotation_id = '41823'

    try:
        request_quotation(driver, email_login, password_login)
        retrieve_quotation(driver, quotation_id)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_quotation_generation_and_retrieval()

