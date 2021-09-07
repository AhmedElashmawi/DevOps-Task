from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='all-meetups'), # our-domain.com/meetups'/' to avoid 404 er
    path('addJobs/',views.addJobs,name='addJobs'), # our-domain.com/meetups/ <dynamic-path-segment>
    path('addEmployee/',views.addEmployee,name='addEmployee'), # our-domain.com/meetups/ <dynamic-path-segment>
    path('updateEmployee/<int:pk>/',views.updateEmployee,name='updateEmployee'), # our-domain.com/meetups/ <dynamic-path-segment>
    path('updateJobs/<int:pk>/',views.updateJobs,name='updateJobs'), # our-domain.com/meetups/ <dynamic-path-segment>
    path('deleteJobs/<int:pk>/',views.deleteJobs,name='deleteJobs'), # our-domain.com/meetups/ <dynamic-path-segment>
    path('deleteEmployee/<int:pk>/',views.deleteEmployee,name='deleteJobs'), # our-domain.com/meetups/ <dynamic-path-segment>
    path('<slug:meetup_slug>/registration-sucess/',views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>/',views.meetup_details,name='meetup-detail'), # our-domain.com/meetups/ <dynamic-path-segment>
]