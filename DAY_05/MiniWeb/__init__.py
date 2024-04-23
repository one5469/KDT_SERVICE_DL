### 모듈 로딩
from flask import Flask, render_template, Blueprint

### 애플리케이션 팩토리 함수
def create_app():
    myapp=Flask(__name__)

    # bp등록
    from .views import main_views
    myapp.register_blueprint(main_views.bp)
    
    return myapp

# ### 전역변수
# myapp = Flask(__name__)

# ### 사용자 요청 URL 처리 기능 => 라우팅(Routing)
# ### 형식 : @Flask_instance_name.route(URL문자열)

# ### 웹 서버의 첫 페이지 : htt://127.0.0.1:5000/
# # @myapp.route('/')
# # def index_page():
# #     return "<h3><font color='red'>My Web Index Page</font></h3>"

# ### 사용자마다 페이지 반환
# ### 사용자 페이지 URL : http://127.0.0.1:5000/<username>
# @myapp.route('/<user_name>')
# def username(user_name):
#     return f'username : {user_name}'

# @myapp.route('/<int:number>')
# def show_number(number):
#     return f'Number : {number}'

# @myapp.route('/hello')
# def hello():
#     return 'hello'

# @myapp.route('/')
# def index_page():
#     return render_template(template_name_or_list='tem.html')

# ### 실행 제어
# if __name__ == '__main__':
#     # Flask 웹 서버 구동
    
#     myapp.run()