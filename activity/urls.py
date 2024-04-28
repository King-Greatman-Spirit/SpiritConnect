from django.urls import path
from . import views

urlpatterns = [
    # path('<slug:activity_slug>/', views.activity, name='activity_slug'),
    path('testimony/', views.testimony, name='testimony'),
]
