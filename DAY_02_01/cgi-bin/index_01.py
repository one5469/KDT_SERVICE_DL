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
# HTML Header
print("Content-Type: text/html")
print()
print('<form><input type="text" name="data1"><br>')
print('<input type="number" name="data2"><br>')
print('<input type="submit"></form>')

print('<form><input type="text" name="data3"><br>')
print('<input type="date" name="data4"><br>')
print('<input type="submit"></form>')

# HTML Body
print(f'Hello CGI~^^ Form : {result}')