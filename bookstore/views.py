from django.shortcuts import render,redirect
# Create your views here.
from .models import Book, Customer, Order
from .forms import OrderForm, CreateNewUser
from .filters import OrderFilter
from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import notLoggedUser, forAdmin, allowedUsers
from django.contrib.auth.models import Group
#_____________________________________________
@login_required(login_url='login')
@forAdmin
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    pending_orders = orders.filter(status='Pending').count()
    delevired_orders = orders.filter(status='Delivered').count()
    in_progress_orders = orders.filter(status='Processing').count()
    cancelled_orders = orders.filter(status='Cancelled').count()
    context = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delevired_orders': delevired_orders,
        'in_progress_orders': in_progress_orders,
        'cancelled_orders': cancelled_orders
    }
    return render(request, 'bookstore/dashboard.html', context)


@login_required(login_url='login')
# @allowedUsers(allowedGroups='admin')
@forAdmin
def books(request):
    books = Book.objects.all()
    return render(request, 'bookstore/books.html', {'books': books})


@login_required(login_url='login')
# @allowedUsers(allowedGroups='admin')
@forAdmin
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'bookstore/customers.html',{'customers': customers})


@login_required(login_url='login')
# @allowedUsers(allowedGroups='admin')
@forAdmin
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    searchFilter = OrderFilter(request.GET, queryset=orders)
    orders = searchFilter.qs
    context = {'orders': orders, 'customer': customer , 'searchFilter': searchFilter}
    return render(request, 'bookstore/customer.html', context)


@login_required(login_url='login')
@allowedUsers(allowedGroups='admin')
def create(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'bookstore/addOrder.html',{'form': form})


@login_required(login_url='login')
@allowedUsers(allowedGroups='admin')
def createorder(request, pk):
    orderFormSet = inlineformset_factory(Customer, Order, fields=('book', 'tags', 'status','note'), extra=2)
    customer = Customer.objects.get(id=pk)
    form = orderFormSet(instance=customer)
    if request.method == 'POST':
        form = orderFormSet(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'bookstore/addOrder.html',{'form': form})


@login_required(login_url='login')
@allowedUsers(allowedGroups='admin')
def update(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'bookstore/addOrder.html',{'form': form})


@login_required(login_url='login')
@allowedUsers(allowedGroups='admin')
def delete(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    return render(request, 'bookstore/deleteOrder.html',{'order': order})


@notLoggedUser
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')
    return render(request, 'users/login.html')

@login_required(login_url='login')
def logoutPage(request, username=None):
    logout(request)
    return redirect('login')

# @notLoggedUser
def registerPage(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customers')
            user.groups.add(group)
            return redirect('login')
    context={'form': form}
    return render(request, 'users/register.html', context)

def userProfile(request):
    context = {}
    return render(request, 'users/userProfile.html' , context)