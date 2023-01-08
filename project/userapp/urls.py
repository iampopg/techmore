from django.urls import path, re_path
import re
from project.userapp import views as userview

urlpatterns = [
    re_path(r'^send_mail/', userview.sendWElcomEmail, name="send_mail"),
    re_path(r'^profile/(?P<_id>\d+)/', userview.profileView, name="profile"),
    re_path(r'^update_profile/(?P<id>\d+)/', userview.updateProfile, name='update_profile'),
    re_path(r'^deactivate_profile/(?P<_id>\d+)/', userview.deactivateProfile, name="deactivate_profile"),
    re_path(r'^displayS/', userview.displayStaff, name="displayS"),
    re_path(r'^displayC/', userview.displayCustomer, name="displayC"),
]
