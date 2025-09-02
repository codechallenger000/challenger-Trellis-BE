from django.urls import path
from .views import NumberToEnglishAPIView

urlpatterns = [
    path('num_to_english/', NumberToEnglishAPIView.as_view(), name="num_to_english"),
]
