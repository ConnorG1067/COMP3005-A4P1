### Video
https://youtu.be/xdlEFcFh6tE

### Database Instructions
1. Create a new database on the localhost port 5432
2. Change the dbname in the code to your database name, as well as the user name and password
3. Run the sql command below to create the table
   ```
      CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        first_name varchar(255) NOT NULL,
        last_name varchar(255) NOT NULL,
        email varchar(255) NOT NULL UNIQUE,
        enrollment_date DATE
    );
   ```
4. Insert the following students into the database
   ```
   INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
   ```

### Compile and Run Application
1. Download all dependencies
2. Configure the database
3. Run the CRUD.py file

### Brief Explanation
1. Main() - Handles all the user inputs and the operations for preforming certain tasks
2. getAllStudents(connection) - Returns a list of tuples of each student
3. addStudent(first_name, last_name, email, enrollment_date, connection) - adds a student to the table with the corresponding values
4. updateStudentEmail(student_id, new_email, connection) - updates a students email with the corresponding values
5. deleteStudent(student_id, connection) - delete the student at the student id


