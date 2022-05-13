class exam(object):
    pass
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import pprint
address = "http://the-internet.herokuapp.com/challenging_dom"
driver_path = "D:\SE2\PracticalPart\chromedriver.exe"


class TestResults(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.wait = WebDriverWait(self.driver, 10)
        self.address = address
    
    def test_header(self):
        driver = self.driver
        elem = driver.find_element(
            By.XPATH, ('//div[@class="large-10 columns"]/table/thead/tr/th[1]').text == "Lorem" 
        )

    def test_open_page(self):
        res = self.driver.get(address)
        print("RESULT", self.driver.current_url, dir(self.driver))
        self.assertIn(self.address, self.driver.current_url)
        script = "return window.performance.getEntries();" 
        perf = self.driver.execute_script(script)
        print(perf)
        pprint.pprint(perf)
        with open(r"D:\SE2\PracticalPart\result_perf.txt", "w") as fh:
            for curr in perf:
                fh.write(f"{curr['name']}, {curr['duration']}\n")
        with open("result_perf.txt", "r") as fh:
            print(fh.read())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()