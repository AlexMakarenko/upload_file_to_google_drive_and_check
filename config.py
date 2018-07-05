import sys
import os
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
platform = sys.platform

#   chromedriver settings
if platform.lower() == 'darwin':
    CHROMEDRIVER = BASE_DIR + "/chromedrivers/chromedriver_mac"
elif platform.lower() == 'linux':
    CHROMEDRIVER = BASE_DIR + "/chromedrivers/chromedriver_linux"
else:
    CHROMEDRIVER = BASE_DIR + "/chromedrivers/chromedriver.exe"

#   logging settings
log_level = logging.INFO
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=log_level)
log = logging

