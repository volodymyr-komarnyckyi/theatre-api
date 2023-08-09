from rest_framework import viewsets

from theatre.models import Genre, Actor, Play
from theatre.serializers import GenreSerializer, ActorSerializer, PlaySerializer, PlayListSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("genres", "actors")

        return queryset

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == "list":
            serializer_class = PlayListSerializer

        elif self.action == "retrieve":
            serializer_class = PlayListSerializer

        return serializer_class
