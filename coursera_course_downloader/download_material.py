from selenium import webdriver

from page import CourseHomePage, CourseWeeklyPage, CourseVideoPage
from utilites import login


driver = webdriver.Chrome('/Users/ivanchen/desktop/chromedriver')
try:
    login(driver, 'https://www.coursera.org/?authMode=login')
    driver.implicitly_wait(5)
    url = 'https://www.coursera.org/learn/nlp-sequence-models/home/welcome'
    home_page = CourseHomePage(driver, url)
    weekly_page_urls = home_page.get_weekly_page_urls()

    for week_num, weekly_page_url in enumerate(weekly_page_urls[0:1]):
        # if week_num == 0:
        # or week_num == 1:
            # continue
        print("processing weekly page: {}".format(week_num + 1))
        weekly_page = CourseWeeklyPage(driver, weekly_page_url)
        video_page_urls = weekly_page.get_video_page_urls()

        for video_page_url in video_page_urls:
            print("processing video page: {}".format(video_page_url))
            video_page = CourseVideoPage(driver, video_page_url)
            # video_page.download_video('videos/week{}'.format(week_num+1))
            video_page.download_slides('slides/week{}'.format(week_num+1))
            # video_page.download_video_notes('video_notes/week{}'.format(week_num+1))
            # video_page.download_lecture_notes('lecture_notes/week{}'.format(week_num+1))

    # video_page_url = 'https://www.coursera.org/learn/neural-networks-deep-learning/lecture/Z8j0R/binary-classification'
    # video_page = CourseVideoPage(driver, video_page_url)
    # video_page.download_slides('slides/week{}'.format(1))
finally:
    driver.quit()

