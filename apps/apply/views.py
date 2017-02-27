from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from apps.session.models import Circles
from apps.apply.models import Application, Item
from apps.session.models import UserProfile
from frontend.web.apply.dates import init as init_date
import json
# Create your views here.


def submit_home(request):
    if not request.user.is_authenticated:
        return redirect('/')
    user_profile = UserProfile.objects.filter(user=request.user) 
    application = Application.objects.filter(user=user_profile[0], semester='SP', year=2017).first()
    if not application:
        application = Application.objects.create(user=user_profile[0], semester='SP', year=2017)
        user_info = request.session.get('user_info',{})
        kaist_info = user_info.get('kaist_info')
        if kaist_info:
            kaist_info = json.loads(kaist_info)
        else:
            kaist_info = {}
        ku_std_no = kaist_info.get('ku_std_no', '')
        gender = user_info.get('gender','')
        if gender=='*M':
            gender='m'
        elif gender=='*F':
            gender='f'
        else:
            gender='e'
        Item.objects.create(application=application, article_name='name', content=user_info.get('last_name','') + user_info.get('first_name',''))
        Item.objects.create(application=application, article_name='studentNumber', content=ku_std_no)
        Item.objects.create(application=application, article_name='department', content='')
        Item.objects.create(application=application, article_name='contactNumber', content='')
        Item.objects.create(application=application, article_name='email', content=user_info.get('email',''))
        Item.objects.create(application=application, article_name='gender', content=gender)
        Item.objects.create(application=application, article_name='position', content='')
        birth = Item.objects.create(application=application, article_name='birthDay', content=user_info.get('birthday','--'))
        if len(birth.content) < 3:
            birth.content = '--';
            birth.save()
        Item.objects.create(application=application, article_name='question0', content='')
        Item.objects.create(application=application, article_name='question1', content='')
        interview = Item.objects.create(application=application, article_name='interviewDates', content='')
        interview.content = json.dumps(init_date)
        interview.save() 
    content = {}
    content['first'] = application.first
    for item in application.item_set.all():
        if item.article_name == 'birthDay':
            if len(item.content) < 2:
                item.content = '--'
                item.save()
            birthday = item.content.split('-')
            content['birthYear'] = birthday[0]
            content['birthMonth'] = birthday[1]
            content['birthDay'] = birthday[2]
        elif item.article_name == 'interviewDates':
            content['interviewDates'] = json.loads(item.content)
        else:
            content[item.article_name]=item.content

    return render(request, 'apply/index.html', content)

@csrf_protect
def submit_data(request):
    if not request.user.is_authenticated:
        return redirect('/')
    user_profile = UserProfile.objects.filter(user = request.user)
    dic = {'position':'포지션', 'department':'학과', 'studentNumber':'학번', 'email':'이메일', 'gender':'성별', 'birthDay':'생일', 'name':'이름', 'contactNumber':'폰번호','question0':'하고 싶은 것', 'question1':'어필해주세요', 'interviewDates':'면접 가능 시간'}
    message = ""
    subject = "2017신입생 지원 "
    if request.method == 'POST':
        application = Application.objects.filter(user = user_profile[0], semester='SP', year='2017')[0]
        for item in application.item_set.all():
            if item.article_name == 'birthDay':
                item.content = request.POST.get('birthYear','') + '-' + request.POST.get('birthMonth','') + '-'  + request.POST.get('birthDay','')
            elif item.article_name == 'interviewDates':
                time_data = json.loads(item.content)
                date0 = request.POST.getlist('interviewDate0', [])
                date1 = request.POST.getlist('interviewDate1', [])
                print('date0',date0)
                print('date1',date1)
                for i in range(len(time_data[0]['dates'])):
                    if not str(i) in date0:
                        time_data[0]['dates'][i]['checked'] = False
                    else:
                        time_data[0]['dates'][i]['checked'] = True
                for i in range(len(time_data[1]['dates'])):
                    if not str(i) in date1:
                        time_data[1]['dates'][i]['checked'] = False
                    else:
                        time_data[1]['dates'][i]['checked'] = True
                item.content = json.dumps(time_data)
            else:
                item.content = request.POST.get(item.article_name,'')
            item.save()
            if not item.article_name == 'interviewDates':
                message += dic.get(item.article_name,"??") + ": "
                message += item.content + "\n"
        application.first = False
        application.save()
        subject += request.POST.get('studentNumber', '??') + " " + request.POST.get('name', '??')
        send_mail(subject, message, 'no-reply@apply.sparcs.org',['interview2017@sparcs.org', ], fail_silently=False,) 
        return redirect('/apply/finish')
    else:
        return HttpResponseForbidden()

def finish_submit(request):
    first = True
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user = request.user)[0]
        application = Application.objects.filter(user = user_profile, semester = 'SP', year=2017)
        if not len(application) == 0:
            application = application[0]
            first = application.first
        return render(request, 'apply/finish.html',{'first':first})
    else:
        return redirect('/')
