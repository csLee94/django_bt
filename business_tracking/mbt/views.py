from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from .models import Inbound
from .forms import InboundForm, InboundToContractForm

def inbound(request):
    page = request.GET.get("page", "1")
    inbound_lst = Inbound.objects.order_by("-created_at")
    paginator = Paginator(inbound_lst, 10) # 10 records per pages
    page_obj = paginator.get_page(page)
    context = {'inbound_list':page_obj}
    return render(request, 'mbt/inbound_list.html', context)

def inbound_detail(request, inbound_id):
    inbound = Inbound.objects.get(id=inbound_id)
    context = {'inbound':inbound}
    return render(request, 'mbt/inbound_detail.html', context)

def create_inbound(request):
    if request.method == 'POST':
        form = InboundForm(request.POST)
        if form.is_valid():
            inbound_record = form.save(commit=False)
            inbound_record.created_at = timezone.now()
            inbound_record.save()
            return redirect('mbt:inbound')
    else:
        form = InboundForm()
    context = {'form': form}
    return render(request, 'mbt/inbound_form.html', context)
    # form = InboundForm()
    # return render(request, 'mbt/inbound_form.html', {'form':form})

def inbound_to_contract(request, inbound_id):
    inbound = get_object_or_404(Inbound, pk=inbound_id)
    if request.method == "POST":
        form = InboundToContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.created_at= timezone.now()
            contract.status = "수주계약"
            contract.inbound = inbound
            contract.save()
            return redirect("mbt:inbound_detail", inbound_id=inbound.id)
    else:
        return HttpResponseNotAllowed("Only POST is possible")
    context = {'inbound':inbound, 'form':form}
    return render(request, "mbt/inbound_detail.html", context)

# def create_inbound(request):
#     inbound = Inbound(
#         created_at=timezone.now(),
#         inbound_title=request.POST.get('inbound_title'),
#         client_name=request.POST.get("client_name"),
#         client_contact_point=request.POST.get("client_contact_point"),
#         dept=request.POST.get("dept")
#     )
#     inbound.save()
#     return redirect('mbt:inbound')