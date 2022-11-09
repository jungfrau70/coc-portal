import os
import time
import traceback
import pandas as pd
import requests
from pandas_ods_reader import read_ods

topicL = [ 
    ("regularcheck", "정기점검"),
    ("license", "데이터베이스"),
    ("incident", "인시던트"),
    ("issue", "이슈"),
    ("problem", "장애"),
    ("change", "변경"),
    ("request", "요청"),
    ("database", "DB"),
    ("kubernetes", "k8s"),
    ("instance", "VM"),
    ("capacity", "용량"),
    ("backup", "백업"),
    ("security", "보안"),
    ("discussion", "논의점") ]

   
class FileModified():
    def __init__(self, file_path, callback):
        self.file_path = file_path
        self.ods_files = [i for i in os.listdir(file_path) if i.endswith('.ods')]
        self.callback = callback
        self.modifiedOn = os.path.getmtime(file_path)
        self.lastest_files = self.ods_files 
            
    def start(self):
        while (True):
            time.sleep(0.5)
            modified = os.path.getmtime(self.file_path)
            current_ods_files = [i for i in os.listdir(file_path) if i.endswith('.ods')]
            try:
                if modified != self.modifiedOn:
                    self.modifiedOn = modified
                    new_ods_files = list(set(current_ods_files) - set(self.lastest_files))
                    for ods_file in new_ods_files:                    
                        uploadFile(ods_file)
                    self.lastest_files = current_ods_files
                    if self.callback():
                        break
            except Exception as e:
                print(traceback.format_exc())

def uploadFile(ods_file):

    # for ods_file in difference:

    filename = path+"//"+ods_file.split('.')[0]
    df = read_ods(f"{filename}.ods", headers=True)
    df.to_csv(f"{filename}.csv", encoding='utf-8-sig')
    csv_file = filename + ".csv"

    for ( topic, value ) in topicL:
        if value in csv_file:
            try:
                url = f"http://localhost:8000/{topic}/uploadfile"
                data = {'dir':path, 'submit':'Submit'}     
                with open(csv_file, 'rb') as f:
                    files = {'file':(csv_file, f, 'text/csv')}
                    r = requests.post(url, data=data, files=files)

                print(r.content)

            except Exception as e:
                print(e)

def file_modified():
    print("File Modified!")
    return False

if __name__ == "__main__":
    path = "c://Data//10월"
    file_path = path
    fileModifiedHandler = FileModified(file_path,file_modified)
    fileModifiedHandler.start()
