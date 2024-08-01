from django.urls import path
from .views import generation_view, json_generation_view, json_response_view

app_name = 'ONsettings'

urlpatterns = [
    path('', generation_view),
    path('json/', json_generation_view),
    path('jsonresp/', json_response_view),

]

