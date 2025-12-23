from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document


# Главная страница - список документов
@login_required
def document_list(request):
    documents = Document.objects.all().order_by('-created_at')
    return render(request, 'main/document_list.html', {'documents': documents})


# Создание документа
@login_required
def document_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # ВАЖНО: Получаем файл из запроса
        file = request.FILES.get('file')

        # Создаем документ, передавая файл
        Document.objects.create(
            title=title,
            content=content,
            file=file,
            author=request.user
        )
        return redirect('home')
    return render(request, 'main/document_create.html')


# Детальный просмотр и действия
@login_required
def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)

    # Обработка кнопок Согласовать/Отклонить
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            document.status = 'approved'
        elif action == 'reject':
            document.status = 'rejected'
        document.save()
        return redirect('home')

    return render(request, 'main/document_detail.html', {'document': document})