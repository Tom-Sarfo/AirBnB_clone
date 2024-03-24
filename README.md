# 0x00. AirBnB clone - The console

## Project Description
Welcome to the Airbnb Clone – a simplified command-line interface (CLI) designed for ease of use. This initiative is part of the ALX curriculum project, presenting an interactive shell to manage instances of various classes such as User, amenity, city, place, state, review, and the BaseModel, serving as the foundation for all other classes.
## Command Interpreter Description
The command interpreter plays a pivotal role in the Airbnb Console Clone project, offering users an interactive shell to engage with the application. It acts as a textual interface through which users can input commands to execute a range of operations, encompassing the creation, display, modification, and removal of instances across diverse classes.
### Key Features:

- **User-friendly-interface:** The command interpreter provides a simple and user-friendly interface, facilitating smooth navigation and execution of commands for users.
- **CRUD Operations:** Users can effortlessly carry out operations of Creation, Reading, Updating, and Deletion on instances of various classes present in the application (User, Amenity, City, State, Review, and BaseModel).
- **Dynamic handling:** - The interpreter dynamically manages various classes, enabling users to interact with multiple models like BaseModel and User.
- **Command Interpreter:** Use a command-line interface to engage with the application.
- **Data Serialization:** The interpreter communicates with a specialized FileStorage class, guaranteeing accurate serialization and deserialization of data to and from JSON files to maintain persistent storage.

### Usage

To use the Airbnb Console Clone, follow these steps:

1. Clone the repository:

    ```bash
    git clone [The Git Repository URL]
    ```

2. Navigate to the project repository:

    ```bash
    cd AirBnB_clone
    ```

3. Run the console:

    ```bash
    ./console.py
    ```

4. Start interacting with the shell and managing instances.

### Commands
- `create`: Create a new instance of a specified class and save it.
- `show`: Display the string representation of an instance based on the class name and ID.
- `destroy`: Delete an instance based on the class name and ID.
- `all`: Print string representations of all instances based on the class name.
- `update`: Update an instance based on the class name and ID by adding or updating attributes.

## Classes
- `BaseModel`: The base model class with common attributes and methods - serves as a super class for other classes
- `User`: A class representing a user with attributes like email, password, first name, and last name.
- `State`: A class representing a state with attributes such as name
- `City`: A class representing a City with attributes such as name, `state_id`
- `Amenity`: A class representing an amenity with attributes such as name
- `Place`: A class representing a place with attributes such as `city_id`, `user_id`, name, description, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, latitude, longitude, `amenity_ids`
- `Review`: A class representing a review with attributes such as `place_id`, `user_id`, and text.

## Contributors
- Thomas Sarfo
- Kabute Grace
