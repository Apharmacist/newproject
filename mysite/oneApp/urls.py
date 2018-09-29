from django.urls import path
from . import views
# 函数 path() 具有四个参数.
# 两个必须参数：route//相对路径 和 view//引用函数，两个可选参数：kwargs 和 name


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>/', views.detail, name='detail'),
    path('grades/', views.grades, name='grades'),
    path('students/', views.students, name='students'),
    path('grades/<int:num_id>/', views.gradeStudent, name='gradeStudent'),
    # num = 10,由 <int:num> 匹配生成。
    # 使用尖括号“捕获”这部分 URL，且以关键字参数的形式发送给视图函数。
    # 上述字符串的 :num> 部分定义了将被用于区分匹配模式的变量名，而 int: 则是一个转换器决定了应该以什么变量类型匹配这部分的 URL 路径。
]






