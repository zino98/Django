from django.contrib import admin
from django.urls import path

# 요청을 처리할 함수가 있는 파일을 import
from myapp import views  # 이대로 써도 문제는 없다. 

urlpatterns = [
    path("admin/", admin.site.urls),  # URL 등록 -> 해당 요청 수행
    # path("users/", admin.site.urls), admin -> 관리자 페이지 (root / 1234)
    path("", views.index), 
    path("menu/", views.menu),  # 127.0.0.1/menu URL 실행
    path("article/<int:num>", views.detail),   # 127.0.0.1/article/num URL 실행
    path("search/", views.search),  # 127.0.0.1/search?query="()" URL 실행
    path("crud/", views.work),
    path("crud/detail/<int:itemid>", views.detail_page),
    path("get/<int:itemid>", views.get),
] 
