class person :
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def display(self):
        print("이름 {0}, 성별 {1}".format(self.name, self.gender))
        print("나이 {0}".format(self.age))

p1 = person("사람1", "여자", "6")
p2 = person("사람2", "남자", "7")
p2.display()