from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import match_mentor_and_team


def home(request):
    # try:
    #     user = User.objects.get(username='Team-prashant')
    #     user_data = user.registration_form
    #     return HttpResponse("Success")
    # except User.DoesNotExist:
    #     return HttpResponse("User not found", status=404)
    # except AttributeError:
    #     return HttpResponse("User does not have 'registration_form' data", status=400)
    # match_mentor_and_team()
    # users_judge = User.objects.filter(username__icontains='Judge')

    # add_result_permission = Permission.objects.get(codename='add_result')
    # update_result_permission = Permission.objects.get(codename='change_result')
    # delete_result_permission = Permission.objects.get(codename='delete_result')

    # # user.has_perm('users.add_result')
    # for user in users_judge:
    #     user.user_permissions.add(add_result_permission)
    #     user.user_permissions.add(update_result_permission)
    #     user.user_permissions.add(delete_result_permission)
        
    #     print(user)
    return HttpResponse(200)


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


class ResultDashBoard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
