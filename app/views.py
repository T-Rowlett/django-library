from django.shortcuts import render, redirect
from app.models import Book, Transaction
from django.contrib import messages

# Create your views here.


def home(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def borrow_book(request, id):
    book = Book.objects.get(id=id)
    if book.in_stock:
        transaction = book.transaction_set.create(False)
        messages.success(request, "Borrowed <title> by <author>")
        return redirect("book_list.html", transaction.id)
    elif book.in_stock:
        book = Book.objects.get(id=id)
        transaction = book.transaction_set.create(True)
        messages.error(request, "<title> by <author> is unavailable")
        return redirect("book_list.html", transaction.id)


def return_book(request, id):
    book = Book.objects.get(id=id)
    if book.in_stock:
        transaction = book.transaction_set.create(True)
        messages.success(request, "returned <title> by <author>")
        return redirect("transaction_detail.html", transaction.id)
    elif book.in_stock:
        book = Book.objects.get(id=id)
        transaction = book.transaction_set.create(False)
        messages.error(request, "<title> by <author> is unavailable")
        return redirect("transaction_detail.html", transaction.id)
