from django.shortcuts import render, redirect, get_object_or_404
# render->webページを表示　, redirect->post処理後、元のページに戻る、get_object_or_404->データが見つからなかった場合、エラーを表示
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request,'bookapp/book_list.html', {'book_list': books})

def book_detail(request, pk):
    # 指定されたキー(pk)から対応する書籍を取得
    target = get_object_or_404(Book, pk=pk)
    # 表示するs
    return render(request, 'bookapp/book_detail.html', {'book':target})

def book_create(request):
    if(request.method == 'POST'):
        # フォームにPOSTデータを紐付け
        form = BookForm(request.POST)
        if(form.is_valid()):
            #有効なデータなら保存
            form.save()
            return redirect('book_list')
    else:
        #GETの時はからのフォームを送信
        form = BookForm()
    return render(request, 'bookapp/book_form.html',{'form':form, 'title':'書籍登録'})

def book_update(request,pk):
    target = get_object_or_404(Book, pk=pk)
    
    if(request.method == 'POST'):
        form = BookForm(request.POST, instance = target)
        if(form.is_valid()):
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=target)
        
    return render(request, 'bookapp/book_form.html',{'form':form, 'title':'書籍編集'})

def book_delete(request, pk):
    target = get_object_or_404(Book, pk=pk)
    if(request.method == 'POST'):
        target.delete()
        return redirect('book_list')
        
    return render(request, 'bookapp/book_confirm_delete.html',{'title':'書籍編集'})
