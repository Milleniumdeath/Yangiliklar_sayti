
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('<slug:slug>/', ArticleDetailsView.as_view(), name='article-detail'),
    path('category/<int:pk>/', CategoryArticleView.as_view(), name='category-articles'),
    path('contact/', ContactView.as_view(), name='contact')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)