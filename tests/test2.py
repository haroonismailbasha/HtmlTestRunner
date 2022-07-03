import unittest
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from verify import expect

import verify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC

# from test import TestStringMethods
# from test import MoreTests as MoreTests_


class My_Tests(unittest.TestCase):

    def test_one(self):
        self.assertTrue(True)

    def test_two(self):
        self.assertTrue(False)

    def test_two_(self):
        sleep(3)
        user_name = "hel@gmail.com"
        password = "hel"
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://www.facebook.com")
        # element = driver.find_element(By.ID,"email")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "jal"))
        )
        print(verify.Falsy(element.is_displayed()))
        driver.quit()
        # element.send_keys(user_name)
        # element = driver.find_element(By.ID,"pass")
        # element.send_keys(password)
        # element.send_keys(Keys.RETURN)
        # print(verify.Greater(3, 20))
        # print(verify.Greater(3, 2))
    def test_two__(self):
        sleep(3)
        user_name = "hel@gmail.com"
        password = "hel"
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://www.facebook.com")
        element = driver.find_element(By.ID,"email")
        print(verify.Truthy(element.is_displayed()))
        driver.quit()

    # def is_awesome(value):
    #     return 'awesome' in value
    #
    # def is_more_awesome(value):
    #     return value > 'awesome'
    #
    # expect('so awesome', is_awesome, is_more_awesome)

    # def is_just_right(self,value):
    #     assert value == 'just right', 'Not just right!'
    #     try:
    #         expect('too cold', value.is_just_right)
    #     except AssertionError:
    #         raise
    #     self.assertTrue(True)


    # def test_two(self):
    #     # demonstrate that stdout is captured in passing tests
    #     print("HOLA CARACOLA")
    #     self.assertTrue(True)
    #
    # def test_three(self):
    #     self.assertTrue(True)
    #
    # def test_1(self):
    #     # demonstrate that stdout is captured in failing tests
    #     print("HELLO")
    #     self.assertTrue(False)
    #
    # def test_2(self):
    #     self.assertTrue(False)
    #
    # def test_3(self):
    #     self.assertTrue(False)
    #
    # def test_z_subs_pass(self):
    #     for i in range(2):
    #         with self.subTest(i=i):
    #             print("i = {}".format(i))  # this won't appear for now
    #             self.assertEqual(i, i)


# class MoreTests(unittest.TestCase):
#     def test_1(self):
#         print("This is different to test.MoreTests.test_1")
#         self.assertAlmostEqual(1, 1.1, delta=0.05)


if __name__ == '__main__':
    # tests = unittest.TestLoader().loadTestsFromTestCase(My_Tests)
    # # other_tests = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # more_tests = unittest.TestLoader().loadTestsFromTestCase(MoreTests)
    # # more_tests_ = unittest.TestLoader().loadTestsFromTestCase(MoreTests_)
    # # suite = unittest.TestSuite([tests, other_tests, more_tests, more_tests_])
    # suite = unittest.TestSuite([tests, more_tests])
    # HTMLTestRunner(
    #     report_title='TEST COMBINED',
    #     report_name="MyReports",
    #     add_timestamp=False,
    #     open_in_browser=True,
    #     combine_reports=True
    # ).run(suite)

    tests = unittest.TestLoader().loadTestsFromTestCase(My_Tests)
    # other_tests = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # more_tests = unittest.TestLoader().loadTestsFromTestCase(MoreTests)
    # more_tests_ = unittest.TestLoader().loadTestsFromTestCase(MoreTests_)
    # suite = unittest.TestSuite([tests, other_tests, more_tests, more_tests_])
    suite = unittest.TestSuite([tests])
    HTMLTestRunner(
        report_title='TEST SEPARATE',
        report_name="MyReports",
        open_in_browser=True,
        combine_reports=False
    ).run(suite)
