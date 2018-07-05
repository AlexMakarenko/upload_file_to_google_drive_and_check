#   An example how to:
*   ##create folder and upload file to the google drive via API and Python
*   ##check that folder created and file uploaded via UI with Selenium and Python

To run the code you need to install all dependencies from requirement.txt: 
```
pip install -r requirements.txt
```
In the `tests.test_google_drive.py` edit constants and enter real `GOOGLE_EMAIL` and `PASSWORD`.

Then you can run the test using pytest:
```
pytest tests
```

*NOTE:* The test will request access to your google drive to create a folder and a file via API. 
