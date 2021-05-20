from django.urls import path

from api.views import add_view, token, substract_view, multiply_view, divide_view

# substract_view, multiply_view, divide_view

app_name = 'api'

urlpatterns=[
    path('add/', add_view, name='add'),
    path('substract/', substract_view, name='substract'),
    path('get_token/', token, name='get_token'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide')
]