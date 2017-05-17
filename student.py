# class type, id
class Student:
    name = ""
    # department = "Physics"
    age = 18
    year = 1
    papers = []
    achievements = None  # if there is nothing reasonable

    # @staticmethod
    def print_info(self):
        print("Name: ", self.name)
        print("Department:", self.department)
        print("Year: ", self.year)
        print("Age: ", self.age)
    #
    # @staticmethod
    # def print_info(student):
    #     print("Name: ", student.name)
    #     print("Year: ", student.year)
    #     print("Age: ", student.age)
    #
    #
    # def print_papers(self):
    #     for paper in enumerate(self.papers):
    #         print("Paper %d: %s" % (idx, paper))
    #
    def __init__(self, name, department, age, year):
        self.name = name
        self.age = age
        self.department = department
        self.year = year

    # def print_info_ua(self):
    #     print("Имя: ", self.name)
    #     print("Год: ", self.year)
    #     print("Возраст: ", self.age)



