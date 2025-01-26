from django.urls import path
from .views import CombinedSearchView, ConnectionListAPIView, LastNNewsAPIView, GovernanceListAPIView, \
    ResolutionListAPIView, ProvisionListAPIView

urlpatterns = [
    path('api/search/', CombinedSearchView.as_view(), name='combined-search'),
    path('api/connections/', ConnectionListAPIView.as_view(), name='connection-list'),
    path('api/news/last/<int:n>/', LastNNewsAPIView.as_view(), name='last-n-news'),
    path('api/governance/', GovernanceListAPIView.as_view(), name='governance-list'),
    path('api/resolutions/', ResolutionListAPIView.as_view(), name='resolution-list'),
    path('api/provisions/', ProvisionListAPIView.as_view(), name='provision-list'),
]
