import requests
import matplotlib.image as mping
import json

img = mping.imread("testImage.jpg")

client_id = "1_incDetePbACcKud1Nj"
client_secret = "19ygiH6Dp0"
# url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 닮은꼴 찾기
files = {'image': open('testImage.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code

d = json.loads(response.text)
result = d['faces'][0].get('celebrity').get('value')


if(rescode==200):
    print (result)
else:
    print("Error Code:" + rescode)

