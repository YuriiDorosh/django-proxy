from django.urls import path
from .views import proxy

app_name = "proxy"

urlpatterns = [
    path("<path:url>/", proxy, name="proxy"),
]
