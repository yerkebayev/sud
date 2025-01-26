from django.urls import path
from .views import CombinedRuSearchView, ConnectionRuListAPIView, LastRuNNewsAPIView, GovernanceRuListAPIView, \
    ResolutionRuListAPIView, ProvisionRuListAPIView, NewsRuListAPIView, GalleryRuListAPIView

urlpatterns = [
    path('api_ru/search/', CombinedRuSearchView.as_view(), name='combined-search'),
    path('api_ru/connections/', ConnectionRuListAPIView.as_view(), name='connection-list'),
    path('api_ru/news/last/<int:n>/', LastRuNNewsAPIView.as_view(), name='last-n-news'),
    path('api_ru/news/', NewsRuListAPIView.as_view(), name='news-list'),
    path('api_ru/gallery/', GalleryRuListAPIView.as_view(), name='gallery-list'),
    path('api_ru/governance/', GovernanceRuListAPIView.as_view(), name='governance-list'),
    path('api_ru/resolutions/', ResolutionRuListAPIView.as_view(), name='resolution-list'),
    path('api_ru/provisions/', ProvisionRuListAPIView.as_view(), name='provision-list'),
]
