'''
# 1
Given two integer variables, a and x (where a is 10 and x is 2), write a single
expression that adds 1 to a, and then multiplies the resulting value by x.
Print out the result of your evaluated expression, with the words
"Question 1 Result:" preceding your result print out.
'''

a = 10
x = 2
result1 = (a + 1) * x
print(f"Question 1 Result: {result1}")

ANSWER
correct




'''
# 2
Given three integer variables, x, lb, and ub (where x is 2, lb is 1, and ub is
2), write a single boolean expression that evaluates to True if x is strictly
between lb and ub, and False otherwise.
Print out the result of your evaluated expression, with the words
"Question 2 Result:" preceding your result print out.
'''

x = 2
lb = 1
ub = 2
result2 = lb <= x and x <= ub
print(f"Question 2 Result: {result2}")

ANSWER
x = 2
lb = 1
ub = 2
expression2 = lb < x < ub # lb < x and x < ub
print(expression2)


'''
# 3
Given three integer parameters a, b, and c (where a is 4, b is 3, and c is 5),
write a single boolean expression that returns True if a2+b2 is equal to c2
(this is called a "Pythagorean Triple"), and False otherwise. For example, given
the a=4, b=3, c=5, the expression evaluate as True. Print out the result of your
evaluated expression, with the words
"Question 3 Result:" preceding your result print out.
'''

a, b, c = 4, 3, 5
result3 = a**2 + b**2 == c**2
print(f"Question 3 Result: {result3}")

ANSWER
a = 4
b = 3
c = 5
expression3 = a ** 2 + b ** 2 == c ** 2
print(expression3)
print("Question 3 result: " + str(expression3))
print("Question 3 result: ", expression3)



'''
# 4
Suppose that, in order to graduate a (fictional) MA program, students need to
complete at least four Computer Science courses, at least four Social Science
electives, and exactly two workshop classes. Note that students are allowed to
substitute computing classes with courses from the Statistics Department.
Finally, their GPA must be above 3.0 to graduate from the program under normal
conditions. If their GPA is 3.0 or lower, they do have the option, though, to
write a thesis to complete their requirements and graduate.

Write an expression (and any variables that you find useful) to evaluate whether
students with the following characteristics are eligible to graduate from the
program. If they are eligible to graduate, your expression should evaluate as
True, otherwise it should evaluate as False. Print out the results of your
evaluated expressions for each student, with the words "Question 4, Student
NUMBER_HERE Graduation Eligibility:" preceding your result print out.

Student 1: 4 Social Science Electives, 3 Computer Science courses, 1 Statistics
course, 2 workshops, 3.7 GPA, no thesis on file.
Student 2: 5 Social Science Electives, 4 Statistics courses, 2 workshops,
3.0 GPA, wrote a thesis.
'''

cs_courses_1 = 3
ss_courses_1 = 4
workshop_1 = 2
stat_courses_1 = 1
gpa_1 = 3.7
thesis_1 = False

cs_courses_2 = 3
ss_courses_2 = 5
workshop_2 = 2
stat_courses_2 = 4
gpa_2 = 3.0
thesis_2 = True

course_requirement_1 = (cs_courses_1 + stat_courses_1) >= 4 and ss_courses_1 >= 4 and workshop_1 == 2
gpa_requirement_1 = gpa_1 > 3.0 or thesis_1
eligible_to_graduate_1 = course_requirement_1 and gpa_requirement_1
print(f"Question 4, Student 1 Graduation Eligibility: {eligible_to_graduate_1}")

course_requirement_2 = (cs_courses_2 + stat_courses_2) >= 4 and ss_courses_2 >= 4 and workshop_2 == 2
gpa_requirement_2 = gpa_2 > 3.0 or thesis_2
eligible_to_graduate_2 = course_requirement_2 and gpa_requirement_2
print(f"Question 4, Student 1 Graduation Eligibility: {eligible_to_graduate_2}")

ANSWER
#student 1
ss_1 = 4
cs_1 = 3
stat_1 = 1
ws_1 = 2
gpa_1 = 3.7
thesis_1 = False

grad_elig_1 = (((cs_1 + stat_1) >= 4) 
             and (ss_1 >= 4) 
             and (ws_1 == 2) 
             and (gpa_1 > 3.0 or thesis_1))
#student 2
ss_2 = 5
cs_2 = 0
stat_2 = 4
ws_2 = 2
gpa_2 = 3.0
thesis_2 = True

grad_elig_2 = (((cs_2 + stat_2) >= 4) 
             and (ss_2 >= 4) 
             and (ws_2 == 2) 
             and (gpa_2 > 3.0 or thesis_2))


