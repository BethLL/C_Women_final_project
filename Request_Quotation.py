from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_quotation_generation_and_saving():
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/insurance/v1/index.php")
    driver.maximize_window()

    email_login = "fake@htmail.com"
    password_login = "test123"

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
    success = driver.get_screenshot_as_file("screenshot3.png")
    if success:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")

    for field_id, value in dropdown_menu.items():
        element = driver.find_element(By.ID, field_id)
        Select(element).select_by_visible_text(value)
        time.sleep(1)

    radio_button = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='Yes']")
    radio_button.click()
    success = driver.get_screenshot_as_file("screenshot4.png")
    if success:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")

    driver.find_element(By.NAME, "submit").click()
    time.sleep(1)

    element = driver.find_element(By.XPATH, "/html/body/b[1]")
    fetched_text = element.text
    assert fetched_text == "You have saved this quotation!", f"Expected 'You have saved this quotation!', but got '{fetched_text}'"
    print("Test passed successfully")

    driver.back()
    success = driver.get_screenshot_as_file("screenshot5.png")
    if success:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")

    time.sleep(2)
# n. of quotation  41823
    driver.find_element(By.LINK_TEXT, "Retrieve Quotation").click()
    time.sleep(1)
    retrieve_quotation = driver.find_element(By.NAME, "id")
    retrieve_quotation.send_keys('41823')
    time.sleep(1)
    success = driver.get_screenshot_as_file("screenshot6.png")
    if success:
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")
    retrieve_button = driver.find_element(By.ID, "getquote")
    retrieve_button.click()
    time.sleep(2)

    quotation = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[4]/td[1]/b")
    assert quotation.is_displayed(), "Saved quotation not found in the list"

    print("Quotation saved successfully")

    driver.back()
    time.sleep(2)
    driver.quit()


