from vizards.cc import *
from user.serializers import *
from user.models import *
from django.contrib.auth.models import User


@api_view(['get'])
def userAuth(request):
    users = User.objects.all()
    serialized = UserSerializer(users, many=True)
    return Response(serialized.data)


class userAuthLogin(APIView):

    def post(self, request):
        if ws(request,'email'):
            return Response({'status' : 'loggedin'})
        user = User.objects.filter(email=request.data.get('email'))
        context = {'status' : 'null'}
        if user:
            if user[0].password == request.data.get('password'):
                context['status']='success'
                createSession(request, user[0]) 
            else: context['status'] = 'invalid password' 
        else: context['status'] = 'invalid user'
        return Response(context)

    def get(self, request):
        return Response()

class userAuthSignup(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        context = {'status':'null'}
        if ws(request,'email'):
            return Response(context)    
        try: 
            if serializer.is_valid(): serializer.save();context['status'] = 'success'
            else: context['status'] = 'invalid format' 
        except KeyError: context['status'] = 'error'
        return Response(context)

    def get(self, request):
        if ws(request,'email'):
            return Response({'statsu':'loggedin'})
        return Response()


@api_view(['get'])
def logout(request):
    delSession(request, 'all')
    return Response({'status':'loggedout'})




















