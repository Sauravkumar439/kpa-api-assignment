from django.urls import path
from .views import LoginView, KPAFormDataView

urlpatterns = [
    path('user/login/', LoginView.as_view(), name='user-login'),
    path('kpa/form_data/', KPAFormDataView.as_view(), name='kpa-form-data'),
]
