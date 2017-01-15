from apps.session.models import UserProfile
from django.contrib.messages.storage import session
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponse
from apps.session.sparcsssov2 import Client
import random
# Create your views here.

sso_client = Client(settings.SSO_ID, settings.SSO_KEY, is_beta=False)


def test_login(request):
    user_list = User.objects.filter(username='1')
    if len(user_list) == 0:
        user = User.objects.create_user(username='1',
                                        email='test@kaist.ac.kr',
                                        password=str(random.getrandbits(32)),
                                        first_name='duck',
                                        last_name='duck')
        user.save()
        UserProfile.objects.create(user=user,
                                   sso_uid='1')
    else:
        user = user_list[0]

    user.backend = 'django.contrib.auth.backends.ModelBackend'

    auth_login(request, user)
    nexturl = request.session.pop('next', '/')
    print(request.user.is_authenticated)
    return redirect(nexturl)

# /session/login/
def login(request):
    if request.user.is_authenticated:
        return redirect('/apply')

    request.session['next'] = request.GET.get('next', '/')

    login_url, state = sso_client.get_login_params()
    request.session['sso_state'] = state

    return redirect(login_url)


def callback(request):
    state_before = request.session['sso_state']
    state = request.GET.get('state', '')

    if(state_before != state):
        return HttpResponseForbidden()

    code = request.GET.get('code','')
    user_info = sso_client.get_user_info(code)

    sid = user_info['sid']
    user_list = User.objects.filter(username=sid)
    if len(user_list) == 0:
        user = User.objects.create_user(username=sid,
                                        email=user_info['email'],
                                        password=str(random.getrandbits(32)),
                                        first_name=user_info['first_name'],
                                        last_name=user_info['last_name'])
        user.save()
        UserProfile.objects.create(user=user,
                                   sso_uid=user_info['uid'])
    else:
        user = user_list[0]

    user.backend = 'django.contrib.auth.backends.ModelBackend'

    auth_login(request, user)
    nexturl = request.session.pop('next', '/')
    return redirect(nexturl)


def logout(request):
    if not request.user.is_authenticated:
        return redirect('/')

    auth_logout(request)

    return redirect('/')

def unregister(request):
    code = request.GET.get('code', '')
    user_info = sso_client.get_user_info(code)
    user = UserProfile.objects.get(sso_uid=user_info['uid'])
    user.delete()

    return redirect('/')
