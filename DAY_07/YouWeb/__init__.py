### 모듈 로딩
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

### DB관련 인스턴스 생성
db = SQLAlchemy()
migrate = Migrate()

### Application Create 함수
def create_app():
    # Flask Server 인스턴스 새엇ㅇ
    app = Flask(__name__)

    # 설정 내용 로딩
    # print(f'__name__ : {__name__}')
    # app.config.from_object(config)
    app.config.from_pyfile('config.py')

    # ORM 즉, DB 초기화
    db.init_app(app)
    migrate.init_app(app, db)

    # 테이블 클래스
    from . import models

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    # Flask Server 인스턴스 반환
    return app