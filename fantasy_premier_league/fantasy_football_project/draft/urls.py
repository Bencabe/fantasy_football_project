from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('create_league/', views.create_league, name='create_league'),
    path('change_template/<str:template>',  views.change_template, name='change_template'),
    path('leagues/',  views.leagues, name='leagues'),
    path('change_template_leagues/<str:template>/<str:league>',  views.change_template_leagues, name='change_template_leagues'),
    path('process_join_form/',  views.process_join_form, name='process_join_form'),
    path('leagues/draft_zone/<str:league>/<str:player>',  views.draft_zone, name='draft_zone'),
    path('leagues/check_data/',  views.check_data, name='check_data'),
]