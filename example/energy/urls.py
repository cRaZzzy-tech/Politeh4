from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import *


app_name = 'energy'

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', load_files, name='load_files'),
    path('xls/<int:pk>', xls, name='xls'),
    path('xls_tahe/<int:pk>', xls_tahe, name='xls_tahe'),
    path('xls_gps/<int:pk>', xls_gps, name='xls_gps'),
    path('xls_gps_final/<int:pk>', xls_gps_final, name='xls_gps_final'),
    path('load_files_new/', load_files_new, name='load_files_new'),
    path('load_files/', load_files, name='load_files'),
    path('load_gps/', load_gps, name='load_gps'),
    path('search/<int:pk>', search, name='search'),
    path('search_gps/<int:pk>', search_gps, name='search_gps'),
    path('search_gps_load/<int:pk>', search_gps_load, name='search_gps_load'),
    path('search_tahe/<int:pk>', search_tahe, name='search_tahe'),
    path('remove/<int:pk>', remove, name='remove'),
    path('remove_tahe/<int:pk>', remove_tahe, name='remove_tahe'),
    path('remove_gps/<int:pk>', remove_gps, name='remove_gps'),
    path('remove_gpsfile/<int:pk>', remove_gpsfile, name='remove_gpsfile'),
    path('step_1/<int:pk>', step_1, name='step_1'),
    path('step1_copy/<int:pk>', step1_copy, name='step1_copy'),
    path('tahe_copy/<int:pk>', tahe_copy, name='tahe_copy'),
    path('gpsfile_copy/<int:pk>', gpsfile_copy, name='gpsfile_copy'),
    path('gps_copy/<int:pk>', gps_copy, name='gps_copy'),
    path('step_2/<int:pk>', step_2, name='step_2'),
    path('step_gps/<int:pk>', step_gps, name='step_gps'),
    path('step_1_gps/<int:pk>', step_1_gps, name='step_1_gps'),
    path('tahe/', tahe, name='tahe'),
    path('gps/', gps, name='gps'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('post_gps/', CreateGPSPostView.as_view(), name='add_post_gps'),
    path('ajax/ajax_step2', ajax_step2, name='ajax_step2'),
    path('ajax/ajax_gps', ajax_gps, name='ajax_gps'),
    ]





