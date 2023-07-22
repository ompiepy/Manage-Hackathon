from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    try:
        user = User.objects.get(username='Team-prashant')
        user_data = user.registration_form
        return HttpResponse("Success")
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)
    except AttributeError:
        return HttpResponse("User does not have 'registration_form' data", status=400)


# @api_view(['GET','POST'])
# def login(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username')
#         pass_word = request.POST.get('password')
#         authetication = authenticate(
#             request, username=user_name, password=pass_word)
#         print(authetication)
#         print(user_name)
#         print(pass_word)
#         if authetication is not None:
#             login(request, authetication)
#             messages.success(request, 'successfully logged in!')
#             return HttpResponse(200)
#         else:
#             message = str(messages.error(request, "login failed!"))
#             return HttpResponse(message)
#     return Response(200)


# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def login(request):
#     user_name = request.data.get('username')
#     pass_word = request.data.get('password')
#     # authetication = authenticate(
#     #     request, username=user_name, password=pass_word)
#     print(user_name)
#     print(pass_word)

#     # if authetication is not None:
#     #     login(request, authetication)
#     #     return Response({'detail': 'Successfully logged in!'}, status=status.HTTP_200_OK)
#     # else:
#     return Response({'detail': 'Login failed!'}, status=status.HTTP_401_UNAUTHORIZED)


