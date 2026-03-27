# Django Blog Application

A complete Django blog application with user authentication, CRUD operations for posts, comment functionality, and advanced features like tagging and search.

## Features

### ✅ Task 0: Initial Setup and Project Configuration
- Django project setup with proper structure
- Blog app configuration
- Post model with title, content, published_date, and author fields
- Static files and templates setup
- Database migrations

### ✅ Task 1: User Authentication System
- User registration with email field
- User login/logout functionality
- Profile management (view and edit user details)
- Secure password handling with Django's built-in hashing
- CSRF protection on all forms

### ✅ Task 2: Blog Post Management (CRUD)
- **Create**: Authenticated users can create new posts
- **Read**: All users can view posts (list and detail views)
- **Update**: Only post authors can edit their posts
- **Delete**: Only post authors can delete their posts
- Class-based views for better organization
- Proper permissions and access control

### ✅ Task 3: Comment Functionality
- Users can add comments to blog posts
- Comment authors can edit and delete their comments
- Comments are displayed on post detail pages
- Proper permissions (only comment authors can edit/delete)
- Comment timestamps (created_at and updated_at)

### ✅ Task 4: Advanced Features
- **Tagging System**: Posts can have multiple tags
- **Search Functionality**: Search posts by title, content, or tags
- **Tag Filtering**: View all posts with a specific tag
- **Responsive Design**: Modern, clean UI with CSS styling

## Project Structure

```
django_blog/
├── django_blog/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   ├── migrations/
│   ├── templates/blog/
│   │   ├── base.html
│   │   ├── post_list.html
│   │   ├── post_detail.html
│   │   ├── post_form.html
│   │   ├── post_confirm_delete.html
│   │   ├── comment_form.html
│   │   ├── comment_confirm_delete.html
│   │   ├── search_results.html
│   │   ├── posts_by_tag.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── logout.html
│   │   └── profile.html
│   └── static/blog/
│       ├── style.css
│       └── main.js
├── manage.py
└── db.sqlite3
```

## Models

### Post Model
- `title`: CharField (max_length=200)
- `content`: TextField
- `published_date`: DateTimeField (auto_now_add=True)
- `author`: ForeignKey to User
- `tags`: ManyToManyField to Tag

### Comment Model
- `post`: ForeignKey to Post
- `author`: ForeignKey to User
- `content`: TextField
- `created_at`: DateTimeField (auto_now_add=True)
- `updated_at`: DateTimeField (auto_now=True)

### Tag Model
- `name`: CharField (max_length=50, unique=True)

## URL Patterns

- `/` - Home page (post list)
- `/post/<id>/` - Post detail view
- `/post/new/` - Create new post
- `/post/<id>/edit/` - Edit post
- `/post/<id>/delete/` - Delete post
- `/post/<id>/comment/` - Add comment
- `/comment/<id>/edit/` - Edit comment
- `/comment/<id>/delete/` - Delete comment
- `/tag/<tag_name>/` - Posts by tag
- `/search/` - Search posts
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/profile/` - User profile

## Installation and Setup

1. **Install Django**:
   ```bash
   pip install django
   ```

2. **Navigate to project directory**:
   ```bash
   cd django_blog
   ```

3. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

### For Users
1. **Register**: Create a new account with username, email, and password
2. **Login**: Access your account to create and manage posts
3. **Browse Posts**: View all posts on the home page
4. **Search**: Use the search bar to find posts by title, content, or tags
5. **Filter by Tags**: Click on any tag to see all posts with that tag
6. **Comment**: Add comments to posts (login required)
7. **Manage Profile**: Update your username and email

### For Authors
1. **Create Posts**: Click "New Post" to create a blog post
2. **Add Tags**: Include relevant tags separated by commas
3. **Edit Posts**: Modify your posts using the "Edit Post" button
4. **Delete Posts**: Remove posts you no longer want
5. **Manage Comments**: Edit or delete your own comments

## Security Features

- **CSRF Protection**: All forms include CSRF tokens
- **User Authentication**: Secure login/logout system
- **Permission Checks**: Users can only edit/delete their own content
- **Password Hashing**: Django's built-in secure password handling
- **Input Validation**: Form validation for all user inputs

## Technologies Used

- **Django 5.2.5**: Web framework
- **SQLite**: Database (default)
- **HTML/CSS**: Frontend styling
- **Bootstrap-inspired CSS**: Responsive design
- **Django Templates**: Template engine
- **Django Forms**: Form handling and validation

## Future Enhancements

- User profile pictures
- Post categories
- Rich text editor for post content
- Email notifications for comments
- Social media sharing
- Post drafts and publishing workflow
- Admin panel customization
- API endpoints for mobile apps

## Contributing

This is a learning project. Feel free to fork and experiment with additional features!

## License

This project is for educational purposes as part of the ALX Django Learning Lab.
