from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        articles = Article.published_objects.all().order_by('important', '-views')
        articles3 = Article.published_objects.all().order_by('important', '-views')[3:]
        categories = Category.objects.all()
        context = {
            'articles': articles,
            'articles3': articles3,
            'categories':categories,
        }

        return render(request, 'index.html', context)

class ArticleDetailsView(View):
    def get(self, request,slug):
        article = get_object_or_404(Article, slug=slug)
        articles = Article.objects.all()
        comments = Comment.published_objects.filter(article=article)
        context = {
            'article': article,
            'articles': articles,
            'comments': comments,
        }
        return render(request, 'detail-page.html', context)

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        if request.POST.get('name') == '':
            name = 'Anonymous'
        else:
            name=request.POST.get('name')

        Comment.objects.create(
            name=name,
            email=request.POST['email'],
            text=request.POST['text'],
            article=article,
        )
        return self.get(request, slug)

class CategoryArticleView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        articles = Article.published_objects.filter(category=category)
        categories = Category.objects.all()

        context = {
            'category': category,
            'articles': articles,
            'categories': categories
        }
        return render(request, 'category_articles.html', context)

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Majburiy bo‘lmagan email yoki phone validatsiyasi
        if not phone and not email:
            return render(request, 'contact.html', {
                'error': 'Iltimos, kamida email yoki telefon raqam kiriting.'
            })

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        return render(request, 'contact.html', {
            'success': 'Xabaringiz muvaffaqiyatli yuborildi! ✅'
        })



