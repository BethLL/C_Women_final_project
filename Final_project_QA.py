from clselenium.webdriver.common.by import By
import time


class Test_case_1:

    def test_method01(self, driver):
        driver.get("https://demo.guru99.com/test/newtours/index.php")
        register_here = driver.find_element(By.XPATH,
                                            '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a')
        register_here.click()

        time.sleep(3)
        user_name = driver.find_element(By.XPATH, "//*[@id='email']")
        user_name.send_keys('Lucia Peralta')

        time.sleep(2)
        pass_word = driver.find_element(By.XPATH,
                                        '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[14]/td[2]/input')
        pass_word.send_keys('Uli124omis')

        time.sleep(2)
        pass_word2 = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[15]/td[2]/input')
        pass_word2.send_keys('Uli124omis')
        time.sleep(3)

        submit_button = driver.find_element(By.XPATH,
                                            "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[17]/td/input")
        submit_button.click()
        time.sleep(3)
        # word_expected = driver.find_element(By.XPATH, 'L/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b').text
        # word_fetched = 'Dear'
        # assert word_expected == word_fetched, f"Test Failed: Expected '{word_expected}', but got '{word_fetched}'"

        time.sleep(2)
        signed_off_button = driver.find_element(By.XPATH,
                                                "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a")
        signed_off_button.click()
        time.sleep(2)
        # word_expected = driver.find_element(By.XPATH, 'Mercury Interactive').text
        # word_fetched = 'Mercury Interactive'
        # assert word_expected == word_fetched, f"Test Failed: Expected '{word_expected}', but got '{word_fetched}'"


        driver.close()
        print("sample test case successfully completed")
