from .files import DriveFiles
from .login import DriveLogin
from os import mkdir
from os import path
from os import chdir
from os import getcwd
from .files import DriveFiles
from .login import DriveLogin

class Drive():
    def __init__(self, creds_path) -> None:
        self.drive_login = DriveLogin(creds_path)
        self.drive_files = DriveFiles(self.drive_login.api_login())
    
    def download_file(self,file_name, download_dir):
        if  not path.exists(download_dir):
            mkdir(download_dir)
        base_dir = getcwd()
        chdir(download_dir)
        self.drive_files.download_file(file_name)
        chdir(base_dir) 

    def upload_file(self,file_name, upload_dir):
        folder_meta = self.drive_files.get_resource_metadata(upload_dir)
        file_id = self.drive_files.upload_file(file_name, folder_meta['id'])
        return file_id
        