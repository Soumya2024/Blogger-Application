# Mini Blogging

A simplified backend API using Python Flask to simulate a basic blogging platform.

## Features

- User authentication (signup and login with JWT tokens)
- Blog post management (create, read, update, delete)
- Comment functionality
- SQLite database with Flask-SQLAlchemy

## Getting Started

### Prerequisites

- Python 3.7+
- Poetry

### Installation

1. Clone the repository or download the code

2. Create a virtual environment:
   ```
   Poetry Init
   ```

3. Activate the virtual environment:
   ```
   poetry shell
   poetry update
   ```

4. Install the required packages:
   ```
   poetry add packages
   ```

5. Configure the environment variables by creating a `.env` file with:
   ```
   SECRET_KEY=secret key
   DATABASE_URI=sqlite:///blog.db
   ```

6. Run the application:
   ```
   python app.py
   ```

The API will be available at `http://localhost:5000`.

## API Endpoints

### Authentication

- **POST** `/api/signup` - Register a new user
- 
- **POST** `/api/login` - Login and get an access token

### Blog Posts

- **GET** `/api/posts` - Get all blog posts (public)

- **GET** `/api/posts/<post_id>` - Get a specific blog post (public)

- **POST** `/api/posts` - Create a new blog post (requires authentication)

- **PUT** `/api/posts/<post_id>` - Update a blog post (requires authentication, only the author can update)

- **DELETE** `/api/posts/<post_id>` - Delete a blog post (requires authentication, only the author can delete)
  
### Comments

- **POST** `/api/posts/<post_id>/comments` - Add a comment to a blog post (public)

- **GET** `/api/posts/<post_id>/comments` - Get all comments for a specific blog post (public)
