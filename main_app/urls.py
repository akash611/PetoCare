from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('services/', views.services, name="services"),
    path('about/',views.about,name="about"),
    path('login/',views.login, name="login"),
    path('signup/',views.signup, name="signup"),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('vet/login/',views.vet_login, name="vet_login"),
    path('trainer/login/',views.trainer_login, name="trainer_login"),
    path('forgotpassword/', views.forgot_pass, name="forgot_pass"),
    path('join/vet/', views.vet_register, name="vet_register"),


    path('join/trainer/', views.trainer_register, name="trainer_register"),

    path('services/vet/booking/<int:vet_id>',views.vet_book, name="vet_book"),
    path('services/grooming/',views.grooming, name="grooming"),
    path('services/training/',views.training, name="training"),
    path('services/grooming/booking/<int:grooming_id>',views.groomer_book, name="groomer_book"),
    path('services/training/booking/<int:training_id>',views.trainer_book, name="trainer_book"),
    path('services/vet',views.vet,name="vet"),
    path('services/orders',views.orders, name="orders"),
    path('logout/',views.user_logout, name="logout"),




    



]