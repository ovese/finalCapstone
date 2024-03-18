# Project name:
Task Manager

# Program description:
This project utilizes lists, dictionaries and functions to extend the
functionality of a simple task management system. The program is designed for
a small business to help it manage tasks assigned to each member of a team.

## This project aims include:
1. Ability to refactor code. 
2. Reduce code complexity, and 
3. Ensure the readability of a team’s functioning code so that other developers will not struggle to decipher the code.
4. Extend the functionality beyond the standard task specification where necessary or possible
5. Package the application for use and modification 
6. Demonstrate core software engineering principles covering OOP, SOLID, PEP8 standard

## What the application does:
The application allows for two types of users:
1. Admin user
2. Non-admin users

The admin has extended rights and priviledges which are not possessed by no-admin users. The admin differs from
non-admin users because he can view all tasks on record, generate reports and display statistics. Non-admin users
would not have the range of program options which the admin would have on their display panel


# Table of Contents


# Installation section:
To install the program on your local computer, the relavant libraries would have to be
installed on the host computer. These libraries have been made available in the requirements.txt
file which can be found in the repository of project files. 
Since development of the program was made in a virtual containerized enviroonment, pip freeze command
has been used to provide the complete list of libraries used within the virtual environment duriong production.
Finally, the program has been tested on both a windows command line environment and ubuntu 22.04 LTS and
it works seamlessly on both platforms.

# Program usage:
The program flow will be demonstrated with the aid of visuals, which are made by screen grabs of the program
during execution for each of the menu items.

In total, there are seven menu options which can be selected from by the admin, and 5 menu options which non-admin
users can choose from. These menu options are:
1. Registering a user(r): works to register a new user by requesting a username and password that must be unique
2. Adding a task(a): allocate task to a specific user
3. View all(va): view all allocated tasks with serial numbers
4. View mine(vm): view only current user's tasks and their serial number as found on task list
5. Generate reports(gr): Generate report which would be written to a text file. Two reports are required here viz-a-vis task_overview.txt and user_overview.txt
6. Display statistics(ds): Display statistics of task manager app usage and status by pulling information from the previous two files listed in (5)
7. Exit application(e)

## program sequence shown through screen illustrations
### user.txt file having registered users. Can be updated by registering new users
![login admin](/assets/images/user-txt.png)
### login screen and menu for admin and non-admin user
![login admin](/assets/images/log-in.png)
![login admin](/assets/images/log-in-others.png)
### Registration screen 
![login admin](/assets/images/register-user.png)
### View all screen
![login admin](/assets/images/view-all.png)
### View mine screen
![login admin](/assets/images/view-mine.png)
### View specific task screen
![login admin](/assets/images/view-specific.png)
### Generate report screen
![login admin](/assets/images/generate-report.png)
### Display statistics screen
![login admin](/assets/images/display-stats.png)
### Exit application screen
![login admin](/assets/images/exit.png)


# Credits:
The resulting  program was completed by the author and shows my understanding of various experimented concepts during the course
of the HyperionDev's software engineering bootcamp. However, I would like to sincerely thank the tutors, code reviewers and mentors who helped to make
the bootcamp a success. I am a much more confident software engineer because of them.



