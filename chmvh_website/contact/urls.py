from django.conf.urls import url

from contact import views


app_name = "contacts"

urlpatterns = [
    url(r"^$", views.ContactView.as_view(), name="contact"),
    url(r"^thanks/$", views.SuccessView.as_view(), name="success"),
]
