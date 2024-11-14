# Klase
A learning management and online assessment system for academic education.

## CSIT327 - G7     BSIT - 3     Cebu Institute of Technology - University

## Group Members:
 1. Martus, Matthew Rimar S.  - Owner of the repository
 2. Calzada, Earl Owen V.
 3. Cagampang, Emmanuel A. Jr.

## Required code and documentary repository
 1. Functional Requirements
 2. Gantt Chart
 3. ERD
 4. UI/UX Design

The Above Made By : Martus, Matthew Rimar S.

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

## Tech Stack

1. Django
2. Bootstrap
3. jQuery
4. Chart.js
5. Animate.css

## Run Locally

1. Clone the project

```bash
git clone https://github.com/JivSTuban/lms.git
```

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

4. Go to the klase directory

```bash
cd klase
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Make migrations and migrate

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

7. Create admin/superuser

```bash
python manage.py createsuperuser
```

8. Finally run the project

```bash
python manage.py runserver
```

Now the project should be running on http://127.0.0.1:8000/
