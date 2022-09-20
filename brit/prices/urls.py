from django.urls import path, include

from . import views


app_name = 'prices'
urlpatterns = [
    path('items', views.items, name='items'),
    path('summary', views.summary, name='summary'),
    path('new_item', views.new_item, name='new_item'),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
