import yaml, pdb
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from validate_email import validate_email
from webdriver_manager.core.utils import ChromeType
from trueup_link import GHApply
from driver_chrom import Driver
from gh_ext import GHAPPLY2

if __name__ == '__main__': 
    parameters = Driver.validate_yaml()
    browser = Driver.init_browser()
    
   # # Trueup
   # bot = GHApply(parameters, browser)
   # bot.login()
   # bot.security_check()
   # bot.scan_job_list()

    # Link analysis
    gh = GHAPPLY2(parameters, browser)
    gh.gh_apply()
