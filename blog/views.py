from django.shortcuts import render

posts = [
    {
        'title': 'عنوان التدوينة',
        'content': 'محتوى التدوينة',
        'date': '2020-1-1',
        'author': 'المؤلف الاول',
    },
    {
        'title': 'عنوان التدوينة',
        'content': 'محتوى التدوينة',
        'date': '2020-1-1',
        'author': 'المؤلف الاول',
    },
]


def home(r):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
    }
    return render(r, 'index.html', context)


def about(r):
    context = {
        'title': 'من أنا',
    }
    return render(r, 'about.html', context)
