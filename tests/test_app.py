# test_todo_crud.py

import allure
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from app import Todo

@allure.feature('Todo CRUD Operations')
@pytest.mark.usefixtures("init_database", "flask_server", "sample_todo")
class TestTodoCRUD:

    @allure.story('Create Todo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_todo(self, driver: Chrome):
        todo = "Eat Dinner"
        with allure.step('Navigate to homepage'):
            driver.get("http://localhost:5000")
        
        with allure.step('Enter new todo'):
            todo_input = driver.find_element(By.NAME, "content")
            todo_input.send_keys(todo)
            todo_input.send_keys(Keys.RETURN)
        
        with allure.step('Wait for new todo to appear'):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{todo}')]"))
            )
        
        with allure.step('Verify new todo is in the database'):
            assert Todo.query.filter(Todo.content == todo).one_or_none() != None, "Record wasn't added to database!"

        allure.attach(driver.get_screenshot_as_png(), 
                      name="create_result", 
                      attachment_type=allure.attachment_type.PNG)
        
    @allure.story('Delete Todo')
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_todo(self, driver):
        with allure.step('Navigate to homepage'):
            driver.get("http://localhost:5000")

        # Attach a screenshot to the report
        allure.attach(driver.get_screenshot_as_png(), 
                      name="before_delete_result", 
                      attachment_type=allure.attachment_type.PNG)
        
        with allure.step('Delete the first todo'):
            delete_button = driver.find_element(By.XPATH, '/html/body/div/ul/li/a')
            delete_button.click()
        
        with allure.step('Verify todo is deleted'):
            todos = driver.find_elements(By.XPATH, "//li")
            assert len(todos) == 0
        
        # Attach a screenshot to the report
        allure.attach(driver.get_screenshot_as_png(), 
                      name="delete_result", 
                      attachment_type=allure.attachment_type.PNG)