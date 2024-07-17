import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from app import app, db, Todo
import threading
import time
from werkzeug.serving import make_server
from flask import Flask

# This fixture sets up the Flask app for testing
@pytest.fixture(scope="session")
def flask_app() -> Flask:
    # Configure the app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    return app

# This fixture creates a test client for the Flask app
@pytest.fixture(scope="session")
def client(flask_app: Flask):
    return flask_app.test_client()

# This class is used to run the Flask app in a separate thread
class ServerThread(threading.Thread):
    def __init__(self, app: Flask):
        threading.Thread.__init__(self)
        # Create a server instance for the Flask app
        self.srv = make_server('127.0.0.1', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        # Start the server
        self.srv.serve_forever()

    def shutdown(self):
        # Shutdown the server
        self.srv.shutdown()

# This fixture starts and stops the Flask server for the duration of the test session
@pytest.fixture(scope="session")
def flask_server(flask_app: Flask):
    server = ServerThread(flask_app)
    server.start()
    time.sleep(2)  # Give the server time to start
    yield server
    server.shutdown()

# This fixture creates a Selenium WebDriver instance for browser automation
@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run Chrome in headless mode (optional)
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--start-maximized') 
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# This fixture sets up and tears down the database for each test function
@pytest.fixture(scope="function")
def init_database(flask_app: Flask):
    with flask_app.app_context():
        db.create_all()  # Create all tables
        yield db
        db.session.remove()  # Remove the session
        db.drop_all()  # Drop all tables after the test

# This fixture creates a sample todo item for each test function
@pytest.fixture(scope="function")
def sample_todo(init_database):
    todo = Todo(content="Sample Todo")
    init_database.session.add(todo)
    init_database.session.commit()
    return todo