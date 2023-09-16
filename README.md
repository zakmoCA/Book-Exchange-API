# Book Exchange App API 

## Installation

In your terminal, navigate to the directory you would like to install this project. You can run the following command to clone the project directory locally. 

    git clone https://github.com/zakmoCA/Book-Exchange-API.git

Launch the directory in your code editor.

Once there open a new terminal window and connect to the PostgreSQL database like so.

    psql postgres

Create the database.

    CREATE DATABASE books_exchange;

Connect to database.

    \c books_exchange;

Create admin account.

    CREATE USER books_exchange_dev WITH PASSWORD 'blimeyharry';

Grant privileges.

    GRANT ALL PRIVILEGES ON DATABASE books_exchange to books_exchange_dev;

Next we will create a virtual environment. Open a new terminal window and enter the following.

    python3 -m venv venv
    source venv/bin/activate

Next we will install all our dependencies.

    python3 -m pip install -r requirements.txt

Before we create and seed the database, you'll need to set up some environment variables. In the root directory of the project, create a file called .env. Open this file in a text editor and add the following lines, replacing the placeholders with your actual data:

    DB_URI="postgresql+psycopg2://books_exchange_dev:blimeyharry@localhost:5432/books_exchange"
    JWT_KEY="Your JWT Key Here"


Now we will create and seed the database.

    flask db create
    flask db seed

Now run the Flask app.

    flask run



## Endpoints

### **Auth Routes**

**/auth/users**

**Methods: GET**


![Get Users](/docs/auth-users.png)

**/auth/register**

**Methods: POST**

- Arguments: None
- Authentication: None
- Token: None
- Request body: 
```JSON
{
        "email": "createuser@test.com",
        "username": "dummyuser",
        "password": "dummypass",
        "is_admin": false,
        "location_id": "1"
}
```

- Description: Allows user to sign up with email and password.
- Request response:
```JSON
{
    "email": "createuser@test.com",
    "id": 5,
    "is_admin": false,
    "location_id": "1",
    "username": "dummyuser"
}
```

![Register User](/docs/register-user.png)

**/auth/login**

**Methods: POST**

- Arguments: none
- Authentication: email and password
- Token: JWT generated
- Identifier: email, JWT
- Request body: 
```JSON
{
    "email": "createuser@test.com",
    "password": "dummypass"
}
```
- Description: Allows user to log in
- Request response:
```JSON
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODI5NDkyNywianRpIjoiNmNhZDdiNzYtZmJjOC00ZTQyLTgyM2ItZjRkMjNkZTgwMDMwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NSwibmJmIjoxNjg4Mjk0OTI3LCJleHAiOjE2ODkxNTg5Mjd9.g-n4e1S8cSiAzCQZqJDrAEEojJYASvv-A7-FCJSpBzY",
    "user": {
        "email": "createuser@test.com",
        "id": 5,
        "is_admin": false,
        "location_id": "1",
        "username": "dummyuser"
    }
}
```

![Login endpoint](/docs/login.png)

### **Delete User**
**/auth/`<int:user_id>`**

**Methods: DELETE**

- Arguments: user_id
- Authentication: JWT identity
- Authorization: Account owner or admin
- Token: JWT required
- Identifier: user_id
- Description: Admin can delete a user and a user can delete their account.
- Request body: None

**Request**

    http://127.0.0.1:5000/auth/5
Here we delete the user we created earlier:
```JSON
{
    "email": "createuser@test.com",
    "id": 5,
    "is_admin": false,
    "location_id": "1",
    "username": "dummyuser"
}
```
**Response**

```JSON
{
    "message": "User account 5 deleted"
}
```

![User deleted](/docs/user-deleted.png)




### **User Routes**

### Get all users
**/users**
**Methods: GET**

```JSON
{
    "email": "createuser@test.com",
    "id": 5,
    "is_admin": false,
    "location_id": "1",
    "username": "dummyuser"
}
```

![Get users](/docs/get-users.png)

### Get specific user
**/users/`<int:id>`**
**Methods: GET**

- Arguments: user_id
- Authentication: None
- Token: None
- Identifier: user_id
- Request body: None
- Description: Get list of all users.
- Request response:

![Get specific user](/docs/get-specific-user.png)

### **Book Routes**

### Get all books
**/books**

**Methods: GET**

- Arguments: None
- Authentication: None
- Token: None
- Request body: None
- Description: Get a list of all books.
- Request response:
```JSON
    [
        {
            "author": "Adam Kay",
            "genre": "Memoir",
            "id": 5,
            "owner_id": 4,
            "publication_year": 2017,
            "title": "This Is Goint to Hurt: Secret Diaries of a Junior Doctor"
        },
        {
            "author": "David Deutsch",
            "genre": "Physics, Pop Science",
            "id": 4,
            "owner_id": 3,
            "publication_year": 2011,
            "title": "The Beginning of Infinity"
        },
        {
            "author": "JK Rowling",
            "genre": "Fantasy",
            "id": 1,
            "owner_id": 1,
            "publication_year": 1996,
            "title": "Harry Potter"
        },
        {
            "author": "Vaclav Smil",
            "genre": "History",
            "id": 3,
            "owner_id": 4,
            "publication_year": 2017,
            "title": "Energy and Civilization: A History"
        },
        {
            "author": "Tom Holland",
            "genre": "History",
            "id": 2,
            "owner_id": 2,
            "publication_year": 2019,
            "title": "Dominion"
        }
    ]
```
![]()
### Get a specific book 
**/books/`<int:book_id>`**

**Methods: GET**
- Arguments: book_id
- Authentication: None
- Token: None
- Identifier: book_id
- Description: Get a specific book via its id.
- Request body: None

Request response:

![Get specific book](/docs/get-specific-book.png)

### **Search for a book via title/author**

**/books/search**

**Methods: GET**

- Arguments: Search query
- Authentication: None
- Token: None
- Identifier: None
- Description: Search for a book via the title, or author.
- Request body: None

Request response (search by author):

![Search by author example](/docs/search-by-author.png)

Request response (search by title):

![Search by title example](/docs/search-by-title.png)


### Get all books at a specific locaiton
**/books/location/`<int:location_id>`**

**Methods: GET**

All my books currently have the same location; Melbourne.

- Arguments: location_id
- Authentication: None
- Token: None
- Identifier: location_id
- Description: Get a list of all the books at a given location, as accessed by the location_id
- Request body: None
- Request response:

![Get books by location](/docs/get-books-by-location.png)


### Add a book
**/books**

**Methods: POST**

- Arguments: none
- Authentication: jwt required
- Authorisation: admin or owner required
- Token: None
- Identifier: user_id
- Description: User can add a book to their 'library', and admin can add a book to the books table.
- Request body and response: 

![Create a book](/docs/book-creation.png)


### Delete a book
**/books/`<int:book_id>`**

**Methods: DELETE**

- Arguments: book_id
- Authentication: jwt required
- Authorisation: Must be book owner or admin
- Token: None generated
- Identifier: book_id, user_id
- Description: User can delete their book, and admin can delete a book.
- Request body: None
- Request response:

```JSON
{
    "messsage": "Book deleted"
}
```


### Update a book
**/books/`<int:book_id>`**

**Methods: PUT**

- Arguments: book_id
- Authentication: jwt required
- Authorisation: Must be book owner or admin
- Token: None generated
- Identifier: book_id, user_id
- Description: Update book details.
- Request body: None
- Request response:

![Update book](/docs/updated-book-details.png)


### **Transaction Routes**

Transactions persist in the database even after being cancelled (cancelled request) or declined (declined request).
The 'status' of the transaction is all that is changed.
I want to maintain historical data for the time being, so I can later add functionality for tracking user behaviour, generating reports, and making recommendations.

### **Get all transactions**
**/transactions**

**Methods: GET**

- Arguments: None
- Authentication: None
- Token: None
- Identifier: None
- Request body: None
- Description: Get a list of all current transactions.
- Request reponse:

![Get all transactions](/docs/get-all-transactions.png)

### **Get all transactions for the logged-in user**
**/transactions/user**

**Methods: GET**

- Arguments: None
- Authentication: JWT required
- Token: JWT generated
- Identifier: user_id
- Description: User can view their current transactions
- Request body: None

Logging in as Mr Bigsby

![login](/docs/get-my-transactions-login.png)

Getting Mr Bigsby's transactions.
Request response:

![get user transactions](/docs/get-my-transactions.png)

### Create a new transaction (request a book)
**/transactions/request**

**Methods: POST**

- Arguments: None
- Authentication: JWT required
- Token: None
- Identifier: requester_id, requested_book_id
- Description: User can request a book which exists in the database.

Currently logged in as Ashy Larry, requesting 'This Is Going To Hurt':

- Request body: 

```JSON
{
    "requester_id": 1,
    "requested_book_id": 5
}
```

- Request response:

```JSON
{
    "id": 4,
    "provided_book_id": null,
    "provider_id": null,
    "requested_book_id": 5,
    "requester_id": 1,
    "status": "Requested"
}
```

![Request book](/docs/request-book.png)

### Accept an incoming book request
**/transactions/accept/`<int:transaction_id>`**

**Methods: PUT**

- Arguments: transaction_id
- Authentication: JWT required
- Token: None
- Identifier: transaction_id, user_id
- Description: User can accept an incoming request for one of their books.
- Request body: None

We will now log in as Silky Johnson, the owner of the book which Ashy Larry requested,
and accept the transaction.

**Request response:**

```JSON
{
    "id": 4,
    "provided_book_id": 5,
    "provider_id": 4,
    "requested_book_id": 5,
    "requester_id": 1,
    "status": "Accepted"
}
```



![]()

### Canceling a book request
**/transactions/cancel/`<int:transaction_id>`**

**Methods: PUT**

- Arguments: transaction_id
- Authentication: jwt required
- Token: None generated, jwt identity required
- Identifier: user_id, transaction_id
- Request body: None
- Description: User can cancel an outgoing book request.

While still logged in as Silky Johnson, we will request a book and then cancel the request.

**Request**

```JSON
{
    "requester_id": 4,
    "requested_book_id": 2
}
```

**Request response**

```JSON
{
    "id": 5,
    "provided_book_id": null,
    "provider_id": null,
    "requested_book_id": 2,
    "requester_id": 4,
    "status": "Requested"
}
```

![](/docs/request-to-cancel.png)

**Cancel request**

Request response:

```JSON
{
    "id": 5,
    "provided_book_id": null,
    "provider_id": null,
    "requested_book_id": 2,
    "requester_id": 4,
    "status": "Cancelled"
}
```

![](/docs/cancelled-request.png)

### Declining a book request
**/transactions/decline/`<int:transaction_id>`**

**Methods: PUT**

- Arguments: transaction_id
- Authentication: jwt required
- Token: None generated, jwt identity required
- Identifier: user_id, transaction_id
- Request body: None
- Description: User can decline a request for one of their books.

We will now log in as as the admin to decline an incoming book request for one her books.

**Book**

```JSON
{
    "author": "JK Rowling",
    "genre": "Fantasy",
    "id": 1,
    "owner_id": 1,
    "publication_year": 1996,
    "title": "Harry Potter"
}
```


**Book owner**

```JSON
{
    "email": "admin@test.com",
    "id": 1,
    "is_admin": true,
    "location_id": "1",
    "username": "Admin"
}
```


**Request (transaction)**

```JSON
{
    "id": 1,
    "provided_book_id": null,
    "provider_id": null,
    "requested_book_id": 1,
    "requester_id": 2,
    "status": "Requested"
}
```

**Request response:**

![Declining a book request](/docs/declined-request.png)



## **Third party services**

The third party services involved in this project are:

- SQLAlchemy
- Psycopg2
- Flask-Marshmallow
- Flask-JWT-Extended
- Python-Dotenv

### **SQLAlchemy**

This is a Python SQL toolkit and Object-Relational Mapping system that handles the heavy lifting of my database interactions in my application. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access without having to interact with the databse directly. It allows me to model my application's data as Python classes (models). These models are then used to query the database in a Pythonic way, meaning we can use Python statements instead of writing SQL queries.

### **Psycopg2**

Psycopg2 is the most popular PostgreSQL adapter for the Python programming language. In this application, I'm using it as the underlying engine for SQLAlchemy to communicate with our Postgres database. It enables efficient and safe PostgreSQL operations. It offers many PostgreSQL-specific features.

### **Flask-Marshmallow**

This is an object serialization/deserialization library, and is being used to validate, serialize, and deserialize data going to and from the app's HTTP endpoints. With Flask-Marshmallow, we can easily convert complex data types, such as objects, to Python dictionaries, which can then be converted to JSON format. It also allows me to validate incoming data to make sure it has the right form before using it.

### **Flask-JWT-Extended**

JWT stands for JSON Web Tokens, and is useful for securely transmitting information between parties as a JSON object. My app is using Flask-JWT-Extended for user authentication. When a user logs in with their credentials, they receive a JWT, which they must then include in the headers of their HTTP requests to access protected routes.

### **Python-Dotenv**

This library allows me to utilize a .env file for my environment-specific settings. It's a crucial part of keeping the application secure because it enables me to use environment variables to store sensitive information. This way, I can keep secret keys, database URIs, and other sensitive data out of the codebase. Python-Dotenv reads key-value pairs from a .env file and adds them to the environment variable.


### **User Model**
  ```py

    class User(db.Model):
        __tablename__ = 'users'

        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(100), unique=True)
        email = db.Column(db.String(120), unique=True)
        password = db.Column(db.String(128))
        location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
        is_admin = db.Column(db.Boolean, default=False)


        location = db.relationship('Location', back_populates='users')
        user_books = db.relationship('Book', back_populates='owner', cascade='delete')
        requested_transactions = db.relationship('Transaction', back_populates='requester', foreign_keys='Transaction.requester_id', cascade='delete')
        provided_transactions = db.relationship('Transaction', back_populates='provider', foreign_keys='Transaction.provider_id', cascade='delete')


    class UserSchema(ma.Schema):
        username = fields.String(required=True, validate=Length(min=3, max=100, error='Username must be between 3 and 100 characters long'))
        email = fields.Email(required=True, validate=Email(error='Invalid email address'))
        password = fields.String(load_only=True, required=True, validate=Length(min=6, error='Password must be at least 6 characters long'))
        location_id = fields.String(required=True)

        class Meta:
            fields = ('id', 'username', 'email', 'location_id', 'password', 'is_admin')
            ordered = True
```




### **Book Model**
```py
    class Book(db.Model):
        __tablename__ = 'books'

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(200))
        author = db.Column(db.String(100))
        genre = db.Column(db.String(100), nullable=True)
        publication_year = db.Column(db.Integer, nullable=True)
        owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


        owner = db.relationship('User', back_populates='user_books')
        requested_transactions = db.relationship('Transaction', back_populates='requested_book', foreign_keys='Transaction.requested_book_id', cascade='delete')
        provided_transactions = db.relationship('Transaction', back_populates='provided_book', foreign_keys='Transaction.provided_book_id', cascade='delete')



    class BookSchema(ma.Schema):
        title = fields.String(required=True, validate=Length(min=1, max=200, error='Title must be between 1 and 200 characters long'))
        author = fields.String(required=True, validate=Length(min=1, max=100, error='Author name must be between 1 and 100 characters long'))
        genre = fields.String(validate=Length(max=100, error='Genre must be up to 100 characters long'))
        publication_year = fields.Integer()

        class Meta:
            fields = ('id', 'title', 'author', 'genre', 'publication_year', 'owner_id')
            ordered = True
```




### **Transaction Model**
```py
    VALID_STATUSES = ['Requested', 'Accepted', 'Declined', 'Completed']

    class Transaction(db.Model):
        __tablename__ = 'transactions'

        id = db.Column(db.Integer, primary_key=True)
        requester_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        provider_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
        requested_book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
        provided_book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=True)
        status = db.Column(db.String(30), default='Requested')

        requester = db.relationship('User', back_populates='requested_transactions', foreign_keys=[requester_id])
        provider = db.relationship('User', back_populates='provided_transactions', foreign_keys=[provider_id])
        requested_book = db.relationship('Book', back_populates='requested_transactions', foreign_keys=[requested_book_id])
        provided_book = db.relationship('Book', back_populates='provided_transactions', foreign_keys=[provided_book_id])

    class TransactionSchema(ma.Schema):
        requester_id = fields.Integer(required=True)
        provider_id = fields.Integer(load_default=0)
        requested_book_id = fields.Integer(required=True)
        provided_book_id = fields.Integer(load_default=0)
        status = fields.String(required=True, validate=OneOf(VALID_STATUSES, error=f'Status must be one of: {VALID_STATUSES}'))

        class Meta:
            fields = ('id', 'requester_id', 'provider_id', 'requested_book_id', 'provided_book_id', 'status')
            ordered = True
    
```



### **Location Model**
```py
    class Location(db.Model):
        __tablename__ = 'locations'

        id = db.Column(db.Integer, primary_key=True)
        city = db.Column(db.String(100))
        state = db.Column(db.String(100))
        country = db.Column(db.String(100))

        users = db.relationship('User', back_populates='location')

    class LocationSchema(ma.Schema):
        city = fields.String(required=True, validate=Length(min=1, max=100))
        state = fields.String(required=True, validate=Length(min=1, max=100))
        country = fields.String(required=True, validate=Length(min=1, max=100))
 
        class Meta:
            fields = ('id', 'city', 'state', 'country')
            ordered = True
```



