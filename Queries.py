import psycopg



def getAllStudents():
    with psycopg.connect("dbname=3005Assignment3Q1 user=postgres password=student") as db:
        with db.cursor() as cursor:        
            cursor.execute("SELECT * FROM STUDENTS ORDER BY student_id ASC")
            result = cursor.fetchall()

        for row in result:
            print(row)


getAllStudents()