from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signin/newuser/', views.signin, name='newuser'),
    path('menu/', views.menu, name='menu'),
    path('menu/data/<str:station>/<str:name>/', views.check_data, name='indextag'),
    path('menu/data/<str:station>/<str:name>/<str:type_chart>', views.check_data, name='changechart'),
    path('menu/geolocation/<str:station>/<str:name>', views.check_location, name='location'),
    path('menu/addparam/<str:station>', views.create_parameter, name='addparam'),
    path('menu/delete/station/<int:station_id>', views.delete_station, name='delstation'),
    path('menu/delete/parameter/<int:parameter_id>', views.delete_parameter, name='delstation'),
    path('menu/api/station/<int:station_id>/', views.api_station, name='serialstation'),
    path('menu/api/stations/', views.api_station, name='serialstationall'),
    path('menu/api/parameter/<int:parameter_id>/', views.api_parameter, name='serialparam'),
    path('menu/api/parameters/', views.api_parameter, name='serialparameterall'),
    path('menu/api/values/<int:parameter_id>/', views.api_values, name='serialvalues')
]