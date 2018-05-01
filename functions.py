import requests
import json
import base64
import config


# 画像読み込み
img_file_path = 'uploads/sample.png'

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

def korean2japanese():
    # Imports the Google Cloud client library
    from google.cloud import translate

    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = u'Hello, world!'
    # The target language
    target = 'ru'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))

korean2japanese()
