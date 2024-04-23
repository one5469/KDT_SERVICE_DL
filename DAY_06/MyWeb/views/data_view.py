## 역할 : 데이터 저장 및 출력 관련 웹 페이지 라우팅 처리
## URL : /input
##       /input/save
##       /input/delete
##       /input/update

## 모듈 로딩
from flask import Blueprint, render_template, request

## BP 인스턴스 생성
dataBP = Blueprint('data', __name__, template_folder='templates', url_prefix='/input')

## 라우팅 함수들
@dataBP.route('/')
## http://127.0.0.1:5000/input/
def input_data():
    return render_template('input_data.html',
                            action="/input/save",
                            method="POST")

## GET방식으로 데이터 저장 처리
## 사용자의 요청 즉, request 객체에 데이터 저장되어 있음
# @dataBP.route('/save_get')
# ## http://127.0.0.1:5000/input/save_get
# def save_get_data():
#     # 요청 데이터 추출
#     req_dict = request.args.to_dict()

#     return render_template('save_data.html', value=req_dict['value'], message=req_dict['message'])

# ## POST방식으로 데이터 저장 처리
# @dataBP.route('/save_post', methods=['POST'])
# ## http://127.0.0.1:5000/input/save_post
# def save_post_data():
#     # 요청 데이터 추출
#     method = request.method
#     header = request.headers
#     args = request.args.to_dict()

#     return f"SAVE POST DATA => <br>Method : {method}<br>Headers : {header}<br>Args : {args}"

@dataBP.route('/save', methods=['GET', 'POST'])
def save_data():
    method = request.method
    if method == 'GET':
        req_dict = request.args.to_dict()
    else:
        print("POST")
        req_dict = request.form
        file = request.files['files']
        print("POST")

    file.save('MyWeb/static/img/test1.png')
            
    # return f"SAVE POST DATA => {req_dict}, {method}"
    return render_template('save_data.html', value=req_dict['value'], message=req_dict['message'], img_path='../static/img/test1.png')