use campusbuddies;

insert into user values (1, "Josh Eckard", "captcrunchjr@gmail.com", null, 1);
insert into user values (2, "Jon Icard", "fakejicard@gmail.com", null, 1);

insert into discipline values(1,"Computer Science"), (2, "Business"), (3, "Math");

insert into degree values (1, "Software Engineering", 1), (2, "Networking", 1), (3, "Data Science", 1);
insert into degree values (4, "Business Admin", 2), (5, "Accounting", 2);
insert into degree values (6, "Teachable Math", 3), (7, "Theoretical Math", 3);
select * from degree;

insert into course values (1, "Data Structures", 1), (2, "Networking 101", 2), (3, "Data Science Course", 3);
insert into course values (4, "How to Admin a Business", 4), (5, "Intro to Accounting", 5), (6, "Math Basics", 6);
select * from course;

insert into post values (1, 1, 1, sysdate(), sysdate(), "Need Help with Data Structures", "I'm currently taking data structures and it's pretty tough.");
insert into post values (2, 4, 1, sysdate(), sysdate(), "Need Help with How to Admin a Business", "I'm currently taking how to admin a business and it's pretty tough.");
insert into post values (3, 3, 1, sysdate(), sysdate(), "Need Help with Data Science Course", "I'm currently taking data science course and it's pretty tough.");

insert into comment values (1, 1, 1, sysdate(), sysdate(), "Bump");
insert into comment values (2, 2, 1, sysdate(), sysdate(), "I know it's really tough");
insert into comment values (3, 3, 1, sysdate(), sysdate(), "Just drop the class");

insert into feed_post values (1, 1, "Hi guys, my name is Josh Eckard. I am a Senior at University of North Carolina at Charlotte. Going into my finaly year, i am trying to find help with Introduction to AR and VR. i have joind the studdy buddies group for that class. If you are also looking for help, please message me so we could study together.", sysdate());
