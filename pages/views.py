from django.shortcuts import render

# Create your views here.

def index(request):
	"""
    Render the index page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: The HTTP response containing the rendered index page.
    :rtype: HttpResponse
    """
	return render(request, 'pages/index.html')

def home(request):
	"""
    Render the home page.

    :param request: The HTTP request.
    :type request: HttpRequest
    :return: The HTTP response containing the rendered home page.
    :rtype: HttpResponse
    """
	return render(request,'pages/home.html')
