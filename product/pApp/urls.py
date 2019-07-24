from django.urls import path

from . import views
urlpatterns = [
    path('', views.P_list.as_view(), name='P_list'),
    path('view/<int:pk>', views.P_View.as_view(), name='P_view'),
    path('new', views.P_Create.as_view(), name='P_new'),
    path('edit/<int:pk>', views.P_Update.as_view(), name='P_edit'),
    path('delete/<int:pk>', views.P_Delete.as_view(), name='P_delete'),
    ]