from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

from django.http import HttpResponse
from django.http import JsonResponse
from .models import Item
# Create your views here.

# 이 함수를 실행하면 ()안의 내용을 클라이언트에게 전송
def index(request):
    return HttpResponse('<h3>Hello Django</h3>')  # Main Page

def menu(request):
    # menu.html 파일을 출력하는데 파일에 message 라는 이름으로 data를 전달
    return render(request, 'menu.html', {'message': 'data'})

def detail(request, num):
    return HttpResponse(str(num))

def search(request):
    # keyword = request.get["query"]
    keyword = request.GET.get("query", "default value")  # 이렇게 하면 예외 발생 X 
    return HttpResponse(keyword)

# 전체 보기 요청을 처리하는 함수
def work(request):   
    # index.html 파일로 출력하는데, message라는 이름으로 data를 전달
    # return render(request, 'index.html', {'message': data})  # message 매개변수로 HTML로 전달

    # Item 클래스와 연결된 테이블의 모든 데이터를 가져오기
    data = Item.objects.all() # all() return -> Instance를 담고 있는 list

    # 여러 개의 데이터이므로 리스트에 저장
    data_list = []
    for item in data:
        data_list.append(itemToDictionary(item))

    # 리스트를 json으로 리턴, 리스트를 직접 출력할 수 없다. -> dict로 변환해서 제공
    # return JsonResponse({"data":data_list})

def itemToDictionary(item:Item) -> dict:
    output = {}  # dict 생성
    
    # 인스턴스 속성을 딕셔너리에 저장
    output["itemId"] = item.itemId
    output["itemName"] = item.itemName
    output["price"] = item.price
    output["description"] = item.description
    output["pictureURL"] = item.pictureURL

    return output

# 상세 보기 요청을 JSON으로 처리 -> 항상 URl 뒤에 Primary_Key 값이 붙기에, 매개변수로 처리해줘야 한다. 
def get(request, itemid):
    item = Item.objects.get(itemId = itemid)  # get() return -> Instance 
    return JsonResponse(itemToDictionary(item))

# 상세 보기 요청을 처리하는 함수
def detail_page(request, itemid):
    item = Item.objects.get(itemId = itemid)
    return render(request, 'detail.html', {'data': item})


# GET 요청이 오면 함수를 호출
@api_view(['GET'])
def api(request):
    return Response("Hello REST API")

@api_view(['GET', 'POST'])
def booksAPI(request):
    # GET 방식의 처리 - 전체 조회를 요청하는 경우
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)  # 브라우저에 맞는 형태로 변환
        return Response(serializer.data)
    # POST 방식의 처리 - 삽입을 요청하는 경우
    elif request.method == 'POST':
        # 클라이언트에서 전송된 데이터를 가지고 Model 인스턴스 생성
        serializer = BookSerializer(data = request.data)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # 실패 시, 오류 출력
        return Response(serializer.errors)
    
    # PUT 방식의 처리 - 변경을 요청하는 경우
    elif request.method == 'PUT':
        pass