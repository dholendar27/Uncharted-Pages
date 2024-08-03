# Uncharted-Pages

This is a simple blog application built using Flask, where users can sign up, log in, create blog posts using Markdown, view their posts, and explore posts from other users. The application is designed to be user-friendly, with full support for Markdown formatting, making it easy to create and view rich-text content.

## Table of Contents

- [Project Features](#project-features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Folder Structure](#folder-structure)

## Project Features

- **User Authentication**: Users can sign up and log in using secure authentication with Flask-Login.
- **Create Posts**: Authenticated users can create new blog posts using Markdown, allowing for rich-text content.
- **View Posts**: Users can view their posts and explore posts from other users.
- **Dynamic Content**: Posts are dynamically rendered, including images, titles, descriptions, and Markdown content.
- **Responsive Design**: The application is designed to be responsive and mobile-friendly.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Flask-Login**: A Flask extension that provides session management for Flask.
- **SQLite**: A lightweight disk-based database.
- **Jinja2**: A templating engine for Python used to generate HTML dynamically.
- **Marked.js**: A JavaScript library for parsing Markdown and converting it to HTML.
- **Bootstrap**: A front-end framework for responsive and mobile-first web development.
- **HTML/CSS/JavaScript**: Standard web technologies for building user interfaces.

## Setup Instructions

### Prerequisites

- Python 3.x
- Virtual Environment (recommended)
- SQLite (or any preferred database)

### Installation

1. **Clone the repository**

   ```bash
   [git clone https://github.com/dholendar27/Uncharted-Pages.git](https://github.com/dholendar27/Uncharted-Pages.git)
   cd Uncharted-Pages
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. **Run the application**

   ```bash
   flask run
   ```

7. **Open your web browser**

   Navigate to `http://127.0.0.1:5000` to access the blog application.

## Usage

### User Authentication

- **Sign Up**: New users can register by providing a username, email, and password.
- **Log In**: Registered users can log in with their credentials to access their dashboard.

### Creating Posts

- **Markdown Editor**: Users can create posts using a Markdown editor to format text.
- **Image Upload**: Users can upload images to include in their posts.

### Viewing Posts

- **My Posts**: Users can view and manage their posts in their profile.
- **Explore**: Users can browse posts made by other users.

## Folder Structure

```
Uncharted pages
|____ app.py
|____ main.py
|____ blog.py
|____ auth.py
|____ models.py
|____ README.md
|____ static
| |____ css
| | |____ style.css
| |____ images
| | |____ right-arrow.png
|____ instance
| |____ blog.db
| |____ blog.db-x-post-1-image.png
|____ templates
| |____ base.html
| |____ login.html
| |____ signup.html
| |____ blog
| | |____ home.html
| | |____ posts.html
| | |____ blogpost.html
| | |____ view_post.html
| | |____ navbase.html

```
