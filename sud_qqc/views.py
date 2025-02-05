from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import ArchiveQqc, ConnectionQqc, GovernanceQqc, ResolutionQqc, ProvisionQqc
from .serializers import ArchiveQqcSerializer, ConnectionQqcSerializer, GovernanceQqcSerializer, \
    ResolutionQqcSerializer, ProvisionQqcSerializer


class ArchiveQqcListAPIView(ListAPIView):
    queryset = ArchiveQqc.objects.all()
    serializer_class = ArchiveQqcSerializer

class SearchArchiveQqcAPIView(APIView):
    def get(self, request):
        search_query = request.GET.get('query', '').strip()

        archive_queryset = ArchiveQqc.objects.all()
        if search_query:
            archive_queryset = archive_queryset.filter(
                Q(title__icontains=search_query) |
                Q(pre_description__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(author_position__icontains=search_query)
            )

        serializer = ArchiveQqcSerializer(archive_queryset, many=True)
        return Response(serializer.data)


class ConnectionQqcListAPIView(ListAPIView):
    queryset = ConnectionQqc.objects.all()
    serializer_class = ConnectionQqcSerializer


class LastQqcNNewsAPIView(APIView):
    """
    Retrieve the last 'n' news articles from the ArchiveQqc model.
    """
    def get(self, request, n, *args, **kwargs):
        try:
            n = int(n)  # Ensure 'n' is an integer

            if n <= 0:
                return Response(
                    {"error": "The value of 'n' must be greater than 0."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Filter only news articles from ArchiveQqc
            news_queryset = ArchiveQqc.objects.filter(type='news').order_by('-added_date')[:n]

            if not news_queryset.exists():
                return Response(
                    {"message": "No news articles found."},
                    status=status.HTTP_204_NO_CONTENT
                )

            serializer = ArchiveQqcSerializer(news_queryset, many=True, context={"request": request})
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


class GovernanceQqcListAPIView(ListAPIView):
    queryset = GovernanceQqc.objects.all()
    serializer_class = GovernanceQqcSerializer


class ResolutionQqcListAPIView(ListAPIView):
    queryset = ResolutionQqc.objects.all()
    serializer_class = ResolutionQqcSerializer


class ProvisionQqcListAPIView(ListAPIView):
    queryset = ProvisionQqc.objects.all()
    serializer_class = ProvisionQqcSerializer

class ArchiveQqcDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        archive_entry = get_object_or_404(ArchiveQqc, pk=pk)
        serializer = ArchiveQqcSerializer(archive_entry, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class NewsQqcListAPIView(ListAPIView):
    queryset = ArchiveQqc.objects.filter(type='news').order_by('-added_date')
    serializer_class = ArchiveQqcSerializer


class GalleryQqcListAPIView(ListAPIView):
    queryset = ArchiveQqc.objects.filter(type='gallery').order_by('-created_at')
    serializer_class = ArchiveQqcSerializer

class ArchiveByYearQqcAPIView(ListAPIView):
    """
    Retrieve all ArchiveQqc entries for a specific year.
    """
    serializer_class = ArchiveQqcSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        return ArchiveQqc.objects.filter(added_date__year=year).order_by('-added_date')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"message": f"No archive entries found for the year {self.kwargs.get('year')}."},
                status=status.HTTP_204_NO_CONTENT
            )
        serializer = self.get_serializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArchiveByYearMonthQqcAPIView(ListAPIView):
    """
    Retrieve all ArchiveQqc entries for a specific year and month.
    """
    serializer_class = ArchiveQqcSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        return ArchiveQqc.objects.filter(
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