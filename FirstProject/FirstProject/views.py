from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def about(request):
    return HttpResponse(
        """ <h1>About Us</h1>
            <p>This is the About page.</p>
            <h2>Our Mission</h2>
            <p>To provide quality education to all.</p>
            <input style="width: 100%; padding: 10px;font-weight: bold;" type="text" placeholder="Your feedback">
            <button style="padding: 10px 20px; font-weight: bold; display: flex; width: 10%; background-color: #007bff; justify-content: center; align-items: center; color: white; border: none; border-radius: 5px; margin: 10px 0;">Submit</button>
        """
    )

def contact(request):
    return HttpResponse("This is the Contact page.")
