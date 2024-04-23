### Application Factory 기반의 Flask Server 구동

## 모듈 로딩
from flask import Flask, render_template, url_for


### Application Factory 기반의 함수 정의
### 함수명 : create_app 변경 불가
### 반환값 : Flask_Server 인스턴스
def create_app():
    ## Flask Server 인스턴스 생성
    app = Flask(__name__)

    from flask import Blueprint
    from .views import data_view
    ## Blueprint 인스턴스 등록 : 서브 카테고리의 페이지 라우팅 기능
    # app.register_blueprint()

    # Blueprint 등록
    app.register_blueprint(data_view.dataBP)
    
    # 데이터 전송하는 라우팅 => 변수<타입:변수명>
    # http://127.0.0.1:5000/user/000
    

    ## Flask Server 인스턴스 반환
    return app