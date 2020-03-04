from  django import forms
from captcha.fields import CaptchaField


# 登陆
class Login(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "Username",}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "password",}))
    captcha = CaptchaField(label='验证码')

# 注册
class Register(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': "username",}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "password",}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "password",}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': "Email",}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    # set = forms.CharField(label='个性签名',widget=forms.Textarea(attrs={'placeholder': "Ersonalized signature",}),max_length=300,)#文本
    set = forms.CharField(label="个性签名", max_length=300,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ersonalized signature", }))
    captcha = CaptchaField(label='验证码')

# 垃圾桶
class Trashcan(forms.Form):
    pass

# 提交垃圾
class Post_Trashcan(forms.Form):
    pass

# 设置
class Set(forms.Form):
    pass