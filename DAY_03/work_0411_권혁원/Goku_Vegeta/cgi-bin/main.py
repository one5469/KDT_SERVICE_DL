### ==> 모듈 로딩
import cgi, os
import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from PIL import Image, ImageFile
from torchvision import transforms
from torchvision.datasets import ImageFolder
from model_class import CNNmodel

### ==> Client 요청 데이터 즉, Form 데이터 저장 인스턴스
form = cgi.FieldStorage()

### ==> 트랜스포머 정의
transformer = transforms.Compose(transforms=
                                 [transforms.ToTensor(),
                                  transforms.Resize(size=[96,96])
                                  ])

### ==> 모델 로딩
model_name = '/Goku_Vegeta_36'
pklfile = os.path.dirname(__file__) + model_name
model = torch.load(pklfile)

### ==> 이미지가 잘렸을 때 발생하는 에러 방지
ImageFile.LOAD_TRUNCATED_IMAGES = True

try:
    ### ==> 이미지 추출 및 텐서화
    img_name = form['img'].filename
    img_file = form['img'].file
    save_path = f'./img/{img_name}'
    with open(file=save_path, mode='wb') as f:
        f.write(img_file.read())

    img = Image.open(save_path)
    imgTS = transformer(img)

    ### ==> 모델 예측
    pre = model(imgTS)
    if pre[0] > 0.5:
        result = '베지터'
    else:
        result = '손오공'
except Exception as e:
    # print('error')
    result = e

### ==> Web 브라우저 화면 출력 코드
# HTML 파일 읽기 -> body 문자열
if 'img' in form:
    filename = './result_page.html'
else:
    filename = './main_page.html'
with open(filename, 'r', encoding='utf-8') as f:
    # HTML Header
    print("Content-Type: text/html")
    print()

    # HTML Body
    print(f.read().format(result))
    # print(f.read())
    # print(form)
    print()
    # try:
    #     print(form['img'])
    # except KeyError as e:
    #     print(e)