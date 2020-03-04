from django.shortcuts import render,redirect
from . forms import  Login
from  .forms import  Register
from . import  models
import hashlib
# Create your views here.


#全局
def getBase(request):

    return render(request,'my_trashcan/base.html')


#首页
def getIndex(request):

    ash_all = models.Ashbin.objects.all()
    # for x in ash_all:
    #     # print(x.author,x.title,x.body,x.created_time)
    #     list_ash = {'author':x.author,'title':x.title,'body':x.body,'time':x.created_time}
    #     print(list_ash)

    if not request.session.get('is_login',None):
        personalized = '登陆后才能显示个性签名哦！'
        return render(request, 'my_trashcan/index.html',locals())

    else:
        username = request.session.get('user_name')
        author = models.User.objects.get(name=username)
        personalized = author.selfdom


    return render(request, 'my_trashcan/index.html',locals())

#丢垃圾
def getAsh(request):

    if  request.method == 'POST':

        title = request.POST.get('name_ash')
        text_t  = request.POST.get('text_ash')

        if not request.session.get('is_login',None):

            message = '登陆后才能丢垃圾'
            return render(request,'my_trashcan/post_ash.html',locals())

        elif not title :

            message = '名称不能为空'
            return  render(request,'my_trashcan/post_ash.html',locals())

        elif not text_t:

            message = '内容不能为空'
            return render(request, 'my_trashcan/post_ash.html', locals())

        else:
            username = request.session.get('user_name')
            author = models.User.objects.get(name=username)
            print(author.selfdom)


            ashcan = models.Ashbin(title=title,body=text_t,author=author)

            ashcan.save()

    return render(request, 'my_trashcan/post_ash.html', locals())

#注册
def getRegister(request):

    if request.session.get('is_login', None):
        return redirect("/ash/getIndex/")

    if request.method == 'POST':

        Register_re = Register(request.POST)
        message = "请检查填写的内容！"

        if Register_re.is_valid():

            username = Register_re.cleaned_data['username']
            password1 = Register_re.cleaned_data['password1']
            password2 = Register_re.cleaned_data['password2']
            email = Register_re.cleaned_data['email']
            sex = Register_re.cleaned_data['sex']
            set = Register_re.cleaned_data['set']

            if password1 != password2:

                message = "两次输入的密码不同！"

                return render(request, 'my_trashcan/register.html', locals())

            else:
                same_name_user = models.User.objects.filter(name=username)

                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'

                    return render(request, 'my_trashcan/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)

                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'my_trashcan/register.html', locals())

                new_user = models.User.objects.create()
                new_user.name = username
                # new_user.password = password1
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.selfdom = set
                new_user.save()
                return redirect('/ash/getLogin')  # 自动跳转到登录页面

    Register_re = Register()
    return render(request, 'my_trashcan/register.html',locals())

#登陆
def getLogin(request):

    if request.session.get('is_login', None):
        return redirect('/ash/getIndex')

    if request.method == "POST":

        Login_log = Login(request.POST)
        message = "请检查填写的内容！"

        if Login_log.is_valid():
            username = Login_log.cleaned_data['username']
            password = Login_log.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/ash/getIndex')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'my_trashcan/login.html', locals())

    Login_log = Login()

    return render(request, 'my_trashcan/login.html',locals())


# 退出登陆
def exitLogin(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/ash/getIndex")
    request.session.flush()
    return redirect("/ash/getIndex")


# 个性签名
# def getPersonalized(request):
#
#     if request.session.get('is_login', None):
#
#         username = request.session.get('user_name')
#         author = models.User.objects.get(name=username)
#         personalized = author.selfdom
#
#
#     return render(request, 'my_trashcan/index.html',locals())










#设置
def getSet(request):
    return render(request, 'my_trashcan/set.html')



# 用哈希加密
def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
