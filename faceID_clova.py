import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
import matplotlib.image as mping
img = mping.imread("testImage.jpg")

client_id = "1_incDetePbACcKud1Nj"
client_secret = "19ygiH6Dp0"
url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
# url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 닮은꼴 찾기
files = {'image': open('testImage.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)

detect_result = json.loads(response.text)
detect_result
detect_summary = detect_result['faces'][0]
x, y, w, h = detect_summary['roi'].values()
gender, gen_confidence = detect_summary['gender'].values()
emotion, emotion_confidence = detect_summary['emotion'].values()
age, age_confidence = detect_summary['age'].values()

fig,ax = plt.subplots(figsize=(10,10))
ax.imshow(img)
rect_face = patches.Rectangle((x,y),w,h,
                              linewidth=5,
                              edgecolor='r',
                              facecolor='none')
ax.add_patch(rect_face)

annotation = gender + ' : ' + str(gen_confidence) + \
                '\n' + emotion + ' : ' + str(emotion_confidence) + \
                '\n' + age + ' : ' + str(age_confidence)
plt.figtext(0.15, 0.17 , annotation, wrap=True, fontsize=17, color='white')
plt.show()