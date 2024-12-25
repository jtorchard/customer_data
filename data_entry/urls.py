from django.urls import path

from . import views

app_name = "data-entry"
urlpatterns = [
    # ex: /data-entry/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /data-entry/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:customer_id>/vote/", views.vote, name="vote"),
]
