# AirBnB clone - The console


## Learning Objectives

**General**

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

### First step: Write a command interpreter to manage your AirBnB objects

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

#### Whats a command interpreter?

Do you remember the Shell? Its exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc
- Do operations on objects (count, compute stats, etc)
- Update attributes of an object
- Destroy an object

##### Execution

*Your shell should work like this in interactive mode:*

$ ./console.py

(hbnb) help


Documented commands (type help <topic>):

========================================

EOF  help  quit


(hbnb)

(hbnb)

(hbnb) quit

$


*But also in non-interactive mode: (like the Shell project in C)*

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

# Examples
$
(hbnb) create BaseModel(or User, Review, State, Amenity, City, Place)
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
$
$
(hbnb)
(hbnb) all BaseModel(or User, Review, State, Amenity, City, Place)
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
$
$
(hbnb)
(hbnb) show BaseModel(or User, Review, State, Amenity, City, Place) 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
$
$
(hbnb)
(hbnb) update BaseModel(or User, Review, State, Amenity, City, Place) 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
$
(hbnb)
(hbnb) show BaseModel(or User, Review, State, Amenity, City, Place) 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb)
(hbnb) create BaseModel(or User, Review, State, Amenity, City, Place)
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb)
(hbnb) all BaseModel(or User, Review, State, Amenity, City, Place)
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb)
(hbnb) destroy BaseModel(or User, Review, State, Amenity, City, Place) 49faff9a-6318-451f-87b6-910505c55907
(hbnb)
(hbnb) show BaseModel(or User, Review, State, Amenity, City, Place) 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).count()
2
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).show("Holberton")
** no instance found **
(hbnb) 
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).count()
2
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).count()
1
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).destroy("Holberton")
** no instance found **
(hbnb) 
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb)
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 23, 'first_name': 'Bob', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb) 
(hbnb) User(or BaseModel, Review, State, Amenity, City, Place).show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)


# Authors
Carlos Araque - Luciana Sarachu
