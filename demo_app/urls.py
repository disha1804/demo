from django.urls import path
from demo_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("form",views.form,name="form"),
   # path("save_data",views.save_data,name="save_data"),
   # path("save_data1",views.save_data1,name="save_data1"),
   path("save_msg",views.save_msg,name="save_msg"),
]
