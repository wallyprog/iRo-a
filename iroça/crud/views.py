from django.shortcuts import render,redirect, get_object_or_404
from django.forms import ModelForm
from .models import *

class ProdutoForm(ModelForm):
    class Meta:
        model= Produto
        fields= ['nome','descricao','quantidade','data_colheita']
def cadastrar_produto(request,template_name='produto_form.html'):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request,template_name,{'form':form})

def produto_list(request, template_name='produto_list.html'):
    query = request.GET.get("busca")
    if query:
        produto = Produto.objects.filter(nome__icontains=query)
    else:
        produto = Produto.objects.all()
    produtos = {'lista': produto}
    return render(request, template_name, produtos)

def editar_produto(request, pk, template_name='produto_form.html'):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, template_name, {'form': form})

def remover_produto(request, pk, template_name='produto_delete.html'):
    produto = Produto.objects.get(pk = pk)
    if request.method=='POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, template_name, {'produto': produto})