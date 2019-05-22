from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from customer.forms import CustomerForm, ChangePasswordForm
from customer.models import Customer
from orders.models import Cart
from users.models import User


def create_customer(request):
    context = {}
    form = CustomerForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            customer = form.save()

            cart  = Cart.objects.get_or_create(customer=customer)

            messages.success(request, 'Customer with username {} and password {} has been created.'.format(
                customer.user.username, customer.owner.split(' ')[0] + '123'))
            return redirect('customers:create')
        messages.error(request, 'Opps! Unable to create customer.')

    context['form'] = form
    return render(request, 'customers/create.html', context)


def list_customer(request):
    context = {}

    datas = Customer.objects.all()

    context['datas'] = datas
    return render(request, 'customers/list.html', context)


def change_customer_password(request, pk):
    context = {}
    form = ChangePasswordForm(request.POST or None)
    #
    if request.method == 'POST':
        if form.is_valid():
            password = form.cleaned_data
            password = password.get('new_password')

            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.save()

            messages.success(request, 'Successfully changed password for user with username {}.'.format(user.username))
            return redirect('customers:list_customer')
        messages.error(request, 'Unable to change password for the user.')

    context['form'] = form
    return render(request, 'customers/change_password.html', context)


def toggle_user_status(request, pk):
    context = {}
    user = User.objects.get(pk=pk)

    user.is_active = not user.is_active
    user.save()

    if user.is_active:
        messages.success(request, 'User with username {} has been activated'.format(user.username))
    else:
        messages.success(request, 'User with username {} has been deactivated'.format(user.username))

    return redirect('customers:list_customer')
