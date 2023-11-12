import time, random, csv, pyautogui, pdb, traceback, sys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import date
from itertools import product
from driver_chrom import Driver

class GHApply:
    def __init__(self, parameters, driver):
        self.browser = driver
        self.email = parameters['email']
        self.password = parameters['password']

    def login(self):
        try:
            self.browser.get("https://www.trueup.io/")
            time.sleep(random.uniform(5, 10))
            self.browser.find_element_by_css_selector(".text-monospace").click()
            time.sleep(random.uniform(5, 10))
            self.browser.find_element_by_id("username").send_keys(self.email)
            self.browser.find_element_by_id("password").send_keys(self.password)
            self.browser.find_element_by_css_selector("button.c89f1057d.c08709d93.cfdf7e7ce.c948a708e.cfbc31414").click()
            time.sleep(random.uniform(10, 15))
        except TimeoutException:
            raise Exception("Could not login!")
    
    def security_check(self):
        current_url = self.browser.current_url
        page_source = self.browser.page_source

        if '/checkpoint/challenge/' in current_url or 'security check' in page_source:
            input("Please complete the security check and press enter in this console when it is done.")
            time.sleep(random.uniform(5.5, 10.5))

    def scan_job_list(self) :
        # click "my job" button
        self.browser.find_element_by_css_selector("a.nav-link").click()
        time.sleep(random.uniform(10, 15))

        rnd = 0 

        while rnd < 3 :
            self.browser.find_element_by_css_selector("div.mx-5.my-1").click()
            time.sleep(random.uniform(1, 5))
            rnd += 1
        self.collect_job_links()

    def collect_job_links(self):
        # find out all the job cards
        job_lists = self.browser.find_elements_by_tag_name("a")
        file1 = open('gh_link_collection', 'a+')
        for job in job_lists:
            try:
                link = job.get_attribute('href')
            except:
                pass
            if link and 'ref=trueup' in link and 'greenhouse' in link:
                file1.seek(0)
                if link not in file1.read():
                    file1.write(link+'\n')
        file1.close()
        self.browser.close()
        self.browser.quit()
 


