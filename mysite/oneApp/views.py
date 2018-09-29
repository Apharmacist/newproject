from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Grades, Students


def index(request):
    # request是请求体，就是浏览器发送给服务器的请求
    return HttpResponse("you are very good!")

def detail(request, num):
    return HttpResponse("You're looking at question %s." % num)
# 当某人请求你网站的某一页面时——比如说，
#  "/oneApp/34/" ，Django 将会载入 mysite.urls 模块，
# 因为这在配置项 ROOT_URLCONF 中设置了。
# 然后 Django 寻找名为 urlpatterns 变量并且按序匹配正则表达式。
# 在找到匹配项 'oneApp/'，它切掉了匹配的文本（"oneApp/"），将剩余文本——"34/"，发送至 'oneApp.urls' URLconf 做进一步处理。
# 在这里剩余文本匹配了 '<int:num>/'，使得我们 Django 以如下形式调用 detail():

# detail(request=<HttpRequest object>, question_id=34)

def grades(request):
    # 去模型里取数据
    gradesList = Grades.objects.all()

    # 将数据传递给模板，模板再渲染页面，最后视图将渲染好的页面返回给浏览器
    # 给模板传递的是一个字典
    text = {"grades": gradesList}
    return render(request, 'oneApp/grades.html', text)
def students(request):
    # 去模型里取数据
    studentsList = Students.objects.all()

    # 将数据传递给模板，模板再渲染页面，最后视图将渲染好的页面返回给浏览器
    # 给模板传递的是一个字典
    text = {"students": studentsList}
    return render(request, 'oneApp/students.html', text)

def gradeStudent(request,num_id):
    g = Grades.objects.get(pk=num_id)
    studentList = g.students_set.all()
    text1 = {"students": studentList}
    return render(request, 'oneApp/students.html', text1)
