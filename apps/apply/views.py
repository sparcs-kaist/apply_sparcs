from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from apps.session.models import Circles
from apps.apply.models import Application, Item
from apps.session.models import UserProfile
import json
# Create your views here.


def submit_home(request):
    user_profile = UserProfile.objects.filter(user=request.user) 
    application = Application.objects.filter(user=user_profile[0], semester='SP', year=2017).first()

    if not application:
        application = Application.objects.create(user=user_profile[0], semester='SP', year=2017)
        user_info = request.session.get('user_info',{})
        kaist_info = json.loads(user_info.get('kaist_info', "{}"))
        ku_std_no = kaist_info.get('ku_std_no', '')

        Item.objects.create(application=application, article_name='position', content='')
        Item.objects.create(application=application, article_name='학과', content='')
        Item.objects.create(application=application, article_name='학번', content=ku_std_no)
        Item.objects.create(application=application, article_name='이메일', content=user_info.get('email',''))
        Item.objects.create(application=application, article_name='성별', content=user_info.get('gender',''))
        Item.objects.create(application=application, article_name='생년월일', content=user_info.get('birthday',''))
        Item.objects.create(application=application, article_name='이름', content=user_info.get('last_name','') + user_info.get('first_name',''))
        Item.objects.create(application=application, article_name='전화번호', content='')
        Item.objects.create(application=application, article_name='출신고교', content='')
        Item.objects.create(application=application, article_name='learn', content='')
        Item.objects.create(application=application, article_name='appeal', content='')

    content = {}
    for item in application.item_set.all():
        content[item.article_name]=item.content

    return render(request, 'apply/index.html', content)

@csrf_protect
def submit_data(request):
    user_profile = UserProfile.objects.filter(user = request.user)
    if request.method == 'POST':
        application = Application.objects.filter(user = user_profile[0], semester='SP', year='2017')[0]
        for item in application.item_set.all():
            item.content = request.POST.get(item.article_name,'')
            item.save()
        #TODO: mail sending
        send_mail('hello', 'hello world', 'no-reply@apply.sparcs.org',['leejeok@sparcs.org', ], fail_silently=False,) 
        return redirect('/')
    else:
        return HttpResponseForbidden()

