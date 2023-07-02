# Book Exchange Application - (T2A2) API Webserver Project

# [My Project Management (Trello)](https://trello.com/b/bmhf0mvA/api-webserver)

# Installation

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

Next we will install our dependencies.

    python3 -m pip install -r requirements.txt

Now we will create and seed the database.

    flask db create
    flask db seed

Now run the Flask app.

    flask run

## **R1	Identification of the problem you are trying to solve by building this particular app.**

As an avid reader I've always cherished the joy of flipping through pages, getting lost in various worlds and learning about the world around me. However, I can't help but acknowledge the challenges associated with this passion, chief among which is accessibility. 

Sometimes visiting a traditional library becomes a tough task due to various constraints (location, time etc.), and an option to conveniently borrow physical books as opposed to simply purchasing them would be great. More importantly, the range of books available at any given library may not align with any one individual's diverse and ever-evolving reading interests.

Reflecting on this, I've realised that there are mini-libraries tucked away in homes all across every city. People's personal book collections often house a diverse range of books, from bestsellers and classics to the more obscure, under-the-radar literature. This is all the more so for non-fiction texts, some of which may be obscure and hard to source, in my experience. 

Each bookshelf is a unique reflection of the reader's journey and taste. These collections are of great benefit to the wider community of readers, and indeed I have seen an analog version of this where people construct bookshelf cabinets along their fence with a sign to “take a book and leave a book” as such. This realisation gave rise to the idea of my current project - a platform designed to bridge this gap, making these personal book collections accessible to everyone.

## **R2	Why is it a problem that needs solving?**

By building this app, I aim to solve the problem of limited accessibility to diverse reading materials in a more decentralised manner, fostering an engaged, interactive community of book lovers. Traditional avenues for accessing books like libraries, bookstores, and digital platforms, certainly have their merits, but they also come with inherent limitations.

I think the first is physical space, bookstores and libraries can only house a certain number of books. This can result in both a lack of diversity and availability, especially when it comes to less mainstream literature. For example, books from indie authors, foreign language works, or region-specific literature may not always be readily available in these traditional avenues.

Secondly, libraries operate on a lending model that often includes strict time limits. If a reader needs more time with a book or needs to revisit it later, they might find the book has been returned to the circulation and isn't immediately available.

Bookstores, on the other hand, require you to purchase books. While this isn't necessarily a problem for everyone, it does pose a barrier for those who can't afford to continually buy new books, especially considering the often high prices of newly released titles or special editions.

Lastly, while digital platforms like Audible provide a great service, they don't cater to those who prefer physical books. While I personally do consume audiobooks, many readers enjoy the tactile experience of reading a physical book, the feel of the pages, the smell of the book, the satisfaction of physically turning a page, something which digital platforms can't replicate.

Through this app, users can share their personal libraries, making their books available to others in their vicinity. Similarly, they can access books from other users' collections, and request them.  It can provide a more diverse range of books in any sizable city, foster a community spirit among readers, and, importantly, ensures that the joy of reading remains accessible to everyone. This platform not only solves the issue of accessibility but also fosters a community of like-minded readers, making the world a bigger place for these people, and also fostering connection and community, something I believe is all the more important these days. The joy of reading should be more readily accessible to everyone.


## **R3	Why have you chosen this database system. What are the drawbacks compared to others?**

I have chosen the relational database management system PostgreSQL for my application. Postgres has its advantages and disadvantages, with some of the generic benefits like ACID compliance and JSON support definitely being handy. However I think it is an excellent choice for my application due to the nature of my data. 

### **Relational model benefits**

The entities in my application (users, books, locations, transactions) have clear relationships and constraints which can be efficiently represented and managed with a relational database. My data being highly structured means it can naturally be organised in tables and columns (Dhruv, 2019). The ACID compliance of PostgreSQL also ensures data integrity for transactions, which is critical for my application (Cloud Infrastructure Services, 2022).

### **Transactions**

Postgres is ACID compliant, with its atomicity meaning it supports transactions, which provide a safe way to handle multiple database operations at once. For example when a user requests a book, the program might need to update both the user and book tables simultaneously (brandur.org, n.d.). Transactions allow me to ensure that either both updates succeed, or, if there's an error, neither change is committed, keeping my data consistent.

### **Drawbacks**

If my application grows, scalability could become a concern, and one of PostgreSQL's limitations is the relative lack of support for horiozntal scaling (Rathbone, 2023). Postgres is also not as user friendly as some other database systems, which poses a steeper learning curve for me, but also will possibly add to development time if I were to collaborate with other developers too. 

## **R4	Identify and discuss the key functionalities and benefits of an ORM**

An object-relational mapper (ORM) provides a way for programmers to interact with relational databases without having to write structured query language (SQL). This is done with an object-oriented language like Python. It can use models (classes) to serve as an abstraction for our tables in the database, along with being able to design schemas and set rules for our table data. Consider we wanted to grab our user attributes for a specific user using an SQL query:

    "SELECT id, username, email, location FROM users WHERE id = 1"

Contrast this to:

    users.GetById(1)

This is a simple example, and often the python statements will not be so much shorter than the AQL query, but they are much easier to understand, read, and reason about for the python programmer who isn’t also very proficient in SQL.

**Benefits of an ORM** (Contributor, 2022)

- Database Independence: the abstraction layer ORMs provide between the application code and the database makes the application database agnostic, meaning it can be switched to another relational database management system with minimal changes to the code.
  - This has the added benefit of allowing developers to work in programming languages they are comfortable with, as not all developers may be proficient in something like SQL.
- ORMs lead to cleaner and more maintainable code 
- ORMs often have protections against SQL injection attacks built-in
- ORMs can keep track of changes to the model classes and map them to our database structure, in a process known as Migration


## **R5	Document all endpoints for your API**

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

- Description: 
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
- Description: 
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
- Description: 
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
- Description: 
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
- Description: 
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
- Description: 
- Request body: None

Request response:

![Get specific book](/docs/get-specific-book.png)

### Search for a book via title/author

**/books/search**

**Methods: GET**

- Arguments: Search query
- Authentication: None
- Token: None
- Identifier: None
- Description: 
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
- Description: 
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
- Description: 
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
- Description: 
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
- Description: 
- Request body: None
- Request response:

![Update book](/docs/updated-book-details.png)


### **Transaction Routes**

### **Get all transactions**
**/transactions**

**Methods: GET**

- Arguments: None
- Authentication: None
- Token: None
- Identifier: None
- Request body: None
- Description: 
- Request reponse:

![Get all transactions](/docs/get-all-transactions.png)

### **Get all transactions for the logged-in user**
**/transactions/user**

**Methods: GET**

- Arguments: None
- Authentication: JWT required
- Token: JWT generated
- Identifier: user_id
- Description: 
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
- Description: 

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
- Description: 
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
- Description: 

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
- Description: 

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



## **R6	An ERD for your app**

![Application entity relationship diagram](/docs/erd.png)

## **R7	Detail any third party services that your app will use**

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

## **R8	Describe your projects models in terms of the relationships they have with each other**

### **Models**

#### Relationships

**User:** A user can have multiple books through the *'user_books'* relationship and can also make multiple transaction requests through *‘requested_transactions’* and *‘provided_transactions’*. Users also belong to a location through the ‘location’ relationship.

**Book:** Each book belongs to a user through *‘owner’* relationship. Each book can also be involved in multiple transaction requests through *‘requested_transactions’* and *‘provided_transactions’*.

**Transaction:** Each transaction involves two users – one who requests the book, through the *‘requester’* relationship, and one who provides the book, through the *‘provider’* relationship. It also involves two books - one which is requested (through the *‘requested_book’* relationship), and one which is provided (through the *‘provided_book’* relationship).

**Location:** Each location can have multiple users associated with it through its *‘users’* relationship.


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




## **R9	Discuss the database relations to be implemented in your application**

My application will primarily involve the management of a book sharing system. Users will be adding, deleting, editing, requesting and providing books. Users will therefore be interacting with books they own, as well as be requesting books owned by others. Transactions, which encapsulate these interactions, will need to reference both the requester and provider of books. 

My database relationships therefore can be established as follows: 

- **Users** are tied to books in a *one-to-many* relationship (one user can own multiple books) 
- **Locations** and users in a *one-to-many* relationship (one location can have multiple users)
- Although the **Transaction** model is managing what can be considered to a many to many relationship between the User and Book models, each of the actual ‘transactions’ involve two users and two books, technically forming a series of *one-to-one* relationships
  - A single user can request multiple books, and a single book can be requested multiple times by multiple users
  - Each transaction (row) in the transaction table is a one to one relationship however, one specific user requesting one specific book

I thought about modelling the ‘transaction’ more holistically, by also modelling a ‘complete’ transaction, as opposed to considering both the ‘requesting’ and ‘providing’ of books by users as transactions. My current design does not capture the full exchange process within a single transaction, which could be a potential downside if the scope of my application ever expanded as such that having an entire exchange encapsulated would be important. However, I went with my ‘requester’ and ‘provider’ transaction model for several reasons:

- **Simplicity:** Each transaction is tied to a single user and a single book. This is straightforward and makes it easy to add new transactions, look up requests by a user or requests for a book.
- **Clarity of state:** A transaction clearly represents a state in the system. It's either a request or a provision. This makes it easy to query the system's state, for example, to find all ‘outstanding requests’.
- **Flexibility for Users:** By treating requests and provisions as separate transactions, my design gives users flexibility to manage their interactions. A user could decide to withdraw a request before it is fulfilled, or decide not to fulfil a request, without affecting other parts of the system.
- **Scalability:** The simplicity of the model allows it to easily accommodate growth in the number of users, books, and transactions. Each new transaction is just a new row in the database, regardless of the number of users or books.

## **R10	Describe the way tasks are allocated and tracked in your project**

### **Project Management**

#### **Planning**

Project planning was done with an implementation planning model which I have come to rely on for projects. It involves:
1. Deciding on application functionality/project scope
2. Deciding which data structures/libraries/entities will be involved
3. Creating a flow diagram for functionality, in this case an ERD
4. Setting deadlines and prioritising tasks
5. Creating a checklist for application funcitonality and final deliverable

Below is my implementation plan for this project.
![Implementation Plan](/docs/implementation-plan.png)


#### **Priorities and Deadlines**
In terms of deadlines and priorities, my highest priority tasks were in order;

1. Decide on scope of my application
2. Develop Implementation Plan
3. Build models and authentication routes
4. Build application endpoints and test endpoints
5. Complete documentation


Doing the above things allows me to complete the core functionality of my application while meeting the minimum requirements for the product. I generally complete all projects with the same workflow, in the order of tasks of greatest complexity to least complexity. Tasks are therefore 'prioritised' by my perceived complexity of delivering, which involves both development time and the number of components which rely on said task.

Tasks which were of greatest priority were performed first. As usual deadlines for the most important tasks were first to ensure as much time as possible could be allocated to them should difficulties arise.

![Deliverables Deadlines](/docs/first-deliverables.png)

As can be seen above, the order in which tasks were completed mapped to their deadlines ie. planning --> erd design --> modelling --> blueprints.

#### **Tracking**

Tracking was straight forward, I would return to my trello board each day to see what upcoming deadlines I have, and work on those deliverables, moving them from the 'To do' column to 'Doing' and then once completed, moving them to the 'Done' column. Below are a couple of examples.

**Day 3**
![Day 3](/docs/day3.png)

**Day 4**
![Day 4](/docs/day4.png)

As can be noted, the colour coding of orange for approaching deadline and red for past due tasks is useful visually in keeping track of timelines. I didn't really colour code tasks for this project like in past projects, as individual task deadlines served what is essentially the same purpose.

## References

- ‌Cloud Infrastructure Services. (2022). MySQL vs PostgreSQL - What’s the Difference (Pros and Cons). [online] Available at: https://cloudinfrastructureservices.co.uk/mysql-vs-postgresql/.
- ‌Dhruv, S. (2019). Pros and Cons of using PostgreSQL for Application Development. [online] Aalpha. Available at: https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/.
- brandur.org. (n.d.). How Postgres Makes Transactions Atomic. [online] Available at: https://brandur.org/postgres-atomicity [Accessed 24 Jun. 2023].
- Rathbone, M. (2023). PostgreSQL limitations. [online] Beekeeper Studio. Available at: https://www.beekeeperstudio.io/blog/postgresql-limitations#:~:text=One%20of%20the%20main%20limitations [Accessed 24 Jun. 2023].
- Contributor, S. (2022). Why Do We Need Object-Relational Mapping? [online] Software Reviews, Opinions, and Tips - DNSstuff. Available at: https://www.dnsstuff.com/why-do-we-need-object-relational-mapping.

‌
‌

