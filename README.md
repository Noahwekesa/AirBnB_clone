# Project: AirBnB Clone 


-  The full-stack project is divided into 7 Parts:

|                                                      Parts                                                 |                    Description                    |
| :--------------------------------------------------------------------------------------------------------  | :-----------------------------------------------  |
### 1. Console            |   Data model management via command interpreter   |
### 2 web static        |             Landing page in HTML and CSS          |
| 3. MySQL storage                                                                                           | Migration of local file storage to MySQL database |
| 4. Deploy static                                                                                           |        Deploy web static on an Nginx server       |
| 5. Web framework - templating                                                                              |         Web server deployment with Flask          |
| 6. RESTful API                                                                                             |      Creating endpoints for CRUD operations       |
| 7. Web dynamic                                                                                             | Loading of objects from client side using Jquery  |


## Part 1: 0x00. AirBnB clone - The console

![](./images/img_1.png)

Part 1 of AirBnB Clone project  The goal of this project is to deploy a server with a simple copy of the AirBnB web app to demonstrate technical grasp (dare we say mastery?) of both front & backend development.

The overall Project scope is:

- Build a command line interpreter to manipulate data without a visual interface.
- A front-end (user interface) and a back-end for the web app: static and dynamic
- Data storage via a database or a file storage
- An API that bridges the front-end and the data (retrieve, create, delete, update)

### Objectives For The BaseModel Class: A Class that defines all common attributes/methods for other classes:

#### Public instance attributes:

- **id:** string - assign with an uuid when an instance is created

- **created_at:** The current datetime when an instance is created

- **updated_at:** The current datetime when an instance is created, updated every time you change your object

- **__str__:** should print: [<class name>] (<self.id>) <self.__dict__>

#### Public instance methods:
- save(self): updates the public instance with the current datetime
- to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance. This method will be the first piece of the serialization/deserialization process to JSON format.

### Objectives For The Command Line Interpreter:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### Operating In Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Operating In Non-Interactive Mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
**Example Usage:**
```
newMod = BaseModel()
       - creates an instance of a method

print(NewMod.id)
	- prints the UUID
	   b6a6e15c-c67d-4312-9a75-9d084935e5

print(NewMod.created_at)
         - prints the time when the instance was created (ISO format)
	   '2017-09-28T21:03:54.052298'

print(NewMod.updated_at)
	- prints the most recent time that file was updated (ISO format)
       	  '2017-09-28T21:03:54.052302'
```
### Directory Tree Structure For Phase #1 of HBnB Clone:
```
.
├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── file_storage.cpython-34.pyc
│   │       └── __init__.cpython-34.pyc
│   ├── __init__.py
│   ├── place.py
│   ├── __pycache__
│   │   ├── amenity.cpython-34.pyc
│   │   ├── base_model.cpython-34.pyc
│   │   ├── city.cpython-34.pyc
│   │   ├── __init__.cpython-34.pyc
│   │   ├── place.cpython-34.pyc
│   │   ├── review.cpython-34.pyc
│   │   ├── state.cpython-34.pyc
│   │   └── user.cpython-34.pyc
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    └── test_models
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-34.pyc
        │   ├── test_amenity.cpython-34.pyc
        │   ├── test_base_model.cpython-34.pyc
        │   ├── test_city.cpython-34.pyc
        │   ├── test_place.cpython-34.pyc
        │   ├── test_review.cpython-34.pyc
        │   ├── test_state.cpython-34.pyc
        │   └── test_user.cpython-34.pyc
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-34.pyc
        │   │   └── test_file_storage.cpython-34.pyc
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py

```
---
## Files

File Name | Description
--- | ---
`README.md` | A description of the Alx AirBnB Project
`AUTHORS` | A listing of the project contributors
`console.py` | The program to launch the HBNB console
`basemodel.py` | Defines the BaseModel Class
`file_storage.py` | Defines the FileStorage Class & handles the database
`user.py` | Defines the User Class, a subclass of BaseModel
`city.py` | Defines the City Class, a subclass of BaseModel
`state.py` | Defines the User Class, a subclass of BaseModel
`amenity.py` | Defines the Amenity Class, a subclass of BaseModel
`review.py` | Defines the Review Class, a subclass of BaseModel
`place.py` | Defines the Place Class, a subclass of BaseModel
`tests/` | The test directory containing the unittest files for each Class
---
