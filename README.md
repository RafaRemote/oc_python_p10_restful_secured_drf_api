# Project 10: SoftDesk / Create a secured API with DRF

<img src="https://img.shields.io/badge/python-3.9.2-blue"
     alt="shiedls.io created badge"
     style="float: left; margin-right: 10px;" />
<img src="https://img.shields.io/badge/django-3.2.8-yellowgreen"
          alt="shiedls.io created badge"
          style="float: left; margin-right: 10px;" />
<img src="https://img.shields.io/badge/django--rest--framework-3.12.14-yellowgreen"
     alt="shiedls.io created badge"
     style="float: left; margin-right: 10px;" />
<img src="https://img.shields.io/badge/django%20default%20database-SQLite-yellowgreen"
     alt="shiedls.io created badge"
     style="float: left; margin-right: 10px;" />
<img src="https://img.shields.io/badge/djangorestframework--simplejwt-4.7.2-orange"
     alt="shiedls.io created badge"
     style="float: left; margin-right: 10px;" />

Menu

1. Usage
2. Endpoints
3. Entity–relationship model
4. Technologies
5. Installation
6. Execution of the program
7. flake8 report
8. Important information about the database
9. API Documentation
10. GDPR Compliance

## 1 - Usage  

API for an Issue Tracking System  
Anyone can sign up hence become a User then log in.  
  
**Only authenticated Users can consume the API.**  
  
User can create a project.  
Owner of the project can create/delete Project's Contributors.  
Contributors and Owner of a Project can create Project's Issues.  
Contributors and Owner of a Project can create Comment to Project's Issues.  
  
Only the Owner of a Project/Issue/Comment can update or delete it.  
  
## 2 - Endpoints  
  
_(check the [POSTMAN Api documentation](https://documenter.getpostman.com/view/12917774/UVC2HpH6) for all the details)_
  
|  			<br># 		  	|  			<br>API Endpoint 	|  			<br>HTTP Method 	|  			<br>URI 		  	|
|---	|---	|---	|---	|
|  			<br>1. 		  	|  			<br>User Signup 	| POST 	|  			<br>/signup 		  	|
|  			<br>2. 		  	|  			<br>Create User 	|  			<br>POST 		  	|  			<br>/login 		  	|
|  			<br>3. 		  	|  			<br>Get all Projects of the connected Usser 	|  			<br>GET 		  	|  			<br>/projects 		  	|
|  			<br>4. 		  	|  			<br>Create Project 	| POST 	|  			<br>/projects 		  	|
|  			<br>5. 		  	|  			 		<br>Get Project details with its id  	|  			<br>GET 		  	|  			<br>/projects/{id} 		  	|
|  			<br>6. 		  	|  			<br>Update Project 	|  			<br>PUT 		  	|  			<br>/projects/{id} 		  	|
|  			<br>7. 		  	|  			<br>Delete Project and its issues 	|  			<br>DELETE 		  	|  			<br>/projects/{id} 		  	|
|  			<br>8. 		  	|  			<br>Create a Contributor to a project 	|  			<br>POST 		  	|  			<br>/projects/{id}/users 		  	|
|  			<br>9. 		  	|  			<br>Get all the Contributors of a Project 	|  			<br>GET 		  	|  			<br>/projects/{id}/users 		  	|
|  			<br>10. 		  	|  			<br>Delete a Contributor 	|  			<br>DELETE 		  	|  			<br>/projects/{id}/users/{id} 		  	|
|  			<br>11. 		  	|  			<br>Get all the Issues of a Project 	|  			<br>GET 		  	|  			<br>/projects/{id}/issues 		  	|
|  			<br>12. 		  	|  			<br>Create a Project's Issue 	|  			<br>POST 		  	|  			<br>/projects/{id}/issues 		  	|
|  			<br>13. 		  	|  			<br>Update a Project's Issue 	|  			<br>PUT 		  	|  			<br>/projects/{id}/issues/{id} 		  	|
|  			<br>14. 		  	|  			<br>Delete a Project's Issue 	|  			<br>DELETE 		  	|  			<br>/projects/{id}/issues/{id} 		  	|
|  			<br>15. 		  	|  			<br>Create an Issue's Comment 	|  			<br>POST 		  	|  			<br>/projects/{id}/issues/{id}/comments 		  	|
|  			<br>16. 		  	|  			<br>Get all the Comments of an Issue 	|  			<br>GET 		  	|  			<br>/projects/{id}/issues/{id}/comments 		  	|
|  			<br>17. 		  	|  			<br>Update a Comment 	|  			<br>PUT 		  	|  			<br>/projects/{id}/issues/{id}/comments/{id} 		  	|
|  			<br>18. 		  	|  			<br>Delete a Comment 	|  			<br>DELETE 		  	|  			<br>/projects/{id}/issues/{id}/comments/{id} 		  	|
|  			<br>19. 		  	| Get a Comment with its id 	|  			<br>GET 		  	|  			<br>/projects/{id}/issues/{id}/comments/{id} 		  	|  
  
## 3 - Entity–relationship model  
  
### simplified view  
  
![ERD simplified](assets/images/database_representation.png)
  
### detailed view  

Automatically generated from the file 'db.sqlite3' with the database tool: <img src="https://img.shields.io/badge/DBeaver-CE-orange"
                                                                                alt="shiedls.io created badge"
                                                                                style="float: left; margin-right: 10px;" />  

![ERD detailed](assets/images/softDesk_erd.png)
  
## 4 - Technologies
  
Programming language: <img src="https://img.shields.io/badge/python-3.9.2-blue"
                           alt="shiedls.io created badge"
                           style="float: left; margin-right: 10px;" />  

Frameworks:  <img src="https://img.shields.io/badge/django-3.2.8-yellowgreen"
                  alt="shiedls.io created badge"
                  style="float: left; margin-right: 10px;" />
<img src="https://img.shields.io/badge/django--rest--framework-3.12.14-yellowgreen"
     alt="shiedls.io created badge"
     style="float: left; margin-right: 10px;" />  

Database: <img src="https://img.shields.io/badge/django%20default%20database-SQLite-yellowgreen"
     alt="shiedls.io created badge"
     style="float: left; margin-right: 10px;" />  

Security: <img src="https://img.shields.io/badge/djangorestframework--simplejwt-4.7.2-orange"
     alt="shiedls.io created badge"
     style="float: left; margin-right: 10px;" />  

## 5 - Installation MacOS / Windows
  
Default installation is for MacOS. There is some litle differences for Windows, follow the given details below.  
You need to have Python installed on your machine. [install python](https://www.python.org/downloads/)  
You need to have Git installed on your machine. [install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  
  
Open a terminal wherever you want then follow these steps:  

- Clone the repository:  

```python
git clone https://github.com/RafaRemote/DAPY_P10_softDesk.git
```

- Move to the root folder:  

```python
cd DAPY_P10_softDesk
```

- Create the virtual environment:  
(check your version of Python. Your environment should use python 3.9.2)

```python
python -m venv env
```

### _command to create the virtual environment for windows_
  
```python
py -m venv env  
```

- Activate the virtual environment:  

```python
source env/bin/activate
```

### _command to activate the virtual environment for windows_
  
```python
env\Scripts\activate  
```

- Upgrade pip:  

```python
pip install --upgrade pip
```

- Install the project dependencies:  

```python
pip install -r requirements.txt
```

## 6 - Execution of the program

From the terminal, be sure to be in the root folder (named 'DAPY_P10_softDesk'), then follow this steps:  

```python
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  
```

Development server starts at: [http://127.0.0.1:8000/](http://127.0.0.1:8000)  

## 7  POSTMAN API Documentation

[postman api documentation](https://documenter.getpostman.com/view/12917774/UVC2HpH6)

## 8 - Important information about the database

The database is empty.  

If you want to create a superuser to access the default Django adminstration page, follow these instructions:

Open a second terminal. (first one is running the script).  
Type:

```python
python manage.py createsuperuser
```

Follow the instructions, once the superuser created you can access the default Django adminstration page and log in with your freshly created credentials @ [http:127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).  
  
## 9 - flake8 report
  
In the root folder (named: 'DAPY_P10_softDesk') you'll find a folder called: 'flake8_report', including an index.html showing 'no flake8 violations'.  

To generate a new report:  

erase the folder 'flake8_report'.  
be sure to be in the root folder 'litreview', then type:  

```python
flake8 --format=html --htmldir=flake8_report
```

## 10 - GDPR Compliance
  
Private data kept in the database are the following:  
  
| data       |
|------------|
| first name |
| last name  |
| email      |
  
**Security**:  
  
Authentication does use the JSON Web Tokens.  
Passwords are encrypted in the database.  
Throttling Policy is set up globally for the project.  
  
If any questions about the protection of the GDPR [contact us](mailto:raphael.49410@gmail.com?Subject=GDPR_api_softDesk)  
  