from django.shortcuts import render,redirect
from .models import Book, Image, Author, Language, Category
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from comment.models import Comment, Like
from comment.forms import CommentForm
# Create your views here.


def home(request):
    top_book = Book.objects.order_by('-rating_avg')
    ordering = request.GET.get('ordering')

    if ordering:
        books = Book.objects.all().order_by(ordering)
    else:
        books = Book.objects.all()

    p = Paginator(books, 6)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object

    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(1)

    context = {
        'book': page_obj,
        'top_book': top_book,
    }

    return render(request, 'book_list.html', context)


def detail(request, slug):
    book = Book.objects.get(slug=slug)
    img = Image.objects.filter(book=book)
    comment = Comment.objects.filter(book=book)
    category_book = Book.objects.filter(category=book.category)
    s = comment
    a = 0
    for i in s:
        a += i.rating
    try:
        book.rating_avg = round(a/comment.count())
    except ZeroDivisionError:
        book.rating_avg=0
    book.views += 1
    book.save()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.book = book
            f.save()
    else:
        form = CommentForm()


    context = {
        'book': book,
        'img': img,
        'comment': comment,
        'category_book': category_book,
        'form': form,
    }
    return render(request, 'book_detail.html', context)


def like(request, slug):
    user = request.user
    book = Book.objects.get(slug=slug)
    current_like = book.like

    liked = Like.objects.filter(user=user, book=book).count()

    if not liked:
        like = Like(user=user, book=book)
        like.save()
        current_like += 1
    else:
        likedd = Like.objects.filter(user=user, book=book)
        likedd.delete()
        current_like -= 1

    book.like = current_like
    book.save()

    return redirect('detail', book.slug)


def author_book(request, slug):
    author = Author.objects.get(first_name=slug)
    books = Book.objects.filter(author=author)

    context = {
        'book':books,
    }

    return render(request, 'book_list.html', context)


def language_book(request, slug):
    language = Language.objects.get(slug=slug)
    books = Book.objects.filter(language=language)

    context = {
        'book': books,
    }

    return render(request, 'book_list.html', context)


def category_book(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)

    context = {
        'book': books,
    }

    return render(request, 'book_list.html', context)




