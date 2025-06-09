from playwright.sync_api import sync_playwright
from utils.logger import *
import allure 
from allure_commons.types import AttachmentType
import time 

# def wait_for_file_release(file_path, timeout=10):
#     """Wait until the file is no longer used by another process."""
#     start_time = time.time()
#     while True:
#         try:
#             with open(file_path, 'a'):
#                 return True
#         except PermissionError:
#             if time.time() - start_time > timeout:
#                 raise TimeoutError(f"Timed out waiting for file: {file_path}")
#             time.sleep(0.5)

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True, args=['--start-maximized'], slow_mo=200)
    context.ctx = context.browser.new_context(no_viewport=True, record_video_dir='reports/videos/', ignore_https_errors=True)
    # context.page = context.ctx.new_page()

def before_scenario(context, scenario):
    logger_setup(scenario.name)
    context.page = context.ctx.new_page()
    context.page.goto('https://www.saucedemo.com/')

def after_scenario(context, scenario):
    log_message('info', f'Closing the page for scenario {scenario.name}')
    video_file =  (context.page.video.path()) if context.page.video else None
    # print(video_file)
    screenshoot_path=f'reports/screenshots/{'_'.join((scenario.name).split('--')[0].split(' '))}_{datetime.now().strftime("%Y%m%d%H%M%S")}.png'
    context.page.screenshot(path=screenshoot_path)
    log_message('info', 'Screenshot is saved at desired location ....')

    with open(screenshoot_path, 'rb') as f:
        allure.attach(f.read(), name='Screenshot', attachment_type=AttachmentType.PNG)


        # wait_for_file_release(video_file)
        # if video_file:
        #     dest_path = f'reports\\videos\\failed_{datetime.now().strftime("%Y%m%d%H%M%S")}_{os.path.basename(video_file)}'
        #     os.rename(video_file, dest_path)
        #     log_message('info', f'Video saved at: {dest_path}')

    if scenario.status == 'failed':
        log_message('error', f'{scenario.name} failed')

    #     with open(video_file, 'rb') as file:
    #         allure.attach(file.read(), name='Video', attachment_type=AttachmentType.MP4)
    # else:
    #     if video_file and os.path.exists(video_file):
    #         os.remove(video_file)
    #         log_message('info', 'Video file removed')

    context.page.close()

def after_all(context):
    log_message('info', 'Closing browser and context')
    context.ctx.close()
    context.browser.close()
    context.playwright.stop()
