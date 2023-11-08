import yaml, pdb
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from validate_email import validate_email
from webdriver_manager.core.utils import ChromeType

class Driver():
    def init_browser():
        browser_options = Options()
        options = ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage', '--remote-debugging-port=9000', '--disable-blink-features', '--start-maximized', '--disable-extensions', '--ignore-certificate-errors', '--disable-blink-features=AutomationControlled']
    
        for option in options:
            browser_options.add_argument(option)
    
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=browser_options)
    
    #    driver.set_window_position(0, 0)
        driver.maximize_window()
    
        return driver
    
    
    def validate_yaml():
        with open("config.yaml", 'r') as stream:
            try:
                parameters = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise exc
    
        mandatory_params = ['email', 'password']
    
        for mandatory_param in mandatory_params:
            if mandatory_param not in parameters:
                raise Exception(mandatory_param + ' is not inside the yml file!')
    
        assert validate_email(parameters['email'])
        assert len(str(parameters['password'])) > 0
    
        return parameters
