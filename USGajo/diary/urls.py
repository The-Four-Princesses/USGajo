from django.contrib import admin
from django.urls import path
from . import views

#for image upload
from django.conf.urls.static import static
from django.conf import settings

#http://127.0.0.1:8000/diary/
app_name = 'diary'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/', views.diaryList, name='diaryList'), #blog
    path('diary/<int:pk>/', views.diaryDetail, name='diaryDetail'), #posting
    path('diary/diaryWrite/', views.diaryWrite),
    path('diary/<int:pk>/update', views.diaryUpdate, name='diaryUpdate'),
    path('diary/<int:pk>/delete', views.diaryDelete, name='diaryDelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)