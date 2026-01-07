# 🚀 Django Internship Workspace

Welcome to my Django learning repository! This workspace documents my journey and progress during the Django Internship at **Edunet Foundation**. Here, I apply the concepts learned in daily sessions to build practical web applications.

---

## 📚 Course Index & Progress

### 🛠️ Module 1: Environment Setup & Prerequisites
Before diving into code, we established a robust development environment.
- **Python Installation**: Verified Python installation and version.
- **Virtual Environment**: Created and activated a virtual environment to manage dependencies isolated from the system.
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
- **Django Installation**: Installed the Django framework using pip.
  ```bash
  pip install django
  ```

### 🏗️ Module 2: First Project - The Foundation
In this module, we learned the core architecture of a Django project.
- **Project Initialization**: Created the first project using `django-admin startproject`.
- **Project Structure**: Explored `manage.py`, `settings.py`, `urls.py`, and `wsgi.py`.
- **Views & URLs**:
    - Created function-based views in `views.py`.
    - Mapped URLs to views using `path()` in `urls.py`.
- **Templates**:
    - Integrated HTML templates for dynamic rendering.
    - Configured `TEMPLATES` settings.
- **Static Files**:
    - Managed CSS, Images, and JavaScript.
    - Configured `STATIC_URL` and `STATICFILES_DIRS`.
- **Outcome**: A multi-page website with a Home, About, Gallery, and Contact page, featuring a custom UI.

### 🚀 Module 3: Second Project - Expanding Horizons
Building upon the basics, we created a second project to reinforce routing concepts.
- **New Project Setup**: Initialized `SecondProject`.
- **Multiple Views**: Implemented distinct views for different sections.
    - `home`: Welcome to HomePage
    - `contact`: Welcome to ContactsPage
    - `gallery`: Welcome to GalleryPage
    - `about`: Welcome to AboutPage
- **Routing Logic**: Configured clean URL patterns to navigate between these views.

### ☁️ Module 4: Deployment
Learned how to take the project from local development to a live server.
- **Configuration**: Prepared `requirements.txt`, `Procfile`, and `vercel.json`.
- **Production Settings**: Configured `ALLOWED_HOSTS` and `whitenoise` for static file serving.
- **Hosting**: Deployed the application on **Vercel**.

---

## 💻 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Aditya948351/Django-Workspace.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Django-Workspace
    ```
3.  **Create and activate virtual environment:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the server:**
    ```bash
    # For FirstProject
    python manage.py runserver

    # For SecondProject
    cd SecondProject
    python manage.py runserver
    ```

---

*This repository is maintained by **Aditya Patil** as part of the Edunet Internship.*
