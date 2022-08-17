from django.urls import path
from .views import CookieList, CookieDetail

urlpatterns = [
    path("", CookieList.as_view(), name="cookie_list"),
    path("<int:pk>/", CookieDetail.as_view(), name="cookie_detail"),
]
