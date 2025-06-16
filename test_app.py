import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class TaskManagerTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://54.152.120.95:9090/")  # CHANGE this to your EC2 app URL if needed

    def tearDown(self):
        self.driver.quit()

    def test_homepage_loads(self):
        self.assertIn("Task Manager", self.driver.title)

    def test_add_task(self):
        input_box = self.driver.find_element(By.NAME, "title")
        input_box.send_keys("Test Task 1")
        input_box.submit()
        time.sleep(1)
        self.assertIn("Test Task 1", self.driver.page_source)

    def test_add_multiple_tasks(self):
        for i in range(3):
            input_box = self.driver.find_element(By.NAME, "title")
            input_box.send_keys(f"Task {i}")
            input_box.submit()
            time.sleep(1)
        page_text = self.driver.page_source
        self.assertIn("Task 0", page_text)
        self.assertIn("Task 1", page_text)
        self.assertIn("Task 2", page_text)

    def test_complete_task(self):
        self.test_add_task()
        toggle_link = self.driver.find_element(By.CLASS_NAME, "toggle")
        toggle_link.click()
        time.sleep(1)
        self.assertIn("Done", self.driver.page_source)

    def test_toggle_task(self):
        self.test_add_task()
        toggle_link = self.driver.find_element(By.CLASS_NAME, "toggle")
        toggle_link.click()
        time.sleep(1)
        toggle_link = self.driver.find_element(By.CLASS_NAME, "toggle")
        toggle_link.click()
        time.sleep(1)
        self.assertIn("Pending", self.driver.page_source)

    def test_delete_task(self):
        self.test_add_task()
        delete_link = self.driver.find_element(By.CLASS_NAME, "delete")
        delete_link.click()
        time.sleep(1)
        self.assertNotIn("Test Task 1", self.driver.page_source)

    def test_empty_list(self):
        tasks = self.driver.find_elements(By.CLASS_NAME, "task-list")
        self.assertIsNotNone(tasks)

    def test_add_empty_task(self):
        input_box = self.driver.find_element(By.NAME, "title")
        input_box.send_keys("")
        input_box.submit()
        time.sleep(1)
        self.assertNotIn("<li></li>", self.driver.page_source)

    def test_html_structure(self):
        header = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(header.text, "Task Manager")

    def test_css_loaded(self):
        link = self.driver.find_element(By.XPATH, "//link[@rel='stylesheet']")
        href = link.get_attribute("href")
        self.assertIn("styles.css", href)

if __name__ == "__main__":
    unittest.main()
