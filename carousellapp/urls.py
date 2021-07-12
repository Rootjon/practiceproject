from django.urls import path , include
from .import views
app_name = 'carousellapp'
urlpatterns =[
    path ('',views.slider,name='slider')
]