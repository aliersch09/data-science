grades = {
        "math": [93,97,95],
        "history": [91,94,92],
        "english": [95,96,93]
    }
def main():
    #add_grade("math",99)
    #print_average("math")
    #print_grades("math")
    run_again = "yes"
    while (run_again == "yes"):
        func_to_run = input("Choose a number: 1) add a grade to a subject 2) print your average for a subject 3) print your grades for a subject 4) print each subject's average 5) print your GPA")
        if (func_to_run=="1"):
            subject = input("What subject is it for? ")
            grade = input("What is the grade? ")
            add_grade(subject,int(grade))
        if (func_to_run=="2"):
            subject = input("What subject? ")
            print_average(subject)
        if(func_to_run=="3"):
            subject = input("What subject? ")
            print_grades(subject)
        if(func_to_run=="4"):
            print_all_averages()
        if(func_to_run=="5"):
            print("GPA: ",get_GPA())
        run_again = input("Do you want to run another method? (yes/no)")
def add_grade(subject,grade):
    grades[subject].append(grade)
def print_average(subject):
    total = 0
    for grade in grades[subject]:
        total=total+grade
    average = total/3
    print(average)
def print_grades(subject):
    for grade in grades[subject]:
        print(grade)
def print_all_averages():
    for subject in grades:
        print(subject,": ",print_average(subject))
def get_GPA():
    total = 0
    numGrades = 0
    for subject in grades:
            for grade in subject:
                total = total + grade
                numGrades=numGrades+1
    average = total/numGrades
    if (average>=92.5):
        return 4.0
    if (average<=92.49 and average>=89.5):
        return 3.7
    if (average<=89.49 and average>=79.5):
        return 3.0
    if(average<=79.49 and average>=69.5):
        return 2.0
    if(average<=69.49 and average>=65.0):
        return 1.0
    if(average<65.0):
        return 0

#Deliverables
#1) The general purpose of my program is to provide a database for my user to store their grades for multiple classes. The program allows the user to easily access the students grades, different averages, and GPA, without having to manually do the calculations.
#2) Two possible expected users for my program are students and teachers. 
# This program would be helpful for teachers because it can be difficult managing students grades, and making sure all calculated averages are accurate. This program provides an organized database of a students grades, and reliable calculated averages/GPAs. 
# This program would be helpful for students to keep track of their grades, so that they are aware of how they are doing in their classes, and can help them avoid stress. It can also prevent students from bothering their teachers about knowing their averages, because this program provides them easy access to that.
#3) One non-negotiable of this project is the print average function, since that is the most important aspect of determining how a student is doing in a class.
# One feature that is nice to have is the get GPA function, since determining a student's gpa is easy with the print all averages function already accessable. Although, this function is nice to have, since it provides a quick answer, where you don't have to think of/calculate the GPA from the averages yourself. 
#4) One additional feature could be a sub dictionary, where you can separate quiz and test grades, since they are weighted differently. This would add the value of the ability to calculate averages in classes with a more complex grading system.
#Another additional feature could be a function that tells you a minimum grade you have to get on a test to move your average to a specific grade. This would add the value of students not having to waste their time calculating themselves what grade they have to get to have a good grade in a class, so they can spend that time studying instead. 