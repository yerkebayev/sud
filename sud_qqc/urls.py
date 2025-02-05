from django.urls import path
from .views import ConnectionQqcListAPIView, LastQqcNNewsAPIView, GovernanceQqcListAPIView, \
    ResolutionQqcListAPIView, ProvisionQqcListAPIView, ArchiveQqcListAPIView, \
    SearchArchiveQqcAPIView, ArchiveQqcDetailAPIView, NewsQqcListAPIView, GalleryQqcListAPIView, ArchiveByYearAPIView, \
    ArchiveByYearMonthAPIView

urlpatterns = [
    path('api_qqc/archive/', ArchiveQqcListAPIView.as_view(), name='archive-list'),
    path('api_qqc/archive/<int:pk>/', ArchiveQqcDetailAPIView.as_view(), name='archive-detail'),
    path('api_qqc/archive/date/<int:year>/', ArchiveByYearAPIView.as_view(), name='archive-by-year'),
    path('api_qqc/archive/date/<int:year>/<int:month>/', ArchiveByYearMonthAPIView.as_view(), name='archive-by-year-month'),
    path('api_qqc/search/', SearchArchiveQqcAPIView.as_view(), name='archive-search'),
    path('api_qqc/news/', NewsQqcListAPIView.as_view(), name='news-list'),
    path('api_qqc/gallery/', GalleryQqcListAPIView.as_view(), name='gallery-list'),
    path('api_qqc/connections/', ConnectionQqcListAPIView.as_view(), name='connection-list'),
    path('api_qqc/news/last/<int:n>/', LastQqcNNewsAPIView.as_view(), name='last-n-news'),
    path('api_qqc/governance/', GovernanceQqcListAPIView.as_view(), name='governance-list'),
    path('api_qqc/resolutions/', ResolutionQqcListAPIView.as_view(), name='resolution-list'),
    path('api_qqc/provisions/', ProvisionQqcListAPIView.as_view(), name='provision-list'),
]
