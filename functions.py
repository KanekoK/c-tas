import requests
import json
import base64
import config
from google.cloud import translate


# 画像読み込み

def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def upload_file_img():
    pass
    # the_file = request.files['the_file']
    # return the_file

def img2digit(img_file_path):
    KEY = config.API_KEY
    url = 'https://vision.googleapis.com/v1/images:annotate?key='
    api_url = url + KEY

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

def lang_translation(target_text, from_lang, to_lang):
    KEY = config.API_KEY
    url = "https://translation.googleapis.com/language/translate/v2?key="
    api_url = url + KEY
    sentence = "&q="+target_text
    langtolang = "&source="+from_lang+"&target="+to_lang
    res = requests.get(api_url+sentence+langtolang)
    res_json = res.json()
    trans_text = res_json["data"]["translations"][0]["translatedText"]
    return trans_text
