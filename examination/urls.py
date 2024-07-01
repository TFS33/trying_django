from django.urls import path

from . import views

app_name = 'examination'

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.persons, name='persons'),
    path('person/<int:pk>/', views.person, name='person'),
    path('person/<int:pk>/delete/', views.person_delete, name='person_delete'),
    path('person/<int:pk>/update/', views.person_update, name='person_update'),
    path('person/<int:pk>/delete_2/', views.person_delete_2, name='person_delete_2'),
    path('person/<int:pk>/update/', views.person_update, name='person_update'),
    path('person/add/', views.person_add, name='person_add'),
    path('person/add_2/', views.add_person_2, name='add_person_2'),
    path('person/add_3/', views.add_person_3, name='add_person_3'),
    path('questions/', views.show_questions, name='show_questions'),
    path('question/<int:pk>/', views.question, name='question'),
    path('question/add/', views.add_question, name='add_question'),
    path('questions/<int:pk>/delete/', views.delete_question, name='delete_question'),
    path('answers/<int:pk>/', views.add_answer, name='add_answer'),
    path('questions/<int:pk_question>/answers/<int:pk_answer>/delete/', views.delete_answer, name='delete_answer'),
    path('questions/<int:pk>/update/', views.update_question, name='update_question'),


]
