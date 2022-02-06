
from django.urls import path
from .views import homepage1, mealspage, contact_us, about_us, ReserveRetrieve, test, index
from .views import login_view, register_view, logout_view

app_name = "karsoft"

urlpatterns = [
    path('home1/', homepage1),
    path('meals/', mealspage),
    path('contact/', contact_us),
    path('about/', about_us),
    path('test/', test),
    path('index/', index),
    path('ReserveRetrieve/', ReserveRetrieve),

    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view)
    # path('add-reserve/', ReserveCreate,)
]

