from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from anushree.decorators import group_required
from sliderimages.forms import SliderImageForm
from sliderimages.models import SliderImage


@group_required('admin', raise_exception=True)
def create_slider_image(request):
    context = {}

    form = SliderImageForm(request.POST or None, files=request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            # form.save()

            messages.success(request, 'Successfully created slider image.')
            return redirect('sliderimages:create')

    context['form'] = form
    return render(request, 'sliderimages/create.html', context)


@group_required('admin', raise_exception=True)
def list_slider_image(request):
    context = {}
    data = SliderImage.objects.all()

    context['datas'] = data
    return render(request, 'sliderimages/list.html', context)


@group_required('admin', raise_exception=True)
def edit_slider_image(request, slug):
    context = {}

    try:
        data = SliderImage.objects.get(slug=slug)
    except SliderImage.DoesNotExist as e:
        messages.error(request, str(e))
        return redirect('sliderimages:list')

    form = SliderImageForm(instance=data)

    if request.method == 'POST':
        form = SliderImageForm(data=request.POST, files=request.FILES, instance=data)
        if form.is_valid():
            form.save()

            messages.success(request, 'Successfully created slider image.')
            return redirect('sliderimages:edit', slug=slug)

    context['form'] = form
    context['thumbnail'] = data.thumbnail.url
    return render(request, 'sliderimages/create.html', context)


@group_required('admin', raise_exception=True)
def delete_slider_image(request, slug):
    try:
        data = SliderImage.objects.get(slug=slug)
    except SliderImage.DoesNotExist as e:
        messages.error(request, str(e))
        return redirect('sliderimages:list')

    data.delete()
    return redirect('sliderimages:list')
