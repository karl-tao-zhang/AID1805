from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def request_views(request):
    # request,类型就是 HttpRequest
    # request 封装的是所有与请求相关的内容
    # print(dir(request))

    # 协议 (方案)
    scheme = request.scheme
    # 请求主体
    body = request.body
    # 请求资源的具体路径
    path = request.path
    # 请求主机的地址 / 域名
    host = request.get_host()
    # 请求方法
    method = request.method
    # get方式请求数据
    get = request.GET
    # post方式请求数据
    post = request.POST
    # cookie 中的数据
    cookies = request.COOKIES
    # 请求的元数据
    meta = request.META
    return render(request,'01_request.html',locals())


def meta_views(request):
    if 'HTTP_REFERER' in request.META:
        print('请求源地址为:'+request.META['HTTP_REFERER'])
    return HttpResponse("Request OK")

# /03_form/
def form_views(request):
    return render(request,'02_form.html')

# /04_get/
def get_views(request):
    # print(request.GET)
    uname = request.GET['uname']
    upwd = request.GET['upwd']
    return HttpResponse("用户名:"+uname+",密码:"+upwd)

# /05_post/
def post_views(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    return HttpResponse("用户名:" + uname + ",密码:" + upwd)

# /06_login/
def login_views(request):
    if request.method == "GET":
        return render(request, '03_login.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        return HttpResponse('uname:'+uname+',upwd:'+upwd)

# /07_remark/
def remark_views(request):
    form = RemarkForm()
    return render(request,'04_remark.html',locals())


# /08_userLogin/
def userLogin_views(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'05_login.html',locals())
    else:
        # 1.手动接收提交的数据
        # uname = request.POST['uname']
        # upwd = request.POST['upwd']

        # 2.自动接收提交的数据
        # 2.1 通过 forms.Form的构造,接收request.POST
        form = LoginForm(request.POST)
        # 2.2 is_valid()
        if form.is_valid():
            # 2.3 form.cleaned_data
            cd = form.cleaned_data
            print(cd)
            print(request.POST)
            uname = cd['uname']
            upwd = cd['upwd']
            uList = Users.objects.filter(uname=uname,upwd=upwd)
            if uList:
                return HttpResponse('登录成功')
            else:
               form = LoginForm()
               errMsg = "用户名或密码不正确"
               return render(request,'05_login.html',locals())





#/09_register/
def register_views(request):
    if request.method =='GET':
        form = RegisterForm()
        return render(request,'06_register.html',locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uname = cd['uname']
            uList = Users.objects.filter(uname=uname)
            if uList:
                errMsg='用户名已经存在'
                form = RegisterForm()
                return render(request,'06_register.html',locals())
            else:
                Users(**form.cleaned_data).save()
                return HttpResponse('注册成功')



