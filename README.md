# Project 10: SoftDesk / Create a secured API with DRF

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

## 1 - Usage  

API for an Issue Tracking System  

## 2 - Endpoints  
  
  |  			 # 		   |  			 API Endpoint                            |  			 HTTP Method |  			 URI 		                                      |
|--------|-------------------------------------------|---------------|---------------------------------------------|
|  			 1. 		  |  			 User Signup                             | POST          |  			 /signup/ 		                                 |
|  			 2. 		  |  			 Create User                             |  			 POST 		       |  			 /login/ 		                                  |
|  			 3. 		  |  			 Get all Projects of the connected Usser |  			 GET 		        |  			 /projects/ 		                               |
|  			 4. 		  |  			 Create Project                          | POST          |  			 /projects/ 		                               |
|  			 5. 		  |  			 		 Get Project details with its id        |  			 GET 		        |  			 /projects/{id}/ 		                          |
|  			 6. 		  |  			 Update Project                          |  			 PUT 		        |  			 /projects/{id}/ 		                          |
|  			 7. 		  |  			 Delete Project and its issues           |  			 DELETE 		     |  			 /projects/{id}/ 		                          |
|  			 8. 		  |  			 Create a Contributor to a project       |  			 POST 		       |  			 /projects/{id}/users/ 		                    |
|  			 9. 		  |  			 Get all the Contributors of a Project   |  			 GET 		        |  			 /projects/{id}/users/ 		                    |
|  			 10. 		 |  			 Delete a Contributor                    |  			 DELETE 		     |  			 /projects/{id}/users/{id} 		                |
|  			 11. 		 |  			 Get all the Issues of a Project         |  			 GET 		        |  			 /projects/{id}/issues/ 		                   |
|  			 12. 		 |  			 Create a Project's Issue                |  			 POST 		       |  			 /projects/{id}/issues/ 		                   |
|  			 13. 		 |  			 Update a Project's Issue                |  			 PUT 		        |  			 /projects/{id}/issues/{id} 		               |
|  			 14. 		 |  			 Delete a Project's Issue                |  			 DELETE 		     |  			 /projects/{id}/issues/{id} 		               |
|  			 15. 		 |  			 Create an Issue's Comment               |  			 POST 		       |  			 /projects/{id}/issues/{id}/comments/ 		     |
|  			 16. 		 |  			 Get all the Comments of an Issue        |  			 GET 		        |  			 /projects/{id}/issues/{id}/comments/ 		     |
|  			 17. 		 |  			 Update a Comment                        |  			 PUT 		        |  			 /projects/{id}/issues/{id}/comments/{id} 		 |
|  			 18. 		 |  			 Delete a Comment                        |  			 DELETE 		     |  			 /projects/{id}/issues/{id}/comments/{id} 		 |
|  			 19. 		 | Get a Comment with its id                 |  			 GET 		        |  			 /projects/{id}/issues/{id}/comments/{id} 		 |  


## 3 - Entity–relationship model  
  
### simplified view  
  
![ERD simplified](assets/images/database_representation.png)
  
### detailed view  
  
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

## 5 - Installation

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

- Install the virtual environment:  

```python
python3 -m venv env
```

or on windows: py -m venv env  

- Activate the virtual environment:  

```python
source env/bin/activate
```

or on windows: env\Scripts\activate  

- Upgrade pip:  

```python
pip install --upgrade pip
```

- Install the project dependencies:  

```python
pip install -r requirements.txt
```

## 6 - Execution of the program

From the terminal, be sure to be in the root folder (named 'DAPY_P10_softDesk'), then type:  

```python
python manage.py runserver
```

Development server starts at: [http://127.0.0.1:8000/](http://127.0.0.1:8000)  

## 7 - flake8 report

In the root folder (named: 'DAPY_P10_softDesk') you'll find a folder called: 'flake8_report', including an index.html showing 'no flake8 violations'.  

To generate a new report:  

erase the folder 'flake8_report'.  
be sure to be in the root folder 'litreview', then type:  

```python
flake8 --format=html --htmldir=flake8_report
```

## 8 - Important information about the database

The database is empty.  

If you want to create a superuser to access the default Django adminstration page, follow these instructions:

Open a second terminal. (first one is running the script).  
Type:

```python
python manage.py createsuperuser
```

Follow the instructions, once the superuser created you can access the default Django adminstration page and log in with your freshly created credentials @ [http:127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).  
  
## 9  POSTMAN API Documentation

[postman api documentation](https://documenter.getpostman.com/view/12917774/UVC2HpH6)
