from django.urls import path
from learning_temp_app import views

app_name = 'learning_temp_app'

urlpatterns = [
    # path('index/',views.index,name='index'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]