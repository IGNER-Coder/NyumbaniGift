from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # The <slug:slug> part is the magic variable!
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
]