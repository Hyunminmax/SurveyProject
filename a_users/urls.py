from django.urls import path
from .views import *

urlpatterns = [
    path('', user_view, name='user_view'),
    # path('<int:question_id>/', survey_view, name='survey_view'),
    # path('surveydone/', survey_done_view, name='survey_done_view'),
]