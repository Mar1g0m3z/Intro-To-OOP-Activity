# add your Student class here!
class Student:
    def __init__(self, name, grade, class_list):
        self.name = name
        self.grade = grade
        self.class_list = class_list

    def add_class(self, new_class):
        self.new_class = new_class
        self.class_list.append(new_class)
        return self.class_list

    def get_num_classes(self):
        return len(self.class_list)

    def summary(self):
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes."

