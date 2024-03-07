import requests
import json
import io
url="https://ekasmin.atlassian.net/rest/api/3/issue/OIT-7020/attachments"
headers={
    "X-Atlassian-Token": "no-check"
}

# To attach single file
#files={
 #   "file":("Epic.pdf",open("Epic.pdf","rb"))
#}

# to attach multiple files

files = [
    ("file", ("Epic.pdf", open("Epic.pdf", "rb"))),
    ("file", ("Epic1.pdf", open("Epic1.pdf", "rb")))
]

response=requests.post(url,headers=headers,files=files,auth=("Vinod.Kotiya@sea.com","ATddddxeXMqQsiob9SCYgKA2Ps32uu-fninid1bYNCEyYkVGDumi8yeX9vNgf2DHXU7rpm2hEv-lOAjmyyDIn7hPJtDyUjPGf-V-vgiMmw1aHM=AB2BE8EA"))
print(response.text) 