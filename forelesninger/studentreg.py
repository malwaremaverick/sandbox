from forelesning2510_student import Student, Course
import course_functions as cf

nils_nilsen = Student("Nils", "Nilsen", 22, "IT678")
programmering1 = Course("Programmering 1", "ITF10219", 10)
webutvikling = Course("Webutvikling", "ITF18724", 10)
designetellerannet = Course("Design etc.", "ITF10783", 10)

nils_nilsen.enroll_in_course(programmering1)
nils_nilsen.enroll_in_course(webutvikling)
nils_nilsen.enroll_in_course(designetellerannet)

print("Med klassemetode:")
print(nils_nilsen.get_total_credits())

print("Med 'ekstern' funksjon: ")
print(cf.calculate_total_credits(nils_nilsen.courses))

all_courses = [programmering1, webutvikling, designetellerannet]
print(cf.calculate_total_credits(all_courses))

print(nils_nilsen.__init__.__doc__)

print(list.append.__doc__)
