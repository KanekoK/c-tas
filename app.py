import requests
import json
import base64
import config

KEY = config.API_KEY
url = 'https://vision.googleapis.com/v1/images:annotate?key='
api_url = url + KEY



# 画像読み込み
img_file_path = 'uploads/sample.png'


def upload_file_img():
    pass
    # the_file = request.files['the_file']
    # return the_file

def img2digit(img_file_path):
    # ヘッダー情報
    headers = {'Content-Type': 'application/json'}
    img = open(img_file_path, 'rb')
    img_byte = img.read()
    img_content = base64.b64encode(img_byte).decode('utf-8')

    # print(type(img_content))

    # リクエストBody作成
    # featuresのtypeが「TEXT_DETECTION」で文字認識
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': img_content
            },
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 10,
            }]
        }]
    })
    # リクエスト発行
    res = requests.post(api_url, data=req_body)

    # リクエストから画像情報取得
    res_json = res.json()
    text = res_json['responses'][0]['fullTextAnnotation']['text']
    return text

print(upload_file_img())
# print(img2digit(img_file_path))

