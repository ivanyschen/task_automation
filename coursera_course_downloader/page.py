import os
from urllib import request

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locator import LoginPageLocators, CourseHomePageLocators, CourseWeeklyPageLocators, CourseVideoPageLocators
from basepage import BasePage


class LoginPage(BasePage):
    """https://www.coursera.org/?authMode=login"""
    def __init__(self, driver, page_url='https://www.coursera.org/?authMode=login'):
        BasePage.__init__(self, driver, page_url)

    def fill_up_email(self, value):
        email_element = self.find_element(*LoginPageLocators.EMAIL)
        email_element.clear()
        email_element.send_keys(value)

    def fill_up_password(self, value):
        password_element = self.find_element(*LoginPageLocators.PASSWORD)
        password_element.clear()
        password_element.send_keys(value)

    def click_login(self):
        login_button = self.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()


class CourseHomePage(BasePage):
    """For example, https://www.coursera.org/learn/neural-networks-deep-learning/lecture/Cuf2f/welcome """
    def __init__(self, driver, page_url):
        BasePage.__init__(self, driver, page_url)
        self.page_url = page_url

    def get_html(self):
        """
        :return: HTML source of the page
        """
        return self.driver.page_source.encode('utf-8').strip()

    def get_weekly_page_urls(self):
        weekly_page_urls = [button.get_attribute('href')
                            for button in self.find_elements(*CourseHomePageLocators.WEEK_BUTTON)]
        return weekly_page_urls


class CourseWeeklyPage(BasePage):
    def __init__(self, driver, page_url):
        BasePage.__init__(self, driver, page_url)

    def get_video_page_urls(self):
        video_page_urls = self.find_elements(*CourseWeeklyPageLocators.VIDEO_LIST)
        video_page_urls = [url.get_attribute('href') for url in video_page_urls]
        return video_page_urls


class CourseVideoPage(BasePage):
    def __init__(self, driver, page_url):
        BasePage.__init__(self, driver, page_url)
        self.title = page_url.split('/')[-1]

    def download_video(self, destination_directory=''):
        try:
            video_url = self.find_element(*CourseVideoPageLocators.LECTURE_VIDEO).get_attribute('href')
        except TimeoutException:
            print("Lecture video is not available for downloading")
            return

        downloadable = request.urlopen(video_url)
        with open(os.path.join(destination_directory, self.title) + '.mp4', 'wb') as new_file:
            new_file.write(downloadable.read())

        print("Lecture video have been saved to {}".format(destination_directory or 'current directory'))

    def download_slides(self, destination_directory=''):
        try:
            slides_url = self.find_element(*CourseVideoPageLocators.LECTURE_SLIDE).get_attribute('href')
        except TimeoutException:
            print("Lecture Slide is not available for downloading")
            return

        downloadable = request.urlopen(slides_url)
        with open(os.path.join(destination_directory, self.title) + '.pptx', 'wb') as new_file:
            new_file.write(downloadable.read())

        print("Lecture Slides have been saved to {}".format(destination_directory or "current dirctory"))
        return

    def download_video_notes(self, destination_directory=''):
        try:
            video_notes_url = self.find_element(*CourseVideoPageLocators.VIDEO_NOTES).get_attribute('href')
        except TimeoutException:
            print("Video Notes is not available for downloading")
            return

        downloadable = request.urlopen(video_notes_url)
        with open(os.path.join(destination_directory, self.title) + '.pdf', 'wb') as new_file:
            new_file.write(downloadable.read())

        print(" ideo Notes have been saved to {}".format(destination_directory or "current dirctory"))
        return

    def download_lecture_notes(self, destination_directory=''):
        try:
            lecture_notes_url = self.find_element(*CourseVideoPageLocators.LECTURE_NOTES).get_attribute('href')
        except TimeoutException:
            print("Lecture Notes is not available for downloading")
            return

        downloadable = request.urlopen(lecture_notes_url)
        with open(os.path.join(destination_directory, self.title) + '.pptx', 'wb') as new_file:
            new_file.write(downloadable.read())

        print("Lecture Notes have been saved to {}".format(destination_directory or "current dirctory"))
        return
