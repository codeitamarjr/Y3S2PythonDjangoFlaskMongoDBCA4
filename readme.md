# Todo List Web App

This is a simple Todo List Web App designed by Itamar Junior for my BSc in Computing subject Back-End Development.

The app is built with Django and Flask, two popular Python web frameworks, and MongoDB, a NoSQL database that provides great flexibility and scalability.

## Features

- Create, read, update, and delete tasks
- Simple and intuitive user interface
- Mobile-friendly design using Bootstrap
- User authentication with sign-in, sign-up, and log out
- Personalized TODO list for each user
- A profile page that shows the total number of tasks for the logged-in user

## Tech Stack

**Client:** Bootstrap

**Server:** Python, Django and Flask, MongoDB hosted in a shared free server

## Security

To enhance the security of this web application, the following steps were taken:

- [x] Email validation was added to the sign-up form using the email-validator library to ensure that only valid email addresses can be registered.
- [x] Flask-WTForms was used to protect against cross-site request forgery (CSRF) attacks by adding a CSRF token to all forms.
- [x] Passwords are hashed using the sha256 method of the Werkzeug.security library before being stored in the database to protect against unauthorized access.
- [x] The app uses the Flask-Login library to manage user authentication and sessions. This includes protecting against session hijacking and ensuring that only authenticated users can access certain routes.
- [x] The app uses MongoDB's built-in authentication mechanisms to ensure that only authorized users can access the database.

These steps were taken to ensure that the app is secure and that user data is protected from unauthorized access or manipulation.

## How to Use

Clone this repository to your local machine
Install the necessary dependencies with pip install -r
Run the app with python app.py
Open your web browser and navigate to <http://localhost:5000>

## Testing

The app has been tested manually, and the following assertions have been used:

- [x] The app displays the correct number of tasks for each user on the profile page.
- [x] The app only displays the user's tasks on the home page after they have logged in.
- [x] The app successfully creates a new task for the logged-in user and displays it on the TODO page.
- [x] The app allows user to delete their tasks successfully.

The test_todo_list.py script is provided to test the behavior of the todo list application.
To run the tests, use the following command:

```python
python test_todo_list.py
```

Future improvements to the application could include additional testing, such as testing the database connection or testing edge cases. Additional features could also be added, such as email notifications or reminders for tasks.

## Contributions

This project is open to contributions. If you find any bugs or would like to suggest improvements, please submit a pull request or open an issue.

## Screenshots

![App Index/Home](https://github.com/codeitamarjr/Y3S2PythonDjangoFlaskMongoDBCA4/blob/master/screenshots/index.png?raw=true)

![App Login](https://github.com/codeitamarjr/Y3S2PythonDjangoFlaskMongoDBCA4/blob/master/screenshots/login.png?raw=true)

![App Sign-up](https://github.com/codeitamarjr/Y3S2PythonDjangoFlaskMongoDBCA4/blob/master/screenshots/signup.png?raw=true)

![App Todo](https://github.com/codeitamarjr/Y3S2PythonDjangoFlaskMongoDBCA4/blob/master/screenshots/todo.png?raw=true)

![App New Todo](https://github.com/codeitamarjr/Y3S2PythonDjangoFlaskMongoDBCA4/blob/master/screenshots/todo%20new.png?raw=true)

![App Profile](https://github.com/codeitamarjr/Y3S2PythonDjangoFlaskMongoDBCA4/blob/master/screenshots/profile.png?raw=true)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact / Support

If you have any questions or comments about this project, please feel free to contact me trought my GitHub profile.
