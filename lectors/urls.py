from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path("", views.MainPage.as_view(), name="add_review"),
    path("lectors", views.LectorsViews.as_view()),
    path("<slug:slug>/", views.LectorDetailViews.as_view(), name="lector_detail"),
    path("test", views.TestDetailView.as_view(), name="test_detail"),
]

