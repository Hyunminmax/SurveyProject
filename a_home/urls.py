from django.urls import path
from .views import *

urlpatterns = [
    path('', survey_view, name='survey'),
    path('<int:question_id>/', survey_view, name='survey_view'),
    path('surveydone/', survey_done_view, name='survey_done_view'),
    path('result/', result_view, name='result_view'),
]