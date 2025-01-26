from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import News, Gallery, Connection, Governance, Resolution, Provision
from .serializers import NewsSerializer, GallerySerializer, ConnectionSerializer, GovernanceSerializer, \
    ResolutionSerializer, ProvisionSerializer


class CombinedSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('query', '').strip()

        # Search in News
        news_queryset = News.objects.all()
        if search_query:
            news_queryset = news_queryset.filter(
                Q(title__icontains=search_query) |
                Q(pre_description__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(author_position__icontains=search_query)
            )

        news_serializer = NewsSerializer(news_queryset, many=True)

        # Search in Gallery
        gallery_queryset = Gallery.objects.all()
        if search_query:
            gallery_queryset = gallery_queryset.filter(
                Q(title__icontains=search_query)
            )

        gallery_serializer = GallerySerializer(gallery_queryset, many=True)

        return Response({
            'news': news_serializer.data,
            'galleries': gallery_serializer.data
        })

    def post(self, request):
        data_type = request.data.get('type')
        if data_type == 'news':
            serializer = NewsSerializer(data=request.data)
        elif data_type == 'gallery':
            serializer = GallerySerializer(data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        data_type = request.data.get('type')
        if data_type == 'news':
            instance = News.objects.get(pk=pk)
            serializer = NewsSerializer(instance, data=request.data)
        elif data_type == 'gallery':
            instance = Gallery.objects.get(pk=pk)
            serializer = GallerySerializer(instance, data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        data_type = request.GET.get('type')
        if data_type == 'news':
            News.objects.get(pk=pk).delete()
        elif data_type == 'gallery':
            Gallery.objects.get(pk=pk).delete()
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ConnectionListAPIView(ListAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

class LastNNewsAPIView(APIView):
    def get(self, request, n, *args, **kwargs):
        """
        Retrieve the last 'n' news articles.
        """
        try:
            n = int(n)  # Ensure 'n' is an integer
            news_queryset = News.objects.order_by('-added_date')[:n]
            serializer = NewsSerializer(news_queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(
                {"error": "Invalid value for 'n'. Must be an integer."},
                status=status.HTTP_400_BAD_REQUEST
            )


class GovernanceListAPIView(ListAPIView):
    queryset = Governance.objects.all()
    serializer_class = GovernanceSerializer


class ResolutionListAPIView(ListAPIView):
    queryset = Resolution.objects.all()
    serializer_class = ResolutionSerializer


class ProvisionListAPIView(ListAPIView):
    queryset = Provision.objects.all()
    serializer_class = ProvisionSerializer