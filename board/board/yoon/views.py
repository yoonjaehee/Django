from django.shortcuts import render, redirect
from .models import Document, User

def documentlist(request):
    docs = Document.objects.all()
    return render(request,'index.html',{'docs':docs})

def createDocument(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.POST['user']
        author = User.objects.get_or_create(name=user)
        doc = Document.objects.create(title=title, content=content, author=author[0])
        return redirect('detailview', doc.id)
    else:
        return render(request,'edit.html')

def documentdetail(request, id):
    doc = Document.objects.get(id=id)
    return render(request,'detail.html',{'doc':doc})
# Create your views here.

def updateDocument(request, id):
    if(request.method == 'POST'):
        # 수정, 리다이렉트
        title = request.POST['title']
        content = request.POST['content']
        user = request.POST['user']
        author = User.objects.get_or_create(name=user)
        Document.objects.filter(id=id).update(title=title,content=content,author=author[0])
        return redirect('detailview', id) # 컨텍스 넣기
    else:
        # doc find
        return render(request, 'update.html',
            # doc: doc
        )

def deleteDocument(request, id):
    Document.objects.filter(id=id).delete()
    return redirect('documentlist')