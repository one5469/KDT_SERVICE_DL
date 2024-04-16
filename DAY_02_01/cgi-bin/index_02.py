### ==> 모듈 로딩
import cgi

### ==> Client 요청 데이터 즉, Form 데이터 저장 인스턴스
form = cgi.FieldStorage()

### ==> 데이터 추출
if 'data1' in form and 'data2' in form:
    result = form.getvalue(key='data1') + ' - ' + form.getvalue(key='data2')
else:
    result = 'No Data'

### ==> Web 브라우저 화면 출력 코드
# HTML 파일 읽기 -> body 문자열
filename = './test.html'
with open(filename, 'r', encoding='utf-8') as f:
    # HTML Header
    print("Content-Type: text/html")
    print()

    # HTML Body
    print(f.read().format(result))