from book.models import Category, Author, Language


def category(request):
    categories = Category.objects.all()
    context = {
        'category':categories,
    }
    return context


def author(request):
    authors = Author.objects.all()

    return {'authors': authors}


def language(request):
    language = Language.objects.all()

    return {'language': language}