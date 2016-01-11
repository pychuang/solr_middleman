from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.QueryView.as_view()),
]
