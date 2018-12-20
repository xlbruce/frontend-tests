from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    options = Options()
    options.add_argument('headless')
    context.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    
