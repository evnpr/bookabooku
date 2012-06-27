from listbook.models import Book
from django.db.models import Q

def getListBook(inp_book):
    books = Book.objects.filter(
        Q(judul__contains=inp_book)|
        Q(tipe__contains=inp_book)|Q(seri__contains=inp_book)
        )
    return books
