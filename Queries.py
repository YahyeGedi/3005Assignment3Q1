#Import psycopg, which will help us connect and run queries to our database
import psycopg


def getAllStudents():
    #Connect to the database using the name of the database, username, and password.
    with psycopg.connect("dbname=3005Assignment3Q1 user=postgres password=student") as db:
        with db.cursor() as cursor:        
            #Execute the query that will retrieve all students.
            cursor.execute("SELECT * FROM STUDENTS ORDER BY student_id ASC")
            result = cursor.fetchall()
        #If something was returned, do this.
        if result:
            print("\nList of Students:")
            #Some formatting to help see the data properly.
            print("{:<10} {:<15} {:<15} {:<30} {:<15}".format("Student ID", "First Name", "Last Name", "Email", "Enrollment Date"))
            print("-" * 90)
            #Prints the data to the terminal.
            for row in result:
                student_id, first_name, last_name, email, enrollment_date = row
                enrollment_date_string = enrollment_date.strftime("%Y-%m-%d") if enrollment_date else ""
                print("{:<10} {:<15} {:<15} {:<30} {:<15}".format(student_id, first_name, last_name, email, enrollment_date_string))
        #If nothing was returned, print this.
        else:
            print("No students found.")


def addStudent(first_name, last_name, email, enrollment_date): 
    #Connect to the database using the name of the database, username, and password.
    with psycopg.connect("dbname=3005Assignment3Q1 user=postgres password=student") as db:
        with db.cursor() as cursor:   
            #Execute this query that will add a student to the database.    
            cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date,))


def updateStudentEmail(student_id, new_email):
    #Connect to the database using the name of the database, username, and password.
    with psycopg.connect("dbname=3005Assignment3Q1 user=postgres password=student") as db:
        with db.cursor() as cursor:  
            #Execute this query that will update the email address of said student.
            cursor.execute("UPDATE students SET email = %s WHERE students.student_id = %s", (new_email, student_id))    

def deleteStudent(student_id):
    #Connect to the database using the name of the database, username, and password.
    with psycopg.connect("dbname=3005Assignment3Q1 user=postgres password=student") as db:
        with db.cursor() as cursor:  
            #Execute this query that will delete said student.
            cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))


#Running the program
if __name__ == '__main__':
    #While the user is doesn't want to quit.
    while True:
        print("\nOptions:")
        print("1. View all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")
        
        option = int(input("\nWhich function do you want to run? "))

        #Fancy way of doing if statements.
        match option:
            case 1:
                getAllStudents()

            case 2:
                first_name = input("\nEnter the first name of the student: ")
                last_name = input("Enter the last name of the student: ")
                email = input("Enter the email of the student: ")
                enrollment_date = input("Enter the enrollment date of the student: ")

                addStudent(first_name, last_name, email, enrollment_date)

            case 3:
                student_id = input("\nEnter the student ID: ")
                email = input("Enter the new email: ")
                updateStudentEmail(student_id, email)

            case 4: 
                idToDelete = input("\nEnter the student ID to delete: ")
                deleteStudent(idToDelete)

            case 5: 
                break;