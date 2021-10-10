from django.forms.forms import Form
from django.urls import path
from converter import views


urlpatterns=[


    path("number",views.NumberView.as_view(),name="convert")
    
]
