#-*-encoding:utf-8-*-

my_file = open("sample.txt", "r")       # 파일 열기
contents = my_file.read()               # 파일 전체 읽기
print type(contents), contents          # 전체 값 출력, 출력형태는 string

my_file.seek(0)                         # 파일 처음으로 돌아가기
content_list = my_file.readlines()      # 파일 전체를 list로 반환
print type(content_list), content_list  # 리스트값 출력

i = 0
my_file.seek(0)                         # 파일 처음으로 돌아가기
while 1:
    line = my_file.readline()
    if not line: break
    print str(i) + " === " + line,      # 한줄씩 값 출력 
    i = i + 1
