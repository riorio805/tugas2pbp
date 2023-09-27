from django.urls import path, include, re_path, register_converter
from main.views import *
from main.converters import *

register_converter(NegativeIntConverter, 'negint')

app_name = 'main'

urlpatterns = [
    path('main/', show_main, name="show_main"),
    path('main/<int:item_count>', show_main, name="show_main"),
    path('', show_readme, name="show_readme"),
    path('archive/<str:file>', show_archive, name="show_archive"),
    path('statics/', show_statics_list, name="show_statics_list"),
    path('main/create_item', create_item, name="create_item"),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),\
    path('main/change_item', change_item, name="change_item"),
    path('main/change_item/<int:id>&<negint:amount>', change_item, name="change_item"),
    path('main/delete_item', delete_item, name="delete_item"),
    path('main/delete_item/<int:id>', delete_item, name="delete_item"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
]