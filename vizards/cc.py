from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


def who(token):
    user = Token.objects.get(key=token).user
    if user: return user 
    else: return False
'''
def hasSession(func):
    def inner(request, *args, **kwargs):
        if request.session.get("email"):
            return func(request, *args, **kwargs)    
        else:
            request.session['tourl'] = request.build_absolute_uri()
            return Response({'status':'notSessoined'})
    return inner

def createSession(request, obj):
    request.session['id'] = obj.id
    request.session['fname'] = obj.fname
    request.session['lname'] = obj.lname
    request.session['bname'] = obj.bname
    request.session['email'] = obj.email
    request.session['phone'] = obj.phone
    request.session['obj'] = {
        'id' : obj.id,
        'fname' : obj.fname,
        'lname' : obj.lname,
        'bname' : obj.bname,
        'email' : obj.email,
        'phone' : obj.phone
    }

def ws(request, ses_name):
    return request.session.get(ses_name)

def delSession(request, which=[]):
    try:
        if which == 'all':
            del request.session['id']
            del request.session['fname']
            del request.session['lname']
            del request.session['bname']
            del request.session['email']
            del request.session['phone']
            del request.session['obj']
        else:
            for i in which:
                try: del request.session[i]
                except KeyError: pass
                
    except KeyError:
        return Response({
            'status':'KeyError',
            'detail':'Try again to logout'
        })
'''
