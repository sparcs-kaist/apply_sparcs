from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from apps.session.models import Circles
from apps.apply.models import Application
# Create your views here.


def submit_home(request):
    return render(request, 'submit_home.html')

# 각 동아리별 신청버튼을 눌렀을때??에 해당함
def submit_init(request):
    cuid = request.GET.get('circle_uid','')
    circle_uid = Circles.objects.filter(circle_uid=cuid)

    if len(circle_uid) == 0:
        return HttpResponseForbidden
    else:
        year = int(request.GET.get('year',0))
        semester = request.GET.get('semester','')
        circle_uid = circle_uid[0]
        Application.objects.create(user=request.user,
                                   year=year,
                                   semester=semester,
                                   circle_uid=circle_uid)

    return HttpResponse("submit init success??")

@csrf_protect
def submit_data(request):
    if request.method == 'POST':
        cid = request.POST.get('circle_uid', '')
        num = request.POST.get('num_contents', 0)
        semester = request.POST.get('semester', '')
        year = request.POST.get('year',0)
        contents = []
        for i in range(int(num)):
            contents.append(request.POST.get('content-%d' % i, ''))

        print(cid, num, semester, year, contents)
    else:
        return HttpResponseForbidden()

    return HttpResponse('%s\n%s\n%s\n%s\n%s' % (cid, num, semester, year, contents))
