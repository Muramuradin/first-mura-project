# def std_weight(height, gender):
#     if gender == "남자" :
#         weight = height * height *22/10000
#         print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
#     elif gender == "여자" :
#         weight = height * height *21/10000
#         print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# std_weight(175,"남자")    

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else :
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))

