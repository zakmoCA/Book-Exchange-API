# Book Exchange Application - (T2A2) API Webserver Project


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

The entities in my application (users, books, locations, transactions) have clear relationships and constraints which can be efficiently represented and managed with a relational database. My data being highly structured means it can naturally be organised in tables and columns. The ACID compliance of PostgreSQL also ensures data integrity for transactions, which is critical for my application.

### **Transactions**

Postgres is ACID compliant, with its atomicity meaning it supports transactions, which provide a safe way to handle multiple database operations at once. For example when a user requests a book, the program might need to update both the user and book tables simultaneously. Transactions allow me to ensure that either both updates succeed, or, if there's an error, neither change is committed, keeping my data consistent.

### **Drawbacks**

If my application grows, scalability could become a concern. Postgres is also not as user friendly as some other database systems, which poses a steeper learning curve for me, but also will possibly add to development time if I were to collaborate with other developers too. 

## **R4	Identify and discuss the key functionalities and benefits of an ORM**

## **R5	Document all endpoints for your API**

## **R6	An ERD for your app**

## **R7	Detail any third party services that your app will use**



## **R8	Describe your projects models in terms of the relationships they have with each other**

### **Models**

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

Tasks which were of greatest priority were performed first, with orange tags being added to those tags in Trello to denote urgency. As usual deadlines for the most important tasks were first to ensure as much time as possible could be allocated to them should difficulties arise.

#### Tracking




## References
