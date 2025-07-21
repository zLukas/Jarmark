from  argparse import ArgumentParser
class InputParams(ArgumentParser):
    def __init__(self):
        super().__init__()
        self.add_argument('--credentials', help='credentials file to send ', required=True)
        self.add_argument('--upload', help='upload file to drive',action='store_true',  required=False)
        self.add_argument('--download', help='download file to drive',action='store_true',  required=False)
        self.add_argument('--files',  help='files names', nargs='+', required=True)
        self.add_argument('--destination', help='files destination dir ', required=True)