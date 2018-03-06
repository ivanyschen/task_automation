from page import LoginPage, CourseHomePage


def login(driver,  page_url):
    login_page = LoginPage(driver, 'https://www.coursera.org/?authMode=login')
    login_page.fill_up_email('ujhuyz0110@gmail.com')
    login_page.fill_up_password('Yushuo1992')
    login_page.click_login()
    return
