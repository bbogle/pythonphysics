#-*-encoding:utf-8-*-

my_file = open("sample.txt", "r")

contents = my_file.read()
word_list = contents.split(" ")      # 빈칸 기준으로 단어를 분리 리스트
line_list = contents.split("\n")     # 한줄 씩 분리하여 리스트

print "Total Number of Characters :", len(contents)
print "Total Number of Words:", len(word_list)
print "Total Number of Lines :", len(line_list)
