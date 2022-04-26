
#code="http://naver.com"
code="http://youtube.com"
print(code)

my_code=code.replace("http://","")
print(my_code)

my_code=my_code[:my_code.index(".")]
print(my_code)

password = my_code[:3] + str(len(my_code)) + str(my_code.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(code, password))
