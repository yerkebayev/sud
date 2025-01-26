from django.urls import path

from .views import CombinedOzSearchView, LastOzNNewsAPIView, ConnectionOzListAPIView, GovernanceOzListAPIView, \
    ResolutionOzListAPIView, ProvisionOzListAPIView, NewsOzListAPIView, GalleryOzListAPIView

urlpatterns = [
    path('api_oz/search/', CombinedOzSearchView.as_view(), name='combined-search'),
    path('api_oz/connections/', ConnectionOzListAPIView.as_view(), name='connection-list'),
    path('api_oz/news/last/<int:n>/', LastOzNNewsAPIView.as_view(), name='last-n-news'),
    path('api_oz/news/', NewsOzListAPIView.as_view(), name='news-list'),
    path('api_oz/gallery/', GalleryOzListAPIView.as_view(), name='gallery-list'),
    path('api_oz/governance/', GovernanceOzListAPIView.as_view(), name='governance-list'),
    path('api_oz/resolutions/', ResolutionOzListAPIView.as_view(), name='resolution-list'),
    path('api_oz/provisions/', ProvisionOzListAPIView.as_view(), name='provision-list'),
]
