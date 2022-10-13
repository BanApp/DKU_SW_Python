class Student:
    def __init__(self,name,grade,number):
        self.name = name
        self.grade = grade
        self.number = number
    def __repr__(self):
        return repr((self.name, self.grade, self.number))

students = [Student('홍길동',3.9,20200303),
    Student('김철수',3.0,20200302),
    Student('최자영',4.3,20200301),
    Student('박소현',4.5,20200304),
    Student('김기수',4.5,20200305)]

print(sorted(students,key=lambda x:x.grade))