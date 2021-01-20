import datetime
from django.http import HttpResponse
from student.models import StudentRecord
from student.forms import StudentForm
from django.shortcuts import redirect, render
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
objects = ['john', 'paul', 'george', 'ringo']

# Create your views here.


# def index (request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


def student_form(request, pk=None):
    # if pk:
    #     student = StudentRecord.objects.filter(id=pk)
    #     form = StudentForm(instance=student[0])
    # else:
    #     form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student-list/')
    return render(request, 'add_students.html', locals())


def student_list(request):
    students = StudentRecord.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(students, 10)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    return render(request, 'students.html', locals())
