import csv
grades = { }
filepath = "/Users/aliersch/Desktop/data-science/data-science/grades.csv"
try: 
    with open(filepath,'r') as f:
        data = csv.reader(f)
    for row in grades:
        if row:
            key = row[0] #first column = key
            values = row[1:] #py list splice = values
            grades[key]=values
except FileNotFoundError:
    print("file not found")
def main():
    run_again = "yes"
    #while the user still wants to use the gradebook
    while (run_again == "yes"):
        #asks which function to run, and runs the function corresponding to the number they input; asks for user input for parameters if necessary
        func_to_run = input("Choose a number: \n1) add a grade to a subject \n2) print your average for a subject \n3) print your grades for a subject \n4) print each subject's average \n5) print your GPA \n")
        if (func_to_run=="1"):
            print_subjects()
            subject = (input("What subject is it for? ")).lower()
            grade = input("What is the grade? ")
            add_grade(subject,int(grade))
        if (func_to_run=="2"):
            print_subjects()
            subject = (input("What subject? ")).lower()
            print_average(subject)
        if(func_to_run=="3"):
            print_subjects()
            subject = (input("What subject? ")).lower()
            print_grades(subject)
        if(func_to_run=="4"):
            print_all_averages()
        if(func_to_run=="5"):
            print("GPA: ",get_GPA())
        #asks if they want to continue using gradebook, runs again if yes, loop stops if no
        run_again = input("Do you want to run another method? (yes/no)")
        try:
            data = { }#non empty dictionary
            with open('output.csv','w',newline="") as file:
                writer = csv.writer(file)
                #iterate through keys and values in dataset, write to csv
                for key, value in data.items():
                    writer.writerow([key,value])
            print("successfully stored in csv")
        except FileNotFoundError:
            print("no file found")
def print_subjects():
    subjects = ""
    for subject in grades:
        subjects = subjects+subject+" "
    print("options: ",subjects," (or a new one)")
def add_grade(subject,grade):
    #adds grade parameter to the list corresponding to that subject
    if(subject in grades):
        grades[subject].append(grade)
    #creates new subject in dictionary with new grade if not already in dictionary
    else:
        grades[subject] = [grade]
    print("added ",str(grade)," to "+subject)
def print_average(subject):
    #adds the grades in that subject's list together, and divides by total number of grades, calculating and printing the average
    total = 0
    numGrades = 0
    for grade in grades[subject]:
        total=total+grade
        numGrades = numGrades +1
    average = total/numGrades
    print(f"{average:.2f}")
def print_grades(subject):
    #prints grades in the subject given by the parameter using a for loop
    for grade in grades[subject]:
        print(grade)
def print_all_averages():
    #prints all averages by iterating through the subjects and using the print average function for each one
    for subject in grades:
        print(subject,": ")
        print_average(subject)
def get_GPA():
    total = 0
    numGrades = 0
    #finds the average by adding all the grades in all subjects together, and divides by the total number of grades
    for subject in grades:
        for grade in grades[subject]:
            total = total + grade
            numGrades=numGrades+1
    average = total/numGrades
    #according to the average, reuturns the correct gpa value
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
def remove_grade(subject,grade):#removes specific grade in that subject
    grades[subject].remove(grade)
    print("removed " , str(grade)," from ",subject)
def visualize_grades():
    for subject in grades:
        graph = ""#empty string for the graph for that subject
        for grade in grades[subject]:#finds the average for that subject
            total=total+grade
            numGrades = numGrades +1
        average = total/numGrades
        while(average>=5):#while the average is 5 or above, add symbols to graph correspondingly
            if(average-50>0):#adds an X for 50 percent
                graph+="X"
                average = average-50
            if(average>5):#adds a * for 5 percent
                graph+="*"
                average = average-5
        print(subject+": "+graph)
if __name__ == "__main__":
    main()