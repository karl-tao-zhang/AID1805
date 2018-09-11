from django import forms

# TOPIC'S initial display and value
TOPIC_CHOICE = (
    ('1','HAO PING'),
    ('2','ZHONG PING'),
    ('3','CHA PING'),
)

# 表示评论内容的表单控件们
# 评论标题 - 文本框
# Email - Input type='Email'
# Message  - Textarea
# Topic - Select
# isSave - Input type='checkbox'
class RemarkForm(forms.Form):
    # Subject - Input type="text"
    # 创建标题,label : 控件前显示的文本
    subject=forms.CharField(label='Title')
    # Email - Input type="email"
    email = forms.EmailField(label='Email')
    # Message - Textarea
    # widget=forms.Textarea , set the message is a <textarea></textarea>
    # 创建评论内容,widget指定显示为多行文本域
    message = forms.CharField(label='Message',widget=forms.Textarea)
    #topic - <select></select>
    #<select>
        # <option value='1'>HAO PING</option>
        # <option value='2'>ZHONG PING</option>
        # <option value='3'>CHA PING</option>
    # </select>
    # 评论级别,choices指定select中显示的数据
    topic = forms.ChoiceField(label='Topic',choices=TOPIC_CHOICE)
    # ISSAVED Input type='checkbox'
    isSaved = forms.BooleanField(label="IsSaved")


# 创建class表示登录的表单
class LoginForm(forms.Form):
    #文本框,表示用户名
    uname=forms.CharField(label='用户名称')
    #密码框,表示用户密码
    upwd =forms.CharField(label='登录密码',widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    uname = forms.CharField(label='用户名称',max_length=18)
    upwd = forms.CharField(label='用户密码',widget=forms.PasswordInput())
    uage = forms.IntegerField(label='用户年龄',)
    uemail = forms.EmailField(label='电子邮箱',)

class widgetForm(forms.Form):
    uname=forms.CharField(
        label='用户名称'
        widget=forms.TextInput(
            attrs={
                'name':'user_name',
                'placeholder':'请输入用户名称',
                'class':'form-control',
            }
        )
    )
    upwd=forms.CharField(
        label='用户密码'
        widget=forms.PasswordInput(
            attrs={
                'name':'user_upwd',
                'placehold':'请输入用户密码',
                'class':'form-control',
            }
        )
    )


