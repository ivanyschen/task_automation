from selenium.webdriver.common.by import By
# Generally Speaking, locators  are abstract way of defining "how" an element will be found


class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    EMAIL = (By.ID, 'emailInput-input')
    PASSWORD = (By.ID, 'passwordInput-input')
    LOGIN_BUTTON = (By.XPATH,
                    '//*[@id="authentication-box-content"]/div/div[1]/div[2]/div/div[1]/form/div[1]/button')


class CourseHomePageLocators(object):
    WEEK_BUTTON = (By.XPATH, "//div[@class='rc-NavigationDrawer']/a")


class CourseWeeklyPageLocators(object):
    VIDEO_LIST = (By.CSS_SELECTOR, '.rc-ItemLink.nostyle')


class CourseVideoPageLocators(object):
    LECTURE_VIDEO = (By.XPATH, "//*[@class='rc-LectureDownloadItem resource-list-item']/a")
    LECTURE_SLIDE = (By.XPATH, "//*[@class='rc-AssetDownloadItem resource-list-item']/a[@download='Powerpoint Slides']")
    LECTURE_NOTES = (By.XPATH, "//*[@class='rc-AssetDownloadItem resource-list-item']/a[@download='Lecture Notes']")
    VIDEO_NOTES = (By.XPATH, "//*[@class='rc-AssetDownloadItem resource-list-item']/a[@download='Video Notes']")

