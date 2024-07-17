# # test_todo_crud.py

# import allure
# import pytest
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import Chrome

# @allure.feature('Todo CRUD Operations')
# @pytest.mark.usefixtures("init_database", "flask_server")
# class TestTodoCRUD:

#     @allure.story('Create Todo')
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_create_todo(self, driver: Chrome):
#         with allure.step('Navigate to homepage'):
#             driver.get("http://localhost:5000")
        
#         with allure.step('Enter new todo'):
#             todo_input = driver.find_element(By.NAME, "content")
#             todo_input.send_keys("New Test Todo")
#             todo_input.send_keys(Keys.RETURN)
        
#         with allure.step('Wait for new todo to appear'):
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'New Test Todo')]"))
#             )
        
#         with allure.step('Verify new todo is in the list'):
#             todos = driver.find_elements(By.XPATH, "//li")
#             assert any("New Test Todo" in todo.text for todo in todos)

#     # Add more test methods here...