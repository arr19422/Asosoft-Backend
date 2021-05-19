
from rest_framework import viewsets
from ..Models.asociationModel import Asociation
from ..Serializers.asociationSerializer import AsociationSerializer


class AsociationViewSet(viewsets.ModelViewSet):
    queryset = Asociation.objects.all()
    serializer_class = AsociationSerializer
