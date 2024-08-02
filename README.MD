# About this Project
Flask e2e testing example, from frontend inputs to database assertions. + Screenshots of results

https://realburi.github.io/flask-todo-e2e/


# Introduction
You can see the results something like this https://realburi.github.io/flask-todo-e2e/

## Prerequisites  
1. Ensure you have JDK-6 and up and $JAVA_HOME set in your %PATH% 
2. Create new python virtual environment, pc or mac

`python -m virtualenv venv` # To create the environment \
`source venv/bin/activate`&nbsp; # On Mac/Linux OS \
`venv\Scripts\activate`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# On Windows OS

3. Install the required packages by running the following command, after activating the **VENV**

`pip install -r requirements.txt`

4. Install Allure for reporting the test Results

`brew install allure`&nbsp;&nbsp;&nbsp;# for mac 

For Windows run the following command \
`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex`

`scoop install allure`

5. Finally Run the tests with the following command

`pytest --alluredir=./allure-results` \
`allure serve ./allure-results`
