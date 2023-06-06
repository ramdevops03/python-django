# python-django
# Ashok

1. Install Django:
   
   pip install Django
   

2. Create a new Django project by running the following command:
   
   django-admin startproject myproject
   

   This will create a new directory called `myproject` with the basic project structure.

3. Inside the `myproject` directory, create a new Django app:
   
   cd myproject
   python manage.py startapp myapp
   

   This will create a new directory called `myapp` inside the `myproject` directory.
   
4. Replace the content of the `myproject/myapp/views.py` file with the following code:
   python
   from django.shortcuts import render

   def hello(request):
       if request.method == 'POST':
           selected_option = request.POST['dropdown']
           return render(request, 'index.html', {'selected_option': selected_option})
       return render(request, 'index.html')
  
 5. Create a new file called `myproject/myapp/templates/index.html` and add the following content:
   html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Dropdown Example</title>
   </head>
   <body>
       <form method="POST">
           {% csrf_token %}
           <label for="dropdown">Select an option:</label>
           <select id="dropdown" name="dropdown">
               <option value="option1">Option 1</option>
               <option value="option2">Option 2</option>
               <option value="option3">Option 3</option>
           </select>
           <input type="submit" value="Submit">
       </form>
       {% if selected_option %}
           <p>You selected: {{ selected_option }}</p>
       {% endif %}
   </body>
   </html>

6. Open the `myproject/myproject/urls.py` file and replace its content with the following code:
   python
   from django.urls import path
   from myapp.views import hello

   urlpatterns = [
       path('', hello, name='hello'),
   ]

7. Run the Django development server by executing the following command in the `myproject` directory:
   
   python manage.py runserver 0.0.0.0:8081
   

   The Django application will now run on port 8081.

8. Visit `http://localhost:8081/` in your web browser to see the dropdown menu and submit button. After selecting an option and clicking the submit button, the selected option will be displayed on the page.

