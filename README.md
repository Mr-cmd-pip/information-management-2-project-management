# CSIT327 BSIT - 3     Cebu Institute of Technology - University
Group Members:
 1. Martus, Matthew Rimar S.  -  Owner of the repository
 2. Calzada, Earl Owen V.
 3. Cagampang, Emmanuel A. Jr.

## Klase (Learning Management System)
Kalse is a learning management and online assessment system for academic education for students and instructors.

## Run Locally

1. Download the lms.zip file
2. Create a virtual environment and activate it (Windows)

```bash
python -m venv env
```

```bash
env\Scripts\activate
```

3. Create a virtual environment and activate it (MacOS)

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Make migrations and migrate

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

6. Create admin/superuser

```bash
python manage.py createsuperuser
```

7. Finally run the project

```bash
python manage.py runserver
```

Now the project should be running on http://127.0.0.1:8000/

## Tech Stack

1. Django
2. Bootstrap
3. jQuery
4. Chart.js
5. Animate.css

## Required code and documentary repository
 1. Functional Requirements
 2. Gantt Chart
 3. ERD
 4. UI/UX Design

## Functional Requirement
1. User Authentication
   Description: Users (stduents) can create accounts, log in, and log out while (instructors) can only be created by admins but can still log in and logout.
    Details:
     - Registration with username, email, password
     - Login with username and password
2. Course Management
   Description: Instructors can create, update and delete courses.
    Details:
     - Creates a new course with title, description and other relevant details.
     - Edit course details
     - Delete courses
3. Enrollment Management
   Description: Students can enroll in and withdraw from courses.
    Details:
     - View available courses
     - Enroll in a couurse
     - Withdraw from a course
4. Assignment Submission
   Description: Students can submit assignments, and instructors can grade them.
    Details:
     - Submit assignments in various formats (e.g. documents, code file, etc.)
     - View and download submitted assignments.
     - Instructors can grade and provide feedback on assingments.
5. Discussion Forum
   Description: Students and Instructors can participate in course-related discussions.
    Details:
     - Post and reply to discussion topics
     - Moderation tools for instructors to manage discussions

## Gantt Chart Link:

```bash
   https://docs.google.com/spreadsheets/d/1DcrNyWu0C5bChdr00rlghfwas8pG24TgNMvCMtA2_tY/edit?gid=0#gid=0
```

## ERD Link:

```bash
   https://www.figma.com/board/UQNcDgun2TJrc0eVdP9ABQ/ERD--(LEARNING-MANAGEMENT-SYSTEM)?node-id=0-1&t=Ux4GpxGwlumqt3Dj-1
```

## UI/UX Link:

```bash
   https://www.figma.com/design/vSgB07hCwSr54QPheBsdOy/Assignment-%233%3A-System-UI%2FUX?node-id=0-1&t=61s05jexIn8YlwWF-1
```
