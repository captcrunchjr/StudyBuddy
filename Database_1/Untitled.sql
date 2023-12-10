/*Question 1*/
Select student.first_name, student.last_name
From student;

/*Question 2*/
Select instructor_id
From instructor
Where tenured = 1;

/*Question 3*/
Select s.first_name AS student_first_name, 
       s.last_name AS student_last_name, 
       i.first_name AS advisor_first_name, 
       i.last_name AS advisor_last_name
From student s
INNER JOIN instructor i ON s.advisor_id = i.instructor_id;

/*Question 4*/
Select i.instructor_id, i.first_name, i.last_name
From instructor i
LEFT JOIN student s ON i.instructor_id = s.advisor_id
Where s.advisor_id IS NULL;

/*Question 5*/
Select i.first_name, i.last_name, SUM(c.num_credits) AS total_credits
From instructor i
LEFT JOIN course c ON i.instructor_id = c.instructor_id
GROUP BY i.instructor_id, i.first_name, i.last_name;

/*Question 6*/
Select course_code, course_name
From course
Where course_code LIKE '_____3%';

/*Question 7*/
Select c.course_code, i.first_name, i.last_name, c.num_credits
From student_schedule ss
JOIN course c ON ss.course_id = c.course_id
JOIN instructor i ON c.instructor_id = i.instructor_id
Where ss.student_id = 1;


