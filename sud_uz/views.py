from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import ArchiveUz, ConnectionUz, GovernanceUz, ResolutionUz, ProvisionUz
from .serializers import ArchiveUzSerializer, ConnectionUzSerializer, GovernanceUzSerializer, \
    ResolutionUzSerializer, ProvisionUzSerializer


class ArchiveUzListAPIView(ListAPIView):
    queryset = ArchiveUz.objects.all()
    serializer_class = ArchiveUzSerializer

class SearchArchiveUzAPIView(APIView):
    def get(self, request):
        search_query = request.GET.get('query', '').strip()

        archive_queryset = ArchiveUz.objects.all()
        if search_query:
            archive_queryset = archive_queryset.filter(
                Q(title__icontains=search_query) |
                Q(pre_description__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(author_position__icontains=search_query)
            )

        serializer = ArchiveUzSerializer(archive_queryset, many=True)
        return Response(serializer.data)


class ConnectionUzListAPIView(ListAPIView):
    queryset = ConnectionUz.objects.all()
    serializer_class = ConnectionUzSerializer


class LastUzNNewsAPIView(APIView):
    """
    Retrieve the last 'n' news articles from the ArchiveUz model.
    """
    def get(self, request, n, *args, **kwargs):
        try:
            n = int(n)  # Ensure 'n' is an integer

            if n <= 0:
                return Response(
                    {"error": "The value of 'n' must be greater than 0."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Filter only news articles from ArchiveUz
            news_queryset = ArchiveUz.objects.filter(type='news').order_by('-added_date')[:n]

            if not news_queryset.exists():
                return Response(
                    {"message": "No news articles found."},
                    status=status.HTTP_204_NO_CONTENT
                )

            serializer = ArchiveUzSerializer(news_queryset, many=True, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError:
            return Response(
                {"error": "Invalid value for 'n'. Must be a positive integer."},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GovernanceUzListAPIView(ListAPIView):
    queryset = GovernanceUz.objects.all()
    serializer_class = GovernanceUzSerializer


class ResolutionUzListAPIView(ListAPIView):
    queryset = ResolutionUz.objects.all()
    serializer_class = ResolutionUzSerializer


class ProvisionUzListAPIView(ListAPIView):
    queryset = ProvisionUz.objects.all()
    serializer_class = ProvisionUzSerializer

class ArchiveUzDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        archive_entry = get_object_or_404(ArchiveUz, pk=pk)
        serializer = ArchiveUzSerializer(archive_entry, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class NewsUzListAPIView(ListAPIView):
    queryset = ArchiveUz.objects.filter(type='news').order_by('-added_date')
    serializer_class = ArchiveUzSerializer


class GalleryUzListAPIView(ListAPIView):
    queryset = ArchiveUz.objects.filter(type='gallery').order_by('-created_at')
    serializer_class = ArchiveUzSerializer

class ArchiveByYearAPIView(ListAPIView):
    """
    Retrieve all ArchiveUz entries for a specific year.
    """
    serializer_class = ArchiveUzSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        return ArchiveUz.objects.filter(added_date__year=year).order_by('-added_date')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"message": f"No archive entries found for the year {self.kwargs.get('year')}."},
                status=status.HTTP_204_NO_CONTENT
            )
        serializer = self.get_serializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArchiveByYearMonthAPIView(ListAPIView):
    """
    Retrieve all ArchiveUz entries for a specific year and month.
    """
    serializer_class = ArchiveUzSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        return ArchiveUz.objects.filter(
            added_date__year=year, added_date__month=month
        ).order_by('-added_date')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"message": f"No archive entries found for {self.kwargs.get('year')}-{self.kwargs.get('month')}."},
                status=status.HTTP_204_NO_CONTENT
            )
        serializer = self.get_serializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)