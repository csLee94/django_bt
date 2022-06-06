from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from .models import Inbound, InboundHistory
from .forms import InboundForm, InboundToContractForm, AddInboundHistory

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
    print("yes")
    context = {'inbound':inbound, "inbound_history":inbound_history}
    print(context)
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

def inbound_to_contract(request, inbound_id):
    # inbound = get_object_or_404(Inbound, pk=inbound_id)
    if request.method == "POST":
        form = InboundToContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.created_at= timezone.now()
            contract.status = "수주계약"
            contract.inbound_id = inbound_id
            contract.save()
            return redirect("mbt:inbound_detail", inbound_id=inbound_id)
    else:
        return HttpResponseNotAllowed("Only POST is possible")
    context = {'inbound':inbound, 'form':form}
    return render(request, "mbt/inbound_detail.html", context)

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
