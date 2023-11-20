import psycopg2
from datetime import date, datetime

def main():
    # Establish a connection
    connection = psycopg2.connect(
        host='localhost', 
        dbname='A4Db', 
        user='postgres',
        password='COMP3005',
        port=5432
    )

    # Set the user choice to an invalid value
    user_choice = -1
    # While the user choice is not invalid
    while(user_choice != 0):
        # Set the user_choice to the input the user selects from the menu
        user_choice = int(input(
            """Please pick an option
    0. Exit the program
    1. List all students
    2. Add a student
    3. update a student email
    4. delete a student
"""
        ))
        # if the input is 0 exit the program
        if(user_choice == 0):
            break
        elif(user_choice == 1):
            # Gets all the students
            print("Getting students")
            getAllStudents(connection)
        elif(user_choice == 2):
            # Add the student
            print("Adding student")
            # Get all the data for the student
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            enrollment_date_input = input("Enrollment Date (- between): ")
            # add the student with their corresponding data
            addStudent(first_name, last_name, email, datetime.strptime(enrollment_date_input, "%Y-%m-%d").date(), connection)
        elif(user_choice == 3):
            # Update the email of a student
            print("Update student email")
            # Get a student id and an email
            student_id = input("Student ID: ")
            email = input("Email: ")    
            # Updat the students email        
            updateStudentEmail(student_id, email, connection)
        elif(user_choice == 4):
            # Deletes a student
            print("Delete a student")
            # Get the student id to delete
            student_id = input("Student ID: ")
            # Delete the student
            deleteStudent(student_id, connection)
        else: 
            # Notify the user the option is not valid
            print("Not a valid option")

    # Connection is closed
    connection.close()

# Gets all the students in the table
def getAllStudents(connection):
    # Set up a cursor
    db_cursor = connection.cursor()
    # Get all the students
    db_cursor.execute('SELECT * FROM students')
    # Get the data
    data = db_cursor.fetchall()
    # If there is no data
    if(len(data) <= 0):
        print("The table is empty")
    # Print each row
    for row in data:
        print(row)

    # close the cursor
    db_cursor.close()

def addStudent(first_name, last_name, email, enrollment_date, connection):
    # Set up a cursor
    db_cursor = connection.cursor()
    try:
        # Insert a student into the table
        db_cursor.execute(
            """ INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s)""",
            (first_name, last_name, email, enrollment_date)
        )
        # Notify the user it was added
        print("Successfully added")
    except Exception as e:
        # Let the user know its not a unique email
        print("Not a unique email")
    # Update the changes server side
    connection.commit()
    # Close the cursor
    db_cursor.close()


def updateStudentEmail(student_id, new_email, connection):
    # Set up a cursor
    db_cursor = connection.cursor()
    # Attempt to update the email at student id
    db_cursor.execute(
        """UPDATE students
        SET email = %s
        WHERE student_id=%s;""",
        (new_email, student_id)
    )
    # Print either successfully updated or no updates made
    print("Successfully Updated" if db_cursor.rowcount > 0 else "No updates made")
    # Update the changes server side
    connection.commit()
    # Close the cursor
    db_cursor.close()


def deleteStudent(student_id, connection):
    # Set up a cursor
    db_cursor = connection.cursor()
    # Attempt to delete the student from the table
    db_cursor.execute(
        """DELETE FROM students
        WHERE student_id=%s;""",
        (student_id,)
    )
    # If deleted let the user know
    print("Successfully Deleted" if db_cursor.rowcount > 0 else "No deletions made")
    
    # Update changes server side
    connection.commit()
    # Close the cursor
    db_cursor.close()

main()