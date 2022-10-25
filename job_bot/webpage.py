from  bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from time import sleep
from userDetails import EMAIL, PASSWORD

class webpage:

    def __init__(self):
        options = Options()
        options.add_argument("window-size=1600,800")
        
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver_newer', chrome_options=options)
        self.wp = 'https:/ie.indeed.com/'
        self.EMAIL = EMAIL
        self.PASSWORD = PASSWORD
        
    
 

    def get_website(self): 
        self.driver.get(self.wp)
        sleep(5)
        self.click_sign_in()


    def login_facebook(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]').click()


        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input').send_keys('')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input').send_keys('')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input').click()

        sleep(7)
        old_window = self.driver.window_handles[0]
        self.driver.switch_to.window(old_window)

       
    def choose_facebook(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/div[2]/div/div[3]/div[3]/button').click()
        sleep(4)
        login_window = self.driver.window_handles[1]
        self.driver.switch_to.window(login_window)
        self.login_facebook()






    def click_sign_in(self):
        #click login button
        sleep(5)
        xpath_sign_button = '/html/body/div[1]/div[1]/nav/div/div/div[2]/div[2]/div[2]/a'
        button = self.driver.find_element_by_xpath(xpath_sign_button)
        button.click()
        sleep(7)
        self.choose_facebook()



    def switch_to_job_application_page(self):
        page = self.driver.window_handles[1]
        self.driver.switch_to.window(page)

    def switch_to_job_results_page(self):
        page = self.driver.window_handles[0]
        self.driver.switch_to.window(page)

    def click_second_continue(self) :   
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button').click()

    def search(self, keyword):
        sleep(7)
        try:
            search_bar = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/span/div[4]/div[2]/div/div/div/div/form/div/div[1]/div/div[1]/div/div[2]/input').send_keys(keyword)
            find_job_button = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/span/div[4]/div[2]/div/div/div/div/form/button').click()

        except :
            print('[*] search_bar element doesnt exist trying the other')
        
            try:
                search_bar = self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[1]/form/div/div[1]/div/div[1]/div/div[2]/input').click()
                search_bar.clear()
                search_bar.send_keys(keyword)
                find_job_button = self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[1]/form/button').click()

            except :
                print('[*] search_bar element doesnt exist - aborting')
                self.driver.quit()


    def reject_all(self):
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[2]').click()
    def click_on_apply(self):
        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div[5]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[3]/div/div[2]/div/div/span/div[2]/button').click()
        

    def user_has_applied_to_job(self):
        self.switch_to_job_application_page()
        sleep(5)
        if self.driver.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/h1'):
            return True
        return False
    

    def check_for_name(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/span/input')
            return True
        except NoSuchElementException:
            return False


    def contact_info_continue(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button').click()


    def resume_continue(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button').click()

    def work_exp_continue(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button').click()

    def review_continue(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button').click()

    def valid_apply(self):
        sleep(5)
        try:
            apply_btn_text = self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div[5]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[3]/div/div[2]/div/div/span/div[2]/button/div/span').text
        except:

            return False

        if apply_btn_text.lower() == 'apply now':
            return True

        return False


    def sort_by_date(self):
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[3]/div/div/div[1]/span[2]/a').click()
        sleep(4)

    def click_next_button(self):
        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div[5]/div[1]/nav/div[6]/a').click()
        sleep(4)

    def find_jobs(self):
        job_on_pages = self.driver.find_elements_by_class_name('cardOutline')
        for job in job_on_pages:
            sleep(5)
            try:
                job.click()
            except:
                print('[*] Error')
                while True:
                    continue
            sleep(3)
            if self.valid_apply():
                sleep(3)
                self.click_on_apply()
                sleep(3)
                self.switch_to_job_application_page()
                sleep(5)
        
                if self.driver.current_url.split('/')[-1] == 'contact-info':
                    self.contact_info_continue()
                sleep(2)
                if self.driver.current_url.split('/')[-1] == 'resume':
                    self.resume_continue()
                sleep(2)
                if self.driver.current_url.split('/')[-1] == 'work-experience':
                    self.work_exp_continue()
                sleep(2)
                if self.driver.current_url.split('/')[-2] == 'questions':
                    self.driver.close()
                    self.switch_to_job_results_page()
                    sleep(3)
                    continue
                sleep(2)
                if self.driver.current_url.split('/')[-1] == 'review':
                    self.review_continue()
                self.driver.close()
                self.switch_to_job_results_page()
                sleep(3)

