from django.urls import path

from . import views

app_name = 'entry'
urlpatterns = [
    path('', views.TeamNumberList.as_view(), name='team_list'),
    path('<slug:pk>/auto/', views.Auto.as_view(), name='auto'),
    path('<slug:pk>/auto/check/', views.validate_match, name='validate_match'),
    path('<slug:pk>/auto/submit/', views.write_auto, name='write_auto'),
    path('<slug:pk>/teleop/<slug:match_number>', views.Teleop.as_view(), name='teleop'),
    path('<slug:pk>/teleop/', views.write_teleop, name='write_teleop'),
    path('visual/', views.Visualize.as_view(), name='view_matches'),
    path('visual/update/', views.update_graph, name='update_graph'),
    path('download', views.download, name='download_event'),
    path('schedule/', views.ScheduleView.as_view(), name='team_list')
]