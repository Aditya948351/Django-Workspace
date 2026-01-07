# Some Things to Check before Working with Django
<ol>
    <li>Check if Virtual invironment is turned on.</li>
    <li>Ensure u are working on Command Prompt terminal not the Powershell</li>
    <li>First do changes in URLs file then vieews.py file must be made</li>
</ol>


<h1>Django Project Initialization Steps</h1>

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
            <img align="left" width=50% src = "https://github.com/Aditya948351/Django-Workspace/blob/main/Readme-assets/views-basic.png?raw=true" alt="views">
            <img align="right" width=50% src = "https://github.com/Aditya948351/Django-Workspace/blob/main/Readme-assets/urls-basic.png?raw=true" alt="urls">
        </div>
    

# Now let's see how we can make the UI in the Routes we created (So we need HTML CSS for that
<ol type="1">
    <li>create template folder in container (not in the Project directory)</li>
    <li>Notify settings.py that we have made those changes</li>
    <li>in DRIS add this in [] --> <code>DIRS=['templates']</code></li>
    <div>
        <li>in ur function in views.py ass this</li>
        <code>
            def home(request):
                return render(request, 'home.html')
        </code>        
    </div>
    <li>Now Restart the Server once again.</li>
    <li>Lol, Error Received cause u haven't imported render</li>
    <li>So, Now add the Import statement in views.py <br> <p><code>from django.shortcuts import render</code></p></li>
    
</ol>
