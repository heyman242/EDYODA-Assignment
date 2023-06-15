from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import NewUser


def login_view(request):
    if request.method == 'POST':
        email_id = request.POST['email_id']
        password = request.POST['password']
        user = authenticate(request, username=email_id, password=password)
        if user is not None and hasattr(user, 'newuser'):
            login(request, user)
            return redirect('main')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_id = request.POST.get('email_id')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})

        # Create user instance
        user = User.objects.create_user(username=email_id, password=password1)
        user.save()

        # Generate a unique ID for the new user
        new_user_id = generate_unique_id()

        # Create NewUser instance with the generated ID
        new_user = NewUser(user=user, id=new_user_id, email_id=email_id, name=name)
        new_user.save()

        return redirect('MelodyShare:login')
    else:
        return render(request, 'signup.html')

def generate_unique_id():
    last_used_id = NewUser.objects.last().id
    if last_used_id:
        last_id_number = int(last_used_id)
        new_id_number = last_id_number + 1
    else:
        new_id_number = 1000

    # Generate the new ID by converting it back to a string
    new_id = str(new_id_number)

    return new_id

