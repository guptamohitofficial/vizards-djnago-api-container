from vizards.cc import *
from card.serializers import *
from user.serializers import UserSerializer
from card.models import *


class GetUserSchedule(APIView):
    
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        cards = Card.objects.filter(creator=request.user)
        serializedCards = CardSerializer(cards, many=True)
        return Response(serializedCards.data)

    def get(self, request):
        return Response()
        

class CreateVisitingCard(APIView):
    
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        print(request.user)
        serializer = CardSerializer(data=request.data)
        context = {'status':'null'}  
        print(serializer.data)
        return Response(context)
        try: 
            if serializer.is_valid(): serializer.save(); context['status'] = 'success'
            else: context['status'] = 'invalid format' 
        except KeyError: context['status'] = 'error'

    def get(self, request):
        return Response()
        
'''
{
    "creator" : 8,
    "ctype" : "visiting",
    "bname" : "WorksNet",
    "bqoute" : "Social Adaptive Learinng",
    "name" : "Mohit Gutpa",
    "address" : "Logoin to WorksNet.in Online",
    "phone" : "+91 7999893361",
    "ofPhone" : "Personal"
}
'''

class CreateMeetingCard(APIView):

    def post(self, request):
        context = {
            'status' : 'null'
            }

        return Response(context)

    def get(self, request):
        
        return Response()

class cardList(APIView):
    
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request):
        context = {
            'status' : 'null'
            }

        return Response(context)

    def get(self, request):
        print(request.user)
        cards = Card.objects.filter(creator=request.user)
        serialized = CardSerializer(cards, many=True)
        #serializedUser = UserSerializer(request.user)
        #return Response(serializedUser.data)
        return Response(serialized.data)



