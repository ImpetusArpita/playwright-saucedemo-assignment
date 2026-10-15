import shutil
import allure
import pytest
from playwright.sync_api import sync_playwright
import config
from pages.login_page import LoginPage

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
   outcome = yield
   report = outcome.get_result()
   if report.when == "call":
       item.test_failed = report.failed

@pytest.fixture
def page(request):
   video_folder = config.VIDEO_FOLDER + "/" + request.node.name
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=config.HEADLESS)
       context = browser.new_context(record_video_dir=video_folder)
       page = context.new_page()
       yield page
   
       failed = getattr(request.node, "test_failed", True)
       if failed:
           screenshot = page.screenshot(full_page=True)
           allure.attach(screenshot, name="screenshot_on_failure",
                         attachment_type=allure.attachment_type.PNG)
       video_path = page.video.path()
    
       context.close()
       browser.close()
       if failed:
           allure.attach.file(video_path, name="video_on_failure",
                              attachment_type=allure.attachment_type.WEBM)
           print("Test failed, video saved at: " + video_path)
       else:
         
           shutil.rmtree(video_folder, ignore_errors=True)

@pytest.fixture
def logged_in_page(page):
   login_page = LoginPage(page)
   login_page.open()
   login_page.login(config.USERNAME, config.PASSWORD)
   return page