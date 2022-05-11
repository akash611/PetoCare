from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, "main_app/index.html")
def gallery(request):
    return render (request, "main_app/gallery.html")
def services(request):
    return render (request, "main_app/services.html")
def about(request):
    return render (request, "main_app/about.html")
def login(request):
    return render (request, "main_app/login.html")
def signup(request):
    return render (request, "main_app/signup.html")
def trainer_login(request):
    return render (request, "main_app/trainer_login.html")
def vet_login(request):
    return render (request, "main_app/vet_login.html")
def forgot_pass(request):
    return render (request, "main_app/forgot_pass.html")
def vet_register(request):
    return render (request, "main_app/vet_register.html")
def trainer_register(request):
    return render (request, "main_app/trainer_register.html")
def vet_book(request):
    return render (request, "main_app/vetbook.html")



