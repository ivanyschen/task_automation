from page import LoginPage, CourseHomePage


def login(driver,  page_url):
    login_page = LoginPage(driver, 'https://www.coursera.org/?authMode=login')
    login_page.fill_up_email('youremail@gmail.com')
    login_page.fill_up_password('yourpassword')
    login_page.click_login()
    return
