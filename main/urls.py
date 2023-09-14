from django.urls import path, include, re_path
from main.views import *

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
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]