grades = {
        "math": [93,97,95],
        "history": [91,94,92],
        "english": [95,96,93]
    }
def main():
    #add_grade("math",99)
    #print_average("math")
    #print_grades("math")
    run_again = ""
    while (run_again!="no"):
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
            print(get_GPA)
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