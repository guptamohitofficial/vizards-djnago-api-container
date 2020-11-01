from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from vizards.serializers import UserSerializer
from vizards.cc import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
class WhoUser(APIView):
    def post(self, request, *args, **kwargs):
        user = who(request.data.get('token'))
        if user: return Response({'detail':True})
        else: return Response({'detail':False})


