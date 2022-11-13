from django.shortcuts import render, redirect, get_object_or_404
from photos.forms import PhotoForm
from photos.models import Photo
from django.contrib import messages
from colorthief import ColorThief
import colorsys

# Create your views here.
def main_page(request):
    return render(
        request=request,
        template_name="main.html",
    )

def get_dom_col(photo_):
    dom_col = ColorThief(photo.image).get_color(1)


def photos_list(request):
    photos = Photo.objects.all()
    return render(request, 'photos-list.html', {"photos": photos })

def add_photo(request):
    context = {}
    if request.method == 'POST':
        form = PhotoForm(request.POST , request.FILES)
        if  form.is_valid():
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get('image')
            album = form.cleaned_data.get('album')
            dom_color = ColorThief(image)
            obj = Photo.objects.create(
                title=title,
                image=image,
                album=album
            )
            obj.save()
            print(image)
            print(dom_color)
            return redirect('photos:photos_list')
    else:
        form = PhotoForm()
    context['form']= form
    return render(request, 'photo-add.html', context)

def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    photo.delete()
    return redirect('photos:photos_list')

def update_photo(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    form = PhotoForm(request.POST or None, instance= photo)
    dom_color = ColorThief(photo.image).get_color(1)
    dom_col_in_hex = f'#{dom_color[0]:02x}{dom_color[1]:02x}{dom_color[2]:02x}'
    if form.is_valid():
        print(photo.album)
        print('zwalidowano')
        form.save()
        return redirect('photos:photos_list')
    return render(request, 'update-photo.html', {"photo": photo, "form":form, "dom_col_in_hex":dom_col_in_hex})

def get_photo_detail(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    print(photo.album)

    return render(request, 'update-photo.html', {"photo": photo})