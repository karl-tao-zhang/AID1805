from django.conf.urls import url
from .views import *
urlpatterns = [
    # 访问路径是 /01_request/ 的时候,交给request_views去处理
    url(r'^01_request/$',request_views),
    # 访问路径是 /02_meta/ 的时候,交给meta_views去处理
    url(r'^02_meta/$',meta_views),
    # 访问路径是 /03_form/ 的时候,交给form_views去处理
    url(r'^03_form/$',form_views),
    # 访问路径是 /04_get/ 的时候,交给get_views去处理
    url(r'^04_get/$',get_views,name='get'),
    # 访问路径是 /05_post/ 的时候,交给post_views去处理
    url(r'^05_post/$',post_views,name='post'),
    # 访问路径是 /06_login/ 的时候,交给login_views去处理
    url(r'^06_login/$',login_views),
    # 访问路径是 /07_remark/ 的时候,交给remark_views去处理
    url(r'^07_remark/$',remark_views),
    # 访问路径是 /08_userLogin/的时候,交给userLogin_views处理
    url(r'^08_userLogin/$',userLogin_views),
    # 访问路径是 /09_register/的时候,交给register_views处理
    url(r'^09_register/$',register_views),
]