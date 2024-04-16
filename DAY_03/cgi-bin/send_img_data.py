### 모듈 로딩
import cgi
import datetime

# 웹 페이지의 form 태그 내의 input 태그 입력값 가져와서
# 저장하고 있는 인스턴스
form = cgi.FieldStorage()

if 'img_file' in form and 'message' in form:
    fileitems = form['img_file']     # form.getvalue(key='img_file')
    msg = form['message']           # form.getvalue(key='message')
    suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

    # 서버에 이미지 파일 저장
    img_file = fileitems.filename
    save_path = f'./image/{suffix}_{img_file}'
    with open(file=save_path, mode='wb') as f:
        f.write(fileitems.file.read())

    img_path = f'../image/{suffix}_{img_file}' 
    

# 요청에 대한 응답 HTML
print('Content-Type: text/html')    # HTML is following
print()
print('<meta charset="UTF-8">')
print('<title>CGI script output</title>')
print('<h1>This is my first CGI script</h1>')
# print(f'<h2>{form}</h2>')
print(f'<img src={img_path} width="20%" height="20%">')