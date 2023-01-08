from django.urls import path, re_path, include
from project.serviceapp import views as serviceView
# from . import set

urlpatterns = [
    re_path(r'^message/', serviceView.messageView, name='massage'),
    re_path(r'^upload/(?P<_id>\d+)/',serviceView.uploadD, name='upload'),
    re_path(r'^status/(?P<_id>\d+)/',serviceView.checkStatus, name='status'),
    re_path(r'^decide/(?P<_id>\d+)/',serviceView.decideView, name='decide'),
    re_path(r'^Admin Status/',serviceView.statusAdmin, name='statusAdmin'),
    re_path(r'^bug/',serviceView.bugView, name='bug'),
]