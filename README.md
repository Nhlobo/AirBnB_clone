# AirBnB Clone - The Console

This console application serves as the cornerstone of Nhlobo's AirBnB Clone project. Inspired by the fundamental concepts covered at Holberton School, the goal is to deploy a server resembling a simplified version of the AirBnB website, offering a command interpreter to manage various objects.

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of Use](#examples-of-use)
* [Known Issues](#known-issues)
* [Contributors](#contributors)
* [License](#license)

## Environment
This project is designed and tested on Ubuntu 14.04 LTS using Python3 (version 3.4.3).

## Installation
* Clone this repository: `git clone "https://github.com/nhlobo/AirBnB_clone.git"`
* Navigate to the project directory: `cd AirBnB_clone`
* Run the console interactively: `./console` and enter commands
* Run the console non-interactively: `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - The console's entry point for the command interpreter. The current supported commands include:
* `EOF` - exits the console 
* `quit` - exits the console
* `<emptyline>` - overwrites the default empty line method and does nothing
* `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file), and prints the id
* `destroy` - Deletes an instance based on the class name and id (saving the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representations of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attributes (saving the change into the JSON file). 

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JSON serialization and deserialization:
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to

## Contributors
Nhlovo Mathebula - [Github](https://github.com/nhlovomathebula)

## License
Public Domain. No copyright protection.
