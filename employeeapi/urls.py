from django.urls import path

from employeeapi import views

urlpatterns=[ 
    path("",views.empListAPIView.as_view(),name="todo_list"),
    path("create/", views.empcreateAPIView.as_view(),name="todo_create"),
    path("get/<int:pk>/",views.getAPIVIEW.as_view(),name="get"),
    path("update/<int:pk>/",views.empupdateAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.empdeleteAPIView.as_view(),name="delete_todo"),
    path("get/<str:emp_type>/",views.test,name="test")

]