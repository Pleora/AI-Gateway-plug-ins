import os
import numpy as np
import cv2
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
    
   
class UploadFileToSharePoint:
    MAIN_URL = "https://pleora589.sharepoint.com"
    SITE_URL = MAIN_URL + "/sites/Sandbox"
    USER_NAME = "??????????"
    PASSWORD  = "??????????"
    LIST_TITLE = "Documents"
    def __init__ (self, filename = None):
        self.ctx = ClientContext(self.SITE_URL).with_credentials(UserCredential(self.USER_NAME, self.PASSWORD))
        self.target_folder = self.ctx.web.lists.get_by_title(self.LIST_TITLE).root_folder
        print(self.USER_NAME)
        print(self.PASSWORD)
        print(self.SITE_URL)

    def upload_file (self, filename):
        with open(filename, 'rb') as content_file:
             file_content = content_file.read()
        name_on_SharePoint = os.path.basename(filename)
        self.target_folder.upload_file(name_on_SharePoint, file_content)
        self.ctx.execute_query()


_UploadFileToSharePoint = UploadFileToSharePoint()
path_file="/home/pleora/image/test.jpg"
_UploadFileToSharePoint.upload_file(path_file)

