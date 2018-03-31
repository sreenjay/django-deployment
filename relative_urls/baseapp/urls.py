from django.urls import path
from baseapp import views

# TEMPLATES TAGGING
app_name = 'baseapp'

urlpatterns = [
    path('base/', views.base, name="base"),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative')
]
