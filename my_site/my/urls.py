from django.contrib import admin
from django.urls import path
from django.urls import include # url의 처리를 다른 모듈에게 위임하고자 할 때 사용하는 패키지

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

    path("example/", include("myapp.urls")), # example로 시작하는 url 요청이 오면 myapp 애플리케이션의 urls.py 파일에 처리를 위임
] 
