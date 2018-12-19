from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'your name Sir/Madam ! :)'
    
    args = {'myName': name}
    return render(request, 'accounts/home.html', args)

def loggedin(request):
	return HttpResponse('You have been logged in!')