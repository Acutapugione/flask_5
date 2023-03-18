class Student:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
      
print(Student("Vasya", 19).__dict__)