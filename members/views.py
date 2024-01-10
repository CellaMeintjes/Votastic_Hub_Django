from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    """
    Log in a user.

    If the request method is POST, attempt to authenticate the user using the provided
    username and password. If authentication is successful, log in the user and
    redirect to the 'polls:index' page. If authentication fails, display an error
    message and redirect to the 'login' page.

    If the request method is not POST, render the 'authenticate/login.html' template.

    Args:
        request: The HTTP request.

    Returns:
        A redirect to the appropriate page or a rendered template.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a polls where students can vote.
            return redirect('polls:index')
        else:
            messages.success(request, ("Login failed! Try again."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
    

def logout_user(request):
    """
    Log out the current user.

    Log out the user, display a success message, and redirect to the 'home' page.

    Args:
        request: The HTTP request.

    Returns:
        A redirect to the 'home' page.
    """
    logout(request)
    messages.success(request, ("You are now logged out!"))
    return redirect('home')


def register_user(request):
    """
    Register a new user.

    If the request method is POST, validate the registration form. If the form is valid,
    save the user, log them in, display a success message, and redirect to the
    'polls:index' page.

    If the request method is not POST, render the 'authenticate/register_user.html' template
    with an empty registration form.

    Args:
        request: The HTTP request.

    Returns:
        A redirect to the 'polls:index' page or a rendered template with the registration form.
    """
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful! ")
            return redirect('polls:index')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html',{
        'form':form,
    })
