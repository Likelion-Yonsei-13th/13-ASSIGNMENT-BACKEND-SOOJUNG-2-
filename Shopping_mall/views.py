from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            owner=request.user
        )
        return redirect('product_list')
    return render(request, 'product_form.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.owner != request.user:
        return HttpResponseForbidden("수정 권한이 없습니다.")

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.save()
        return redirect('product_detail', pk=pk)
    return render(request, 'product_form.html', {'product': product})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.owner != request.user:
        return HttpResponseForbidden("삭제 권한이 없습니다.")

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return redirect('product_detail', pk=pk)
