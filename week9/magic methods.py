class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}"

b = Book("1984", "Harry")


class Math:
    def add(x,y):
        return x+y
print(Math.add(67,34))

class Student:
    uni_name = "Solent Uni"

    @classmethod
    def get_name(cls):
        return cls.uni_name
print(Student.get_name())
