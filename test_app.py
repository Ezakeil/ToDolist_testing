import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class TaskManagerTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Use Remote WebDriver correctly (no desired_capabilities)
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )
        self.driver.get("http://54.152.120.95:9090/")  # Replace this with your EC2 IP

    def tearDown(self):
        self.driver.quit()

    def delete_all_tasks(self):
        while True:
            delete_links = self.driver.find_elements(By.CLASS_NAME, "delete")
            if not delete_links:
                break
            delete_links[0].click()
            time.sleep(1)

    def test_homepage_loads(self):
        self.assertIn("Task Manager", self.driver.title)

    def test_add_task(self):
        self.delete_all_tasks()
        input_box = self.driver.find_element(By.NAME, "title")
        input_box.send_keys("Test Task 1")
        input_box.submit()
        time.sleep(1)
        self.assertIn("Test Task 1", self.driver.page_source)

    def test_add_multiple_tasks(self):
        self.delete_all_tasks()
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
        self.delete_all_tasks()
        self.test_add_task()
        toggle_link = self.driver.find_element(By.CLASS_NAME, "toggle")
        toggle_link.click()
        time.sleep(1)
        self.assertIn("Done", self.driver.page_source)

    def test_toggle_task(self):
        self.delete_all_tasks()
        self.test_add_task()
        toggle_link = self.driver.find_element(By.CLASS_NAME, "toggle")
        toggle_link.click()
        time.sleep(1)
        toggle_link = self.driver.find_element(By.CLASS_NAME, "toggle")
        toggle_link.click()
        time.sleep(1)
        self.assertIn("Pending", self.driver.page_source)

    def test_delete_task(self):
        self.delete_all_tasks()
        self.test_add_task()
        delete_link = self.driver.find_element(By.CLASS_NAME, "delete")
        delete_link.click()
        time.sleep(1)
        self.assertNotIn("Test Task 1", self.driver.page_source)

    def test_empty_list(self):
        self.delete_all_tasks()
        tasks = self.driver.find_elements(By.CLASS_NAME, "task-list")
        self.assertIsNotNone(tasks)

    def test_add_empty_task(self):
        self.delete_all_tasks()
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
