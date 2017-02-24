from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^make_data/", views.make_data, name="make_data"),
	url(r"^(?P<level>[1-3])/(?P<question>\d+)$", views.levels),
]