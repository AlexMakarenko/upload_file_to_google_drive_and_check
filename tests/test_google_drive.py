from config import BASE_DIR
from helpers.google_drive_helper import GoogleDriveApi, GoogleDriveUi

#   google account credentials
GOOGLE_EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'
PATH_TO_FILE = '{}/test_data/HelloWorld.txt'.format(BASE_DIR)


def test_google_drive(driver):
    drive_api = GoogleDriveApi()
    folder_id = drive_api.create_folder('MyFolder')
    file_id = drive_api.create_file('HelloWorld.txt', folder_id, PATH_TO_FILE)
    drive_ui = GoogleDriveUi(driver)
    drive_ui.login(GOOGLE_EMAIL, PASSWORD)
    assert drive_ui.find_file_or_folder(folder_id), 'Folder was not created.'
    drive_ui.double_click_on_file_or_folder(folder_id)
    assert drive_ui.find_file_or_folder(file_id), 'File was not uploaded.'
