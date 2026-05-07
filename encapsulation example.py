class Student:
    def __init__(self,name,rollno, marks):
        self.__name=name
        self.__rollno=rollno
        self.__marks=marks
    def get_name(self):
        print(self.__name)
    def get_rollno(self):
        print(self.__rollno)
    def get_marks(self):
        print(self.__marks)
    def set_name(self,newname):
        if(newname!=""):
            self.__name=newname
            print( self.__name)
        else:
            print("Enter a vaid name")
    def set_rollno(self,newrollno):
        if(newrollno>=1 and newrollno<=100):
            self.__rollno=newrollno
            print(self.__rollno)
        else:
            print("Rollno has to be between 1&100 only")
    def set_marks(self,newmarks):
        if(newmarks>=0):
            self.__marks=newmarks
            print(self.__marks)
        else:
            print("Marks cannot be negative")
stu1=Student("Asrith",-12,77)
stu1.set_rollno(12)
