class Student:
    def __init__(self, first_name, last_name, age, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id 
        
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
        
nils_nilsen = Student("Nils", "Nilsen", 22, "IT567")
anne_gro = Student("Anne", "Gro", 78, "IT098" )

print(f"{nils_nilsen.first_name} {nils_nilsen.last_name} er {nils_nilsen.age} år gammel.")
print(f"{anne_gro.first_name} {anne_gro.last_name} er {anne_gro.age} år gammel.")

print(nils_nilsen.get_full_name())
print(anne_gro.get_full_name())
