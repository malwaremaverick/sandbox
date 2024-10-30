class Student:
    
    # Klassen student
    def __init__(self, first_name, last_name, age, student_id):
        
        # INIT, kjøres automatisk når vi oppretter et objekt av denne klassen
        # :param first_name: Studentens fornavn, (str)
        # :param last_name: Studentens etternavn, (str)
        # :param age: Studentens alder, (int)
        # :param student_id: Studentens student-id, (str)
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.courses = []
        
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def enroll_in_course(self, course):
        self.courses.append(course)
        
    def get_total_credits(self):
        total_credits = 0
        for course in self.courses:
            total_credits += course.credits
        return total_credits
    
class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits
        

