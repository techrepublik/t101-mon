from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from pythonping import ping
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template

from .models import Client, Status
from .forms import ClientForm, StatusForm

from .utils import render_to_pdf

def list_client(request):
    clients = Client.objects.all()
    return render(request, 'clients/clients.html', {'clients': clients})

def new_client(request):
    if request.method == 'POST':
        form    = ClientForm(request.POST)
    else:
        form    = ClientForm()
    return save_client(request, form, 'clients/client_new.html')

def edit_client(request, pk):
    client      = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form    = ClientForm(request.POST, instance=client)
    else:
        form    = ClientForm(instance=client)
    return save_client(request, form, 'includes/partial_client_update.html')

def save_client(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            clients = Client.objects.all()
            data['client_list'] = render_to_string('includes/partial_client_list.html', {'clients':clients})
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def create_client(request):
    if (request.method == 'POST'):
        form = ClientForm(request.POST)
    else:
        form = ClientForm()
    return save_client(request, form, 'includes/partial_client_create.html')

# def update_client(request, pk):
#     client = get_object_or_404(Client, pk=pk)
#     if request.method == 'POST':
#         form = ClientForm(request.POST, instance=client)
#     else:
#         form = ClientForm(instance=client)
#     return save_client(request, form, 'includes/partial_client_update.html')

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    data = dict()
    if request.method == 'POST':
        client.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        clients = Client.objects.all()
        data['client_list'] = render_to_string('includes/partial_client_list.html', {
            'clients': clients
        })
    else:
        context = {'client': client}
        data['html_form'] = render_to_string('includes/partial_client_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def monitor_client(request):
    data = dict()
    clients = Client.objects.all()
    return render(request, 'monitors/monitors.html', {'clients': clients})

def monitor_client_ajax(request):
    data = dict()
    clients = Client.objects.all()
    data['client_list'] = render_to_string('monitors/partial_monitor_list.html', {'clients':clients})
    return JsonResponse(data)

def monitor_ping(request, pk):
    data = dict()
    client = get_object_or_404(Client, pk=pk)
    pingz = ping(client.client_ip, verbose=True, count=10)
    ping_list = pingz
    data['html_form'] = render_to_string('monitors/partial_ping_pop.html', {'pings':ping_list, 'client':client}, request=request)
    ping_list = ''
    return JsonResponse(data)

#status
def status_list(request):
    statuses = Status.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(statuses, 10)

    try:
        statusex = paginator.page(page)
    except PageNotAnInteger:
        statusex = paginator.page(1)
    except EmptyPage:
        statusex = paginator.page(paginator.num_pages)
    
    flag1 = True

    return render(request, 'status/statuses.html', {'statuses': statusex, 'flag1':flag1})
    # data['status_list'] = render_to_string('status/statuses.html', {'statuses': statuses})
    # return JsonResponse(data)

def create_status(request, client):
    data = dict()
    if (request.method == 'POST'):
        form  = StatusForm(request.POST)
        if (form.is_valid()):
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = StatusForm()
    flag1 = False
    context = {'form': form, 'client': client, 'flag1': flag1}
    data['html_form'] = render_to_string('status/partial_status_create.html', context, request=request)
    return JsonResponse(data)

def create_status1(request):
    data = dict()
    if (request.method == 'POST'):
        form  = StatusForm(request.POST)
        if (form.is_valid()):
            form.save()
            data['form_is_valid'] = True
            statuses = Status.objects.all()
            page = request.GET.get('page', 1)
            paginator = Paginator(statuses, 10)

            try:
                statusex = paginator.page(page)
            except PageNotAnInteger:
                statusex = paginator.page(1)
            except EmptyPage:
                statusex = paginator.page(paginator.num_pages)
            data['status_list'] = render_to_string('status/partial_status_list.html', {'statuses':statusex})
        else:
            data['form_is_valid'] = False
    else:
        form = StatusForm()
    context = {'form': form}
    data['html_form'] = render_to_string('status/partial_status_create_1.html', context, request=request)
    return JsonResponse(data)

def update_status(request, pk):
    data = dict()
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            statuses = Status.objects.all()
            data['status_list'] = render_to_string('status/partial_status_list.html', {'statuses': statuses})
        else:
            data['form_is_valid'] = False
    else:
        form = StatusForm(instance=status)
    
    context = {'form': form}
    data['html_form'] = render_to_string('status/partial_status_update.html', context, request=request)
    return JsonResponse(data)

def delete_status(request, pk):
    data = dict()
    status  = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        data['form_is_valid'] = True
        statuses = Status.objects.all()
        data['status_list'] = render_to_string('status/partial_status_list.html', {'statuses': statuses})
    else:
        data['form_is_valid'] = False
        context = {'status': status}
        data['html_form'] = render_to_string('status/partial_status_delete.html', context, request=request)
    
    return JsonResponse(data)

def client_pdf(request):
    clients = Client.objects.all()
    pdf_file = render_to_pdf('clients/clients_pdf.html', {'clients':clients})
    return HttpResponse(pdf_file, content_type='application/pdf')

    # if pdf_file:
    #     response = HttpResponse(pdf_file, content_type='application/pdf')
    #     filename = "ClientList.pdf"
    #     content = "inline; filename='%s'" %(filename)
    #     response['Content-Disposistion'] = content
    #     return content
    # return HttpResponse('Not Found')

    