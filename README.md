# 0x00. AirBnB clone - The console

## Description

This project is the first step towards building our first full web application: an AirBnB clone. In this project, we wrote a command interpreter to manage our AirBnB objects. 
* A parent class (called `BaseModel`) was put in place to take care of the initialization, serialization and deserialization of future instances.
* Created a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Created all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
* Created the first abstracted storage engine of the project: File storage.
* Created all unittests to validate all our classes and storage engine

## Learning Objectives
* How to create a Python package
* How to create a command interpreter in Python using the `cmd` module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage `datetime`
* What is an `UUID`
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

## Requirements for Python scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version 1.7 or more)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation
* All your classes should have a documentation
* All your functions (inside and outside a class) should have a documentation

## Console
The console is a CLI that allows the use of data as backend tool.
It can be used to handle all classes predefined  previously called into
`storage` object.

### How to Use the CLI non-interactive
To run the console in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
```

### How to Use the CLI interactive
To run the console in interactive mode:

run the file console.py:

```
$ ./console.py

```

Running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

## How to Use it / Examples
### Console Commands
AirBnB supports the following commands:
* **create**
  * Usage: create <class>
Creates a new instance of a given class. Class' ID is printed and
the instance is saved to the file file.json.

```
example
```

* **show**
  * Usage: show <class> <id> or <class>.show(<id>)
Prints a string representation of a class instance based on a given id.

```
hbnb) show BaseModel My_very_First_Model                                              
** no instance found **

```

```
(hbnb) show BaseModel                                                                  
** instance id missing **  
```

* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`
Deletes a class instance based on a given id from the storage file file.json and
it is updated accordingly.

```
(hbnb) destroy                                                                   
** class name missing **                                                         

```

* **all**
  * Usage: all or all <class> or <class>.all()
Prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

```
example
```
* **count**
  * Usage: `count <class>` or `<class>.count()`
Retrieves the number of instances of a given class.

```
example
```

* **update**
  * Usage: update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>).
Updates a class instance based on a given id with a given key/value attribute	
pair or dictionary of attribute pairs. If update is called with a single 
key/value attribute pair, only "simple" attributes can be updated (ie. not 
id, created_at, and/or updated_at).

```
example
```

## How to Test:
Unittests for the CLI AirBnB project are defined in the [tests](./tests)
folder. To run the entire test suite simultaneously, execute the following
command:

```
$ python3 unittest -m discover tests
```

Also, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Files
---
File|Task
---|---
console.py | Program that contains the entry point of the command interpreter
models/amenity.py | A class called `Amenity` that inherits from `BaseModel`
models/base_model.py | A parent class called `BaseModel` that takes care of the initialization, serialization and deserialization of our future instances
models/city.py | A class called `City` that inherits from `BaseModel`
models/place.py | A class called `Place` that inherits from `BaseModel`
models/review.py | A class called `Review` that inherits from `BaseModel`
models/state.py | A class called `State` that inherits from `BaseModel`
models/user.py | A class called `User` that inherits from `BaseModel`
models/\_\_init\_\_.py | An init file that makes `models` a package and declares an instance of class `FileStorage` called `storage` that reloads/deserializes all serialized object instances from the filename held in private class attribute `__file_path`
models/engine/file_storage.py | A class called `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances
models/engine/\_\_init\_\_.py | Empty init file that makes `engine` a module

## Directories
---
Directory Name | Description
---|---
models/ | Contains all model files where classes are defined
models/engine/ | Contains file where class `FileStorage` is defined
tests/test_models/ | Contains unittests files to test classes in dir `models/`
tests/test_models/test_engine | Contains unittest files to test classes in dir `engine/`

## Authors
