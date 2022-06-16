from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from petocare import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login as auth_login, logout

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "main_app/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "main_app/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        # subject = "Welcome to PetoCare!!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to PetoCare!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nTeam PetoCare"        
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        # current_site = get_current_site(request)
        # email_subject = "Confirm your Email at PetoCare Login!!"
        # message2 = render_to_string('email_confirmation.html',{
            
        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        # subject,
        # message,
        # settings.EMAIL_HOST_USER,
        # [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()
        
        return redirect('login')
        
        
    return render(request, "main_app/signup.html")
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
def trainer_book(request):
    return render (request, "main_app/trainerbook.html")
def groomer_book(request):
    return render (request, "main_app/groomerbook.html")
def training(request):
    return render (request, "main_app/training.html")
def grooming(request):
    return render (request, "main_app/grooming.html")
def user_logout(request):
    
    messages.success(request, "You are logged out")
    logout(request)
    return redirect('home')
