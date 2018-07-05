from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from elementium.drivers.se import SeElements
from config import log
from selenium.webdriver.common.action_chains import ActionChains


class GoogleDriveApi:
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def create_folder(self, folder_title: str):
        folder_metadata = {'title': folder_title, 'mimeType': 'application/vnd.google-apps.folder'}
        folder = self.drive.CreateFile(folder_metadata)
        folder.Upload()
        log.info('Folder_title: {}, folder_id: {}'.format(folder['title'], folder['id']))
        return folder['id']

    def create_file(self, file_title: str, folder_id: str, path_to_file:str):
        file = self.drive.CreateFile({'title': file_title, 'parents': [{'id': folder_id}]})
        file.SetContentFile(path_to_file)
        file.Upload()
        log.info('title: {}, id: {}'.format(file['title'], file['id']))
        return file['id']


class GoogleDriveUi:
    def __init__(self, driver):
        self.driver = driver
        self.se = SeElements(browser=self.driver)

    def open_home_page(self):
        self.driver.get('https://www.google.com/drive/')

    def click_go_to_google_drive_button(self):
        self.se.xpath('//a[@data-g-action="Intro"]', wait=True, ttl=5).click()

    def login(self, email, password):
        self.open_home_page()
        self.click_go_to_google_drive_button()
        self.se.find('#identifierId', wait=True, ttl=5).clear().write(email)
        self.se.find('#identifierNext', wait=True, ttl=5).click()
        self.se.find('[type="password"]', wait=True, ttl=5).clear().write(password)
        self.se.find('#passwordNext', wait=True, ttl=5).click()

    def double_click_on_file_or_folder(self, data_id):
        actionChains = ActionChains(self.driver)
        actionChains.double_click(self.driver.find_element_by_xpath('//div[@data-id="{}"]'.format(data_id))).perform()

    def find_file_or_folder(self, data_id):
        return self.se.xpath('//div[@data-id="{}"]'.format(data_id), wait=True, ttl=5)
