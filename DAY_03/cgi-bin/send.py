### 모듈 로딩
import cgi

# 웹 페이지의 form 태그 내의 input 태그 입력값 가져와서
# 저장하고 있는 인스턴스
form = cgi.FieldStorage()

if 'img_file' in form and 'message' in form:
    filename = form['img_file']     # form.getvalue(key='img_file')
    msg = form['message']           # form.getvalue(key='message')
    

# 요청에 대한 응답 HTML
print('Content-Type: text/html')    # HTML is following
print()
print('<meta charset="UTF-8">')
print('<title>CGI script output</title>')
print('<h1>This is my first CGI script</h1>')
print(f'<h2>{form}</h2>')
# print(f'<img src={filename}>')