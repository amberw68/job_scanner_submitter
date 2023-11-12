import time, random, csv, pyautogui, pdb, traceback, sys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import date
from itertools import product
from driver_chrom import Driver

class GHAPPLY2:
    def __init__(self, parameters, driver):
        self.browser = driver
        self.email = parameters['email']
        self.first_name = parameters['first_name']
        self.last_name = parameters['last_name']
        self.phone = parameters['phone']
        self.resume_dir = parameters['uploads']['resume']
        self.school = parameters['school']
        self.degree = parameters['degree']
        self.discipline = parameters['discipline']
        self.address = parameters['address']
        self.apt = parameters['apt']
        self.city = parameters['city']
        self.state = parameters['state']
        self.zip = parameters['zip']
        self.linkedin = parameters['linkedin']
        self.hear = parameters['hear']
        self.lawful = parameters['lawful']
        self.location = parameters['location']
        self.highest_edu = parameters['edu']
        self.cloud = parameters['cloud']
        self.golang = parameters['golang']
        self.kubernetes = parameters['kubernets']
        self.gender = parameters['gender']
        self.latino = parameters['latino']
        self.veteran = parameters['veteran']
        self.disability = parameters['disability']
    def gh_apply(self) :
        link_ls = list()
        with open('./gh_link_collection') as file1:
            for line in file1:
                link_ls.append(line)
        for i in link_ls:
            self.browser.get(i)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('first_name').send_keys(self.first_name)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('last_name').send_keys(self.last_name)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('email').send_keys(self.email)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('phone').send_keys(self.phone)
            time.sleep(random.uniform(3,6))
            # upload resume & cover letter
            file_upload_elements = (By.CSS_SELECTOR, "input[name='file']")
            try:
                input_buttons = self.browser.find_elements(file_upload_elements[0], file_upload_elements[1])
                for upload_button in input_buttons:
                    upload_button.send_keys(self.resume_dir)
            except:
                print ("BAD")
            time.sleep(random.uniform(3,6))
            # continue filling forms
            self.browser.find_element_by_id('education_school_name_0').send_keys(self.highest_edu)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('s2id_autogen11_search').send_keys(self.degree)
            time.sleep(random.uniform(3,6))
            #self.browser.find_element_by_id('education_discipline_0').send_keys(self.discipline)
            #time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('job_application_answers_attributes_0_text_value').send_keys(self.address)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('job_application_answers_attributes_1_text_value').send_keys(self.apt)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('job_application_answers_attributes_2_text_value').send_keys(self.city)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-drop-mask').send_keys(self.state)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('job_application_answers_attributes_4_text_value').send_keys(self.zip)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('job_application_answers_attributes_5_text_value').send_keys(self.linkedin)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('s2id_autogen2').send_keys(self.hear)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-3').send_keys(self.lawful)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-4').send_keys(self.location)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-5').send_keys(self.edu)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-6').send_keys(self.cloud)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-7').send_keys(self.golang)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-8').send_keys(self.kubernetes)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-9').send_keys(self.gender)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-10').send_keys(self.latino)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-12').send_keys(self.veteran)
            time.sleep(random.uniform(3,6))
            self.browser.find_element_by_id('select2-chosen-13').send_keys(self.disability)
            time.sleep(random.uniform(3,6))

            



            #self.browser.find_element_by_css_selector('button.unstyled-button.link-button').click()
           # time.sleep(random.uniform(50, 100))
           # self.browser.close()
           # self.browser.quit()

