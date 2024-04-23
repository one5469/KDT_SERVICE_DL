### Application Factory 기반의 Flask Server 구동

## 모듈 로딩
from flask import Flask, render_template, url_for

### Application Factory 기반의 함수 정의
### 함수명 : create_app 변경 불가
### 반환값 : Flask_Server 인스턴스
def create_app():
    ## Flask Server 인스턴스 생성
    app = Flask(__name__)

    ## Blueprint 인스턴스 등록 : 서브 카테고리의 페이지 라우팅 기능
    # app.register_blueprint()
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # 데이터 전송하는 라우팅 => 변수<타입:변수명>
    # http://127.0.0.1:5000/user/000
    @app.route('/user/<name>')
    def user_info(name):
        # return f'<h1>HELLO~^^{name}</h1>'
        return render_template('index.html', name=name)
    
    # 테스트 기능
    with app.test_request_context():
        print(url_for(endpoint='static', filename='css/style_1.css'))

    ## Flask Server 인스턴스 반환
    return app