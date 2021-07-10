import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main(access_token):
    transferData = TransferData(access_token)

    file_from = input("Enter your path of file : ")
    file_to = input("Enter the path to upload the file : ")

    transferData.upload_file(file_from, file_to)
    print('file has been moved !')

main('sl.AxDQQogL15IjnSWiIiUEe7GIioTh-RGLmYY1QUVz1l6SwM9LRxplWOTDLvQ1MD1JAUA_7Q3j6vvQd_aRYrYADxD58rAWrMMsx1t5q35Ra0jn0haH5doXjNzimIBoq53HC-VJXn4')