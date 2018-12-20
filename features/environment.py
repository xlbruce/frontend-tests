from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    options = Options()
    options.add_argument('headless')
    context.browser = webdriver.Chrome('env/bin/chromedriver', chrome_options=options)
    
