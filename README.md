## Creator: Nick Keiffer
## Last edited: 06/28/2021

## Application name: LineUp
```
Tested on Google Chrome Version 91.0.4472.106 using Python 3.8.3

My test account (feel free to check it out):
	Username: "nickeiffer"
	Password: "Password1"

Description:
	LineUp is multi-featured 'todo' management web application that priorities user experience and clean design.

Features:
	* User login/registration system
		- Unique usernames
		- Encrypted passwords
		- User sessions
		- No password reset feature
	* Manage todos
		- Mark todo as completed/incomplete
		- Add new todos
		- Edit existing todos
		- Delete existing todos
		- Attach a due date to todos
		- Attach a note to todos
		- Attach a priority to todos
	* Sort todos in ascending or descending order
		- Sort by title
		- Sort by date created
		- Sort by date due
		- Sort by priority
```
## Setup
```
In Terminal:
pip3 install -r requirements.txt (this depends on how your system is set up)
```
## Usage
```
Use python3.8 or equivalent version

In Terminal:
	To run with existing database --> python3 run.py
	To clear database and run --> python3 run.py drop

On Internet browser:
	Go to site http://127.0.0.1:3000/
```
## Directory Tree

```
├── README.md
├── lineup
│ ├── __init__.py
│ ├── book.sqlite
│ ├── config.py
│ ├── main
│ │ ├── __init__.py
│ │ ├── forms.py
│ │ ├── routes.py
│ │ └── utils.py
│ ├── models.py
│ ├── static
│ │ ├── css
│ │ │ ├── bootstrap.min.css
│ │ │ ├── bootstrap.min.css.map
│ │ │ ├── imgs
│ │ │ │ ├── background-overlay.png
│ │ │ │ ├── priority-green.png
│ │ │ │ ├── priority-outline.png
│ │ │ │ ├── priority-red.png
│ │ │ │ ├── priority-yellow.png
│ │ │ │ └── priority.png
│ │ │ └── main.css
│ │ └── js
│ │     ├── bootstrap.min.js
│ │     ├── bootstrap.min.js.map
│ │     ├── jquery-3.2.1.min.js
│ │     └── main.js
│ ├── templates
│ │ ├── home.html
│ │ ├── layout.html
│ │ ├── login.html
│ │ └── register.html
│ ├── todos
│ │ ├── __init__.py
│ │ ├── forms.py
│ │ └── routes.py
│ └── users
│     ├── __init__.py
│     ├── forms.py
│     └── routes.py
├── requirements.txt
└── run.py`
```























