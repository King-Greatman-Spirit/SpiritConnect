from django.urls import path
from . import views


urlpatterns = [
    path("", views.organization_worker, name='organization_worker'),
    path('staff_detail/<int:organization_worker_id>/', views.staff_detail, name='staff_detail'),
]
