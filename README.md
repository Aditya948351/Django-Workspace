# Django Internship Course

Welcome to the Django Internship Course. This document serves as a guide and index for the topics covered.

# Index

- [Django Internship Course](#django-internship-course)
- [Index](#index)
- [Prerequisites](#prerequisites)
- [Module 1: Project Initialization](#module-1-project-initialization)
- [Module 2: UI and Templates (FirstProject)](#module-2-ui-and-templates-firstproject)
- [Module 3: Creating Django Apps](#module-3-creating-django-apps)
- [Module 4: Adding CSS and JS](#module-4-adding-css-and-js)
- [Module 5 : Installing Bootstrap on Django Project.](#module-5--installing-bootstrap-on-django-project)
- [Module 6 : SQL installing.](#module-6--sql-installing)
- [Module 7: Deployment to Vercel](#module-7-deployment-to-vercel)
- [Module 8: Offline Bootstrap Configuration](#module-8-offline-bootstrap-configuration)
- [Module 9: SMS Project \& StudentApp Initialization](#module-9-sms-project--studentapp-initialization)
- [Module 10: MySQL Database Configuration](#module-10-mysql-database-configuration)
- [Module 11 : opening config with initial.py in migrations](#module-11--opening-config-with-initialpy-in-migrations)

---

# Prerequisites

<ol>
    <li>Check if Virtual invironment is turned on.</li>
    <li>Ensure u are working on Command Prompt terminal not the Powershell</li>
    <li>First do changes in URLs file then vieews.py file must be made</li>
</ol>


# Module 1: Project Initialization

<ol style="color:#fff">
    <li>VS Code >python: create environment     -->> Work on the steps after.</li>
    <li>Virtual Environment will be initiated automatically.</li>
    <li>Activate Virtual Environment.</li>
    <li>Install Django.</li>
    <li>Start Project with Django now.</li>
    <li>
        Start Your Project:<br>
        <code>django-admin startproject <"your project name"></code>
    </li>
    <li>Installing Django: <code>pip install django</code></li>
    <strong>Note: to check if Django is install or not try pip list</strong><br>
    <li>Create views.py inside ur Project Folder (cd ur Project name first)</li>
    <p><strong>views.py includes the /admin /about i.e. routes</strong></p>
    <p>In django we call function first then we create
    <li>We need to import the views.py file first using <code>import views "from <"current directore"></code></li>
    <li>create home function in views.py (already imported views.py in urls) <br>
    <code>from . import views</code>
    </li>
    <li>Add this line in URLs: <br> <code>path('home/', views.home, name='home')</code></li>
    <li>Now create function in views.py otherwise it will give error no Attribute</li>
    <li>so run the server now using cmd terminal command<code>python manage.py runserver </code></li>
    <li>Head to the <code>122.0.0.1:8000</code></li>
    <div width="100%">
        <img width=50% src = "https://github.com/Aditya948351/Django-Workspace/blob/main/Readme-assets/views-basic.png?raw=true" alt="views">
        <img width=50% src = "https://github.com/Aditya948351/Django-Workspace/blob/main/Readme-assets/urls-basic.png?raw=true" alt="urls">
    </div>
</ol>


# Module 2: UI and Templates (FirstProject)

In this module, we enhance the project by adding a user interface using HTML templates and CSS.

<ol type="1">
    <li><strong>Create Template Directory:</strong>
        <ul>
            <li>Create a folder named <code>templates</code> in the root directory (same level as <code>manage.py</code>).</li>
            <li>Inside <code>templates</code>, create HTML files: <code>home.html</code>, <code>about.html</code>, <code>gallery.html</code>, <code>contact.html</code>.</li>
        </ul>
    </li>
    <li><strong>Configure Settings:</strong>
        <ul>
            <li>Open <code>settings.py</code>.</li>
            <li>Find <code>TEMPLATES</code> list and update <code>'DIRS': []</code> to <code>'DIRS': [BASE_DIR / 'templates']</code>.</li>
            <li>Configure Static files:
                <pre><code>STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]</code></pre>
            </li>
        </ul>
    </li>
    <li><strong>Update Views (views.py):</strong>
        <p>Import <code>render</code> and create views for each page.</p>
        <pre><code>from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')</code></pre>
    </li>
    <li><strong>Update URLs (urls.py):</strong>
        <p>Map the new views to URLs.</p>
        <pre><code>from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]</code></pre>
    </li>
    <li><strong>Add Styles (Static Files):</strong>
        <ul>
            <li>Create a <code>static</code> folder in the root directory.</li>
            <li>Create a <code>css</code> folder inside <code>static</code>.</li>
            <li>Add <code>style.css</code> and link it in your HTML files using <code>{% load static %}</code> and <code>&lt;link rel="stylesheet" href="{% static 'css/style.css' %}"&gt;</code>.</li>
        </ul>
    </li>
</ol>


# Module 3: Creating Django Apps 
<ol>
    <li><code>django manage.py startapp AuthorApp</code></li>
    <li></li>
</ol>










# Module 4: Adding CSS and JS 

<li>In Settings.py  add this line below STATIC_URL variable.
<code>
    STATICFILES_DIRS = [
    BASE_DIR / "static",
]
</code>
</li>

<li></li>




# Module 5 : Installing Bootstrap on Django Project.

<ol>
    <li><code>pip install bootstrap</code></li>
    <li>Add to installed Apps</li>
    <li>{% load django_bootstrap_5 %}
    {%  %}
    </li>
    <li></li>
    <li>In installed Apps add this bootstrap_5</li>
</ol>




# Module 6 : SQL installing.

# Module 7: Deployment to Vercel

1.  **Prepare Project**:
    *   Create `vercel.json` in root.
    *   Create `requirements.txt`: `pip freeze > requirements.txt`.
    *   Create `runtime.txt` (e.g., `python-3.9`).
2.  **Configuration**:
    *   Ensure `WSGI` application is correctly pointed in `vercel.json`.
    *   Set `ALLOWED_HOSTS = ['.vercel.app']` in `settings.py`.
3.  **Deploy**:
    *   Push code to GitHub.
    *   Import project in Vercel dashboard.
    *   Deploy.

# Module 8: Offline Bootstrap Configuration

1.  **Download Bootstrap**:
    *   Get compiled CSS and JS files from [getbootstrap.com](https://getbootstrap.com).
2.  **Static Files Setup**:
    *   Place files in `static/css/` and `static/js/`.
    *   Ensure `STATICFILES_DIRS` is configured in `settings.py`.
3.  **Link in Templates**:
    ```html
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    ```

# Module 9: SMS Project & StudentApp Initialization

1.  **Create Project**:
    *   `django-admin startproject SMS`
    *   `cd SMS`
2.  **Create App**:
    *   `python manage.py startapp studentapp`
3.  **Register App**:
    *   Add `'studentapp'` to `INSTALLED_APPS` in `settings.py`.
4.  **Migrate**:
    *   `python manage.py migrate`

# Module 10: MySQL Database Configuration

1.  **Install Driver**:
    *   `pip install mysqlclient`
2.  **Configure Settings**:
    *   Update `DATABASES` in `settings.py`:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'SMS',  # Your DB Name
                'USER': 'root',
                'PASSWORD': 'yourpassword',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
        ```
3.  **Apply Migrations**:
    *   `python manage.py migrate`



# Module 11 : opening config with initial.py in migrations
<li>Added my app in settings.py</li>
<li>Added my app in admin.py</li>


