from io import FileIO
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
class DriveFiles:
    def __init__(self, service = None):
        self.__service = service

    def get_resource_metadata(self, name):
        '''
            Description: find specific resource in google drive,  by name ( file and folder)
            params: resource name
            return: dict, keys = ["id", "kind", "name", "parents field"]
        '''
        search_filter = "name="+ "'" + name + "'"
        files_service = self.__service.files()
        list_service  = files_service.list(q = search_filter,
                                           pageSize=1, 
                                           # all possible fields here:
                                           #https://developers.google.com/drive/api/v3/reference/files
                                           fields="nextPageToken, files(kind, id, name, parents)")
        search_list =list_service.execute()
        if len(search_list['files']) == 0:
            return None
        else:

            return dict(search_list['files'][0])


    def download_file(self, file_name):
        '''
            Description: download a file from google drive
            params: file_name - name of the file to download
            return: None
        '''

        file_meta = self.get_resource_metadata(file_name)
        # none type exception
        if file_meta:
            request = self.__service.files().get_media(fileId=file_meta['id'])
            fh = FileIO(file_name, 'wb')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print (f"Download {int(status.progress() * 100)}.")
        else:
            print(f"{file_name} not found in drive")


    #TODO: handle the case when file already exist
    def upload_file(self, file_name, parent_folder_id):
        '''
            Description: upload a file from local to google drive
            params: file_name - name of the file to update
                    parent_folder_id - drive id of folder in which file will be uploaded
            return: new_file_id['id'] - new file drive id
        '''
        file_metadata = {'name': file_name,
                         'parents': [parent_folder_id]}
        media = MediaFileUpload(file_name, mimetype='text/plain')

        files_service = self.__service.files()
        create_service = files_service.create(body=file_metadata, media_body=media)
        create_service.execute()
        new_file_id =self.get_resource_metadata(file_name)     
        return new_file_id['id']


    def create_folder(self, folder_name):
        # TBD
        if self.__service:
            folder_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            files_service = self.__service.files()
            create_service =  files_service.create(body=folder_metadata,fields='id')
            folder_id = create_service.execute()
            return folder_id
        else:
            return "error: no service provided"
