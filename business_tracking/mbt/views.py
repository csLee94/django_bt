from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from .models import Inbound, InboundHistory, Contract, BillingRevenue, ProductHistory
from .forms import AddbillingRevenue, InboundForm, InboundToContractForm, AddInboundHistory, Contract, ContractForm, AddProduct

def inbound(request):
    page = request.GET.get("page", "1")
    inbound_lst = Inbound.objects.order_by("-created_at")
    paginator = Paginator(inbound_lst, 10) # 10 records per pages
    page_obj = paginator.get_page(page)
    context = {'inbound_list':page_obj}
    return render(request, 'mbt/inbound_list.html', context)

def inbound_detail(request, inbound_id):
    inbound = Inbound.objects.get(id=inbound_id)
    inbound_history = InboundHistory.objects.filter(inbound_id=inbound_id).order_by("-action_created_at")
    context = {'inbound':inbound, "inbound_history":inbound_history}
    return render(request, 'mbt/inbound_detail.html', context)

def create_inbound(request):
    if request.method == 'POST':
        form = InboundForm(request.POST)
        if form.is_valid():
            inbound_record = form.save(commit=False)
            inbound_record.created_at = timezone.now()
            inbound_record.inbound_title = "%s_%s 문의" % (form.cleaned_data.get("client_name"), form.cleaned_data.get("requested_summary"))
            inbound_record.status = "인바운드"
            inbound_record.save()
            return redirect('mbt:inbound')
    else:
        form = InboundForm()
    context = {'form': form}
    return render(request, 'mbt/inbound_form.html', context)
    # form = InboundForm()
    # return render(request, 'mbt/inbound_form.html', {'form':form})

def add_inbound_history(request, inbound_id):
    inbound = get_object_or_404(Inbound, pk=inbound_id)
    if request.method == "POST":
        form = AddInboundHistory(request.POST)
        if form.is_valid():
            inbound_act = form.save(commit=False)
            inbound_act.action_created_at= timezone.now()
            inbound_act.inbound_id = inbound_id
            inbound_act.save()
            return redirect("mbt:inbound_detail", inbound_id=inbound_id)
    else:
        return HttpResponseNotAllowed("Only POST is possible")
    context = {'inbound':inbound, 'form':form}
    return render(request, "mbt/inbound_detail.html", context)

def inbound_to_contract(request, inbound_id):
    inbound = get_object_or_404(Inbound, pk=inbound_id)
    if request.method == "POST":
        form = InboundToContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.contracted_at= timezone.now()
            contract.status = "progress"
            contract.inbound_id = inbound_id
            contract.save()
            return redirect("mbt:contract_detail", contract_id=contract.id)
    else:
        return HttpResponseNotAllowed("Only POST is possible")
    context = {'inbound':inbound, 'form':form}
    return render(request, "mbt/inbound_detail.html", context)

def contract(request):
    page = request.GET.get("page", "1")
    contract_lst = Contract.objects.order_by("-contracted_at")
    paginator = Paginator(contract_lst, 10) # 10 records per pages
    page_obj = paginator.get_page(page)
    context = {'contract_list':page_obj}
    return render(request, 'mbt/contract_list.html', context)

def create_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract_record = form.save(commit=False)
            contract_record.contracted_at = timezone.now()
            contract_record.status = "진행중"
            contract_record.inbound_id = None
            contract_record.save()
            return redirect('mbt:contract')
    else:
        form = ContractForm()
    context = {'form': form}
    return render(request, 'mbt/contract_form.html', context)

def contract_detail(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    billing_rev = BillingRevenue.objects.filter(contract_id=contract_id)
    product = ProductHistory.objects.filter(contract_id=contract_id)
    context = {'contract':contract, 'billing_rev':billing_rev, 'product_lst':product}
    return render(request, 'mbt/contract_detail.html', context)

def add_product(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    if request.method == "POST":
        form = AddProduct(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.contract_id = contract_id
            product.created_at= timezone.now()
            product.save()
            return redirect("mbt:contract_detail", contract_id=contract_id)
    else:
        return HttpResponseNotAllowed("Only POST is possible")
    context = {'contract':contract, 'form':form}
    return render(request, "mbt/contract_detail.html", context)

def add_billing_revenue(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    if request.method == "POST":
        form = AddbillingRevenue(request.POST)
        if form.is_valid():
            billing_rev = form.save(commit=False)
            billing_rev.contract_id = contract_id
            billing_rev.created_at= timezone.now()
            billing_rev.status = "requested"
            billing_rev.save()
            return redirect("mbt:contract_detail", contract_id=contract_id)
    else:
        return HttpResponseNotAllowed("Only POST is possible")
    context = {'contract':contract, 'form':form}
    return render(request, "mbt/contract_detail.html", context)
