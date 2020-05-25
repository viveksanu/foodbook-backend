from django.conf.urls import url 
from part1 import views 
 
urlpatterns = [ 
    url(r'^api/questions$', views.list_question,name='list_question'),
    url(r'^api/answers$', views.save_answer,name='save_answer')
]