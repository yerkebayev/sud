from django.urls import path
from .views import ConnectionRuListAPIView, LastRuNNewsAPIView, GovernanceRuListAPIView, \
    ResolutionRuListAPIView, ProvisionRuListAPIView, ArchiveRuListAPIView, \
    SearchArchiveRuAPIView, ArchiveRuDetailAPIView, NewsRuListAPIView, GalleryRuListAPIView, ArchiveByYearAPIView, \
    ArchiveByYearMonthAPIView

urlpatterns = [
    path('api_ru/archive/', ArchiveRuListAPIView.as_view(), name='archive-list'),
    path('api_ru/archive/<int:pk>/', ArchiveRuDetailAPIView.as_view(), name='archive-detail'),
    path('api_ru/archive/date/<int:year>/', ArchiveByYearAPIView.as_view(), name='archive-by-year'),
    path('api_ru/archive/date/<int:year>/<int:month>/', ArchiveByYearMonthAPIView.as_view(), name='archive-by-year-month'),
    path('api_ru/search/', SearchArchiveRuAPIView.as_view(), name='archive-search'),
    path('api_ru/news/', NewsRuListAPIView.as_view(), name='news-list'),
    path('api_ru/gallery/', GalleryRuListAPIView.as_view(), name='gallery-list'),
    path('api_ru/connections/', ConnectionRuListAPIView.as_view(), name='connection-list'),
    path('api_ru/news/last/<int:n>/', LastRuNNewsAPIView.as_view(), name='last-n-news'),
    path('api_ru/governance/', GovernanceRuListAPIView.as_view(), name='governance-list'),
    path('api_ru/resolutions/', ResolutionRuListAPIView.as_view(), name='resolution-list'),
    path('api_ru/provisions/', ProvisionRuListAPIView.as_view(), name='provision-list'),
]
