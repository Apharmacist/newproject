from django.contrib import admin

# Register your models here.
from .models import Grades, Students
# 注册




class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2  # 额外创建两个学生
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # 列表页属性
    list_display = ['pk', 'g_name', 'g_date', 'g_girl_num', 'g_boy_num', 'isDelete']
    list_filter = ['g_name']
    search_fields = ['g_name']
    list_per_page = 5


    # 添加 、修改页属性

    # fields = ['g_girl_num', 'g_boy_num', 'g_name', 'g_date', 'isDelete']
    fieldsets = [
        ("num", {"fields": ['g_girl_num', 'g_boy_num']}),
        ("base", {"fields": ['g_name', 'g_date', 'isDelete']}),


                 ]
admin.site.register(Grades, GradesAdmin)




@admin.register(Students)   # 装饰一个类
class StudentsAdmin(admin.ModelAdmin):

    def gender(self):
        if self.s_gender:
            return "男"
        else:
            return "女"
    # 设置页面列的名称
    gender.short_description = "性别"

    list_display = ['pk', 's_name', 's_age', gender,
                    's_contend', 'grades', 'isDelete']
    list_per_page = 5


    actions_on_bottom = True
    actions_on_top = False
# admin.site.register(Students,StudentsAdmin)