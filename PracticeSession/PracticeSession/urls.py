from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from  django.conf.urls.static import static
urlpatterns = [
    path('',include('studentrecord.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('mycaptcha/',include("mycaptcha.urls")),
    path('/captcha', include("captcha.urls"))
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)