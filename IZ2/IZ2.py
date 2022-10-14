from tkinter import Grid


class Student:
    name: str
    phone: str
    age: int
    birthday: str
    
    def print(self):
        print(self.name + " " + str(self.age) + " " + self.phone + " " + self.birthday)
    
class Group:
    students: list
    
    def __init__(self):
        self.students = []
        
    def load(self):
        file = open("IZ2/data.txt", "r")

        sourceInfo = file.read().split(sep=";")
        sourceInfo = sourceInfo[0:len(sourceInfo) - 1]
        
        for source in sourceInfo:
            info = source.split(sep=",")
            student = Student()
            student.name = info[0]
            student.phone = info[1]
            student.age = int(info[2])
            student.birthday = info[3]

            self.students.append(student)
        
        file.close()
    
    def save(self):
        file = open("IZ2/data.txt", "w")
        resultStr = ""
        for student in self.students:
            resultStr += student.name + "," + student.phone + "," + str(student.age) + "," + student.birthday + ";"
        
        file.write(resultStr)
        file.close()

group = Group()
group.load()

command = ""
command = input()

while(command != "exit"):
    match command:
        case "add":
            print("name:")
            name = input()
            print("age:")
            age = int(input())
            print("phone:")
            phone = input()
            print("birthday:")
            birthday = input()
            
            student = Student()
            student.name = name
            student.age = age
            student.phone = phone
            student.birthday = birthday
            
            group.students.append(student)
            
        case "print":
            for student in group.students:
                student.print()
                
        case "delete":
            print("name:")
            name = input()
            group.students = list(filter(lambda stud: stud.name != name, group.students))
            
        case sort if sort.split()[0] == "sort":
            component = sort.split()[2]
            match component:
                case "name":
                    group.students = sorted(group.students, key= lambda stud: stud.name)
                    
                case "age":
                    group.students = sorted(group.students, key= lambda stud: stud.age)
                    
                case "birthday":
                    group.students = sorted(group.students, key= lambda stud: stud.birthday)
                    
                case "phone":
                    group.students = sorted(group.students, key= lambda stud: stud.phone)
                    
                case _:
                    print("error.")
                    
        case find if find.split()[0] == "find":
            component = find.split()[2]
            value = find.split()[4]
            finded = []
            
            match component:
                case "name":
                    finded = list(filter(lambda stud: stud.name == value,group.students))
                    
                case "age":
                    finded = list(filter(lambda stud: stud.age == int(value),group.students))
                    
                case "birthday":
                    finded = list(filter(lambda stud: stud.birthday == int(value),group.students))
                    
                case "phone":
                    finded = list(filter(lambda stud: stud.phone == int(value),group.students))
                    
                case _:
                    finded = []
                    
            if len(finded) == 0:
                print("no finded students")
            else:
                for student in finded:
                    student.print()

        case _:
            print("error.")
            
    command = input()

group.save()
            