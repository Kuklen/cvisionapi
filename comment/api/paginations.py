from rest_framework.pagination import PageNumberPagination

class CommentPagination(PageNumberPagination):                #commentlara sayfa yapmak için
    page_size=2   #2 dediğimiz için sayfalarda 2li 2li sıralama yapıyor 3 ders 3 vb.