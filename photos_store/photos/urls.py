from django.urls import path
from .views import photos_list, add_photo, delete_photo, update_photo, get_photo_detail

app_name="photos"
urlpatterns = [
    path('photos/', photos_list, name="photos_list"),
    path('photos/', add_photo, name='photos_add'),
    path('photos/<photo_id>/', get_photo_detail, name='photo_detail'),
    path('photos/<photo_id>/', update_photo, name='update_photo'),
    path('photos/<photo_id>', delete_photo, name='delete_photo'),

]


