from googleApi import Drive
from input import  InputParams

def main():
    input_params  = InputParams()
    args = input_params.parse_args()
    drive = Drive(args.credentials)
    if args.download:
        for file in args.files:
            drive.download_file(file, args.destination)
            print(f"file {file} downloaded to {args.destination} folder")
    else:
        for file in args.files:
            file_id = drive.upload_file(file, args.destination)
            print(f"uploaded file id: {file_id}")

if __name__ == '__main__':
    main()
