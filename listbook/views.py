from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from listbook.models import Book
from django.db.models import Q
from django.http import HttpResponse
from listbook.util import getListBook

def home(request):
  data = {}
  data.update(csrf(request))
  if request.method == "POST":
    inp_book = request.POST.get('searchbook')
    if not inp_book:
      data['empty'] = 'anda belum memasukkan query'
      return render_to_response('st.html', data)
    books = getListBook(inp_book)
    data['query'] = inp_book
    data['numberOfBook'] = books.count()
    if not books:
      data['empty'] = 'maaf tidak tersedia'
    data['books'] = books
  return render_to_response('st.html', data)

def search(request):
  test = request.POST.get('searchbook')
  if test:
    books = Book.objects.filter(judul__contains=test).values('judul').distinct()[:8]
    data = {}
    data.update(csrf(request))
    data['books'] = books
    return render_to_response("test.html", data)

def about(request):
  data = {}
  data.update(csrf(request))
  if request.method == "POST":
    inp_book = request.POST.get('searchbook')
    if not inp_book:
      data['empty'] = 'anda belum memasukkan query'
      return render_to_response('aboutus.html', data)
    books = getListBook(inp_book)
    data['query'] = inp_book
    data['numberOfBook'] = books.count()
    if not books:
      data['empty'] = 'maaf tidak tersedia'
    data['books'] = books
  return render_to_response('aboutus.html', data)
