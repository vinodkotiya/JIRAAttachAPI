import requests
import json
import io
import os
import csv

# Function to read the CSV file and store folder and issue data in a dictionary
def read_csv_to_dict(csv_file):
    folder_issue_dict = {}
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        
        # Print column headers
        print("CSV File Columns:", csv_reader.fieldnames)
        
        # Print first few rows of data
        print("First few rows of data:")
        for i, row in enumerate(csv_reader):
            if i < 5:  # Print first 5 rows
                print(row)
            folder = row['Folder']
            issue = row['Issue']
            folder_issue_dict[folder] = issue
    return folder_issue_dict

# Path to your CSV file
csv_file_path =  r"C:\ekasmin\JIRA API Push Attachment\mapping.csv"

# Read CSV file and store data in a dictionary
folder_issue_dict = read_csv_to_dict(csv_file_path)


folder_path = r"C:\ekasmin\JIRA API Push Attachment\upload"

headers={
     "X-Atlassian-Token": "no-check"
 }
   

def list_files_in_folders(folder_path):
    for root, dirs, files in os.walk(folder_path):
        try:
            folder_name = os.path.basename(root)
            print(f"Folder Path: {root}")
            print(f"Folder: {folder_name}")
            issue = folder_issue_dict[folder_name]
            print(issue)
            url="https://ekasmin.atlassian.net/rest/api/3/issue/"+ issue +"/attachments"
            attach = []

            # Assuming files is a list of file names
            for file_name in files:
               myFile = os.path.join(root, file_name)
               file_tuple = ("file", (file_name, open(myFile, "rb")))
               attach.append(file_tuple)
            response=requests.post(url,headers=headers,files=attach,auth=("Vinod.Kotiya@sea.com","JIRAAPIKey"))
            print(response.text) 
        except Exception as e:
            print(f"Skip to next for Error: {str(e)}")
            continue

list_files_in_folders(folder_path)



# url="https://ekasmin.atlassian.net/rest/api/3/issue/OIT-6940/attachments"
# headers={
#     "X-Atlassian-Token": "no-check"
# }
 # To attach single file
#attach={
 #  "file":("Epic.pdf",open("Epic.pdf","rb"))
#}

# to attach multiple files

#files = [
 #   ("file", ("Epic.pdf", open("Epic.pdf", "rb"))),
  #  ("file", ("Epic1.pdf", open("Epic1.pdf", "rb")))
#]
# response=requests.post(url,headers=headers,files=files,auth=("Vinod.Kotiya@om","ATATT3xFfSgAgxZmVqqRb1PFasFhm3xeXMqQsiob9SCYgKA2Ps32uu-fninid1bYNCEyYkVGDumi8yeX9vNgf2DHXU7rpm2hEv-lOAjmyyDIn7hPJtDyUjPGf-V-vgiMmw1aHM=AB2BE8EA"))
# print(response.text) 