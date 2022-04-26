cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5])
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False