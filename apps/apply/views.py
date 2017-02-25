from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from apps.session.models import Circles
from apps.apply.models import Application
# Create your views here.


def submit_home(request):
    application = Application.objects.filter(user = request.user)
    if len(application) == 0:
        application = Application.objects.create(user=request.user, semester='SP', year=2017)
        user_info = request.session.get('user_info',{})
        kaist_info = user_info.get('kaist_info', {})
        ku_std_no = kaist_info.get('ku_std_no','')
        Item.objects.create(application-application, article_name='position', content='')
        Item.objects.create(application=application, article_name='학과', content='')
        Item.objects.create(application=application, article_name='학번', content=ku_std_no)
        Item.objects.create(application=application, article_name='이메일', content=user_info.get('email',''))
        Item.objects.create(application=application, article_name='성별', content=user_info.get('gender',''))
        Item.objects.create(application=application, article_name='생년월일', content=user_info.get('birthday',''))
        Item.objects.create(application=application, article_name='이름', content=user_info.get('last_name','')+user_info.get('first_name',''))
        Item.objects.create(application=application, article_name='전화번호', content='')
        Item.objects.create(application=application, article_name='출신고교', content='')
        Item.objects.create(application=application, article_name='learn', content='')
        Item.objects.create(application=application, article_name='appeal', content='')
    content = {}
    for item in application.item_set.all():
        content[item.article_name]=item.content

    return render(request, 'apply/index.html',content)

@csrf_protect
def submit_data(request):
    if request.method == 'POST':
        application = Application.objects.filter(user = request.user, semester='SP', year='2017')
        for item in application.item_set.all()
            item.content = request.POST.get(item.article_name,'')
            item.save()
        #TODO: mail sending
    else:
        return HttpResponseForbidden()

