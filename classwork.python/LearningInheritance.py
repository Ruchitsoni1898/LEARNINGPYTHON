class parent():
    def student_name(self):
        print("my name is ruchit")

class student(parent):
    def get_roll_no(self):
        print("Student Roll no is 2")

object = student()
object.student_name()
object.get_roll_no()

