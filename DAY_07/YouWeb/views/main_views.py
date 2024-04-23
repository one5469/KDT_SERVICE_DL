from flask import Blueprint, render_template, request
from ..models import Question, Answer
from YouWeb import db
from datetime import datetime

## BP 인스턴스 생성
bp = Blueprint('main',
               __name__,
               template_folder='templates',
               url_prefix='/')

## 라우팅 함수들
@bp.route('/')
def insert(): 
    # 
    req_dict = {}
    method = request.method
    if method == 'GET':
        req_dict = request.args.to_dict()
    else:
        print("POST")
        req_dict = request.form
    
    if len(req_dict) > 0:
        col = Question(id=req_dict['id'], subject=req_dict['subject'],
                       content=req_dict['content'], create_date=datetime.now())
        db.session.add(col)
        db.session.commit()

    return render_template('question.html')

@bp.route('/read')
def index(): 
    # Question 테이블에 저장된 데이터 읽어서 출력
    question_list = Question.query.order_by(Question.create_date.desc())
    print(f'qeustion_list => {question_list}')
    # return f"<h3>Data : {question_list}</h3>"
    # return "<h3> HI ~^^ </h3>"
    return render_template('question_list.html', question_list=question_list)