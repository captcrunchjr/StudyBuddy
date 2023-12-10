#Shows the user info
SELECT DISTINCT username, password, email
FROM user_info;
#SET SQL_SAFE_UPDATES = 0;
#DELETE FROM user_info WHERE password = 'password5';

#Shows the user account
SELECT major, classes_enrolled, classes_taken, year, GPA
FROM user_account;

#Shows the colleges offered at UNC Charlotte
SELECT name
FROM colleges;

#Shows the different Majors in College of Computing
SELECT name
FROM college_computing;

#Shows the classes for the Web and Mobile Development degree
SELECT name
FROM classes;

SELECT *
FROM users;

SHOW triggers;


