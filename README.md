# Todo API 📝

A modern, professional FastAPI-based Todo application with user management and post functionality.

## 🚀 Features

- **User Management**: Create, read, and delete users
- **Post Management**: Create, read, and delete posts
- **Foreign Key Relationships**: Posts are linked to users
- **Data Validation**: Input validation using Pydantic serializers
- **Professional Structure**: Modular codebase following corporate standards
- **MySQL Database**: Robust database integration with SQLAlchemy
- **Interactive API Docs**: Auto-generated Swagger documentation

## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM)
- **MySQL**: Relational database
- **Pydantic**: Data validation using Python type hints
- **Uvicorn**: ASGI server for running the application

## 📁 Project Structure

```
Todo/
├── db/
│   └── config.py          # Database configuration
├── router/
│   ├── user.py           # User-related endpoints
│   └── post.py           # Post-related endpoints
├── models.py             # Database models
├── serializers.py        # Input/Output data serializers
├── main.py              # Main application entry point
├── requirements.txt     # Python dependencies
└── .gitignore          # Git ignore rules
```

## 🚦 Getting Started

### Prerequisites

- Python 3.8+
- MySQL Server
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd Todo
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up database**

   - Create a MySQL database named `todo`
   - Update database credentials in `db/config.py`

5. **Run the application**

   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API**
   - API Documentation: http://127.0.0.1:8000/docs
   - Alternative Docs: http://127.0.0.1:8000/redoc
   - API Base URL: http://127.0.0.1:8000

## 📚 API Endpoints

### Users

- `POST /users/` - Create a new user
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get user by ID
- `DELETE /users/{user_id}` - Delete user

### Posts

- `POST /posts/` - Create a new post
- `GET /posts/` - Get all posts
- `GET /posts/{post_id}` - Get post by ID
- `DELETE /posts/{post_id}` - Delete post

## 💡 Usage Examples

### Create a User

```bash
curl -X POST "http://127.0.0.1:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"username": "johndoe"}'
```

### Create a Post

```bash
curl -X POST "http://127.0.0.1:8000/posts/" \
     -H "Content-Type: application/json" \
     -d '{"title": "My First Post", "content": "Hello World!", "user_Id": 1}'
```

## 🏗️ Database Schema

### Users Table

- `id` (Primary Key)
- `username` (Unique)

### Posts Table

- `id` (Primary Key)
- `title`
- `content`
- `user_Id` (Foreign Key → users.id)

## 🔧 Configuration

Database configuration is handled in `db/config.py`:

```python
DB_URL = "mysql+pymysql://root:password@localhost:3306/todo"
```

## 🧪 Development

### Running in Development Mode

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Project Features

- **Modular Architecture**: Clean separation of concerns
- **Input Validation**: Automatic request validation
- **Error Handling**: Proper HTTP status codes and error messages
- **Foreign Key Constraints**: Data integrity enforcement
- **Professional Serializers**: Centralized data models

## 📝 API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

These provide interactive documentation where you can test all endpoints directly from your browser.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Built with ❤️ using FastAPI and modern Python practices.

---

**Happy Coding! 🚀**
