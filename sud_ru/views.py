from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import ArchiveRu, ConnectionRu, GovernanceRu, ResolutionRu, ProvisionRu
from .serializers import ArchiveRuSerializer, ConnectionRuSerializer, GovernanceRuSerializer, \
    ResolutionRuSerializer, ProvisionRuSerializer


class ArchiveRuListAPIView(ListAPIView):
    queryset = ArchiveRu.objects.all()
    serializer_class = ArchiveRuSerializer

class SearchArchiveRuAPIView(APIView):
    def get(self, request):
        search_query = request.GET.get('query', '').strip()

        archive_queryset = ArchiveRu.objects.all()
        if search_query:
            archive_queryset = archive_queryset.filter(
                Q(title__icontains=search_query) |
                Q(pre_description__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(author_position__icontains=search_query)
            )

        serializer = ArchiveRuSerializer(archive_queryset, many=True)
        return Response(serializer.data)


class ConnectionRuListAPIView(ListAPIView):
    queryset = ConnectionRu.objects.all()
    serializer_class = ConnectionRuSerializer


class LastRuNNewsAPIView(APIView):
    """
    Retrieve the last 'n' news articles from the ArchiveRu model.
    """
    def get(self, request, n, *args, **kwargs):
        try:
            n = int(n)  # Ensure 'n' is an integer

            if n <= 0:
                return Response(
                    {"error": "The value of 'n' must be greater than 0."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Filter only news articles from ArchiveRu
            news_queryset = ArchiveRu.objects.filter(type='news').order_by('-added_date')[:n]

            if not news_queryset.exists():
                return Response(
                    {"message": "No news articles found."},
                    status=status.HTTP_204_NO_CONTENT
                )

            serializer = ArchiveRuSerializer(news_queryset, many=True, context={"request": request})
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


class GovernanceRuListAPIView(ListAPIView):
    queryset = GovernanceRu.objects.all()
    serializer_class = GovernanceRuSerializer


class ResolutionRuListAPIView(ListAPIView):
    queryset = ResolutionRu.objects.all()
    serializer_class = ResolutionRuSerializer


class ProvisionRuListAPIView(ListAPIView):
    queryset = ProvisionRu.objects.all()
    serializer_class = ProvisionRuSerializer

class ArchiveRuDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        archive_entry = get_object_or_404(ArchiveRu, pk=pk)
        serializer = ArchiveRuSerializer(archive_entry, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class NewsRuListAPIView(ListAPIView):
    queryset = ArchiveRu.objects.filter(type='news').order_by('-added_date')
    serializer_class = ArchiveRuSerializer


class GalleryRuListAPIView(ListAPIView):
    queryset = ArchiveRu.objects.filter(type='gallery').order_by('-created_at')
    serializer_class = ArchiveRuSerializer

class ArchiveByYearAPIView(ListAPIView):
    """
    Retrieve all ArchiveRu entries for a specific year.
    """
    serializer_class = ArchiveRuSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        return ArchiveRu.objects.filter(added_date__year=year).order_by('-added_date')

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
    Retrieve all ArchiveRu entries for a specific year and month.
    """
    serializer_class = ArchiveRuSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        return ArchiveRu.objects.filter(
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
