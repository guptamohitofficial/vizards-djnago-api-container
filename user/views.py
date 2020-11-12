from vizards.cc import *
from user.serializers import *
from user.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


@api_view(['get'])
def userAuth(request):
    users = User.objects.all()
    serialized = UserSerializer(users, many=True)
    return Response(serialized.data)


class GetUserDetails(APIView):
    
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        context = {
            "id" : request.user.id,
            "first_name" : request.user.first_name,
            "last_name" : request.user.last_name,
            "eamil" : request.user.email,
        }
        return Response(context)

    def get(self, request):
        return Response()


class userAuthLogin(APIView):

    def post(self, request):
        user = User.objects.filter(email=request.data.get('email'))
        context = {'status' : 'null'}
        print(user[0].password,request.data)
        if user:
            if user[0].password == request.data.get('password'):
                context['status']='success'
            else: context['status'] = 'invalid password' 
        else: context['status'] = 'invalid user'
        print(context)
        return Response(context)

    def get(self, request):
        return Response()

class userAuthSignup(APIView):

    def post(self, request):
        info = request.data
        info['username'] = info['email']
        info['password'] = make_password(info['password'])
        serializer = UserSerializer(data=request.data)
        context = {'status':'null'} 
        try: 
            if serializer.is_valid(): serializer.save();context['status'] = 'success'
            else: context['status'] = 'invalid format' 
        except KeyError: context['status'] = 'error'
        print(request.data, context)
        return Response(context)

    def get(self, request):
        #if ws(request,'email'):
        #    return Response({'statsu':'loggedin'})
        return Response()


@api_view(['get'])
def logout(request):
    delSession(request, 'all')
    return Response({'status':'loggedout'})




















