from django import forms
from photos.models import Photo, Album


class PhotoForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=None)
    image = forms.ImageField()
    class Meta:
        model = Photo
        fields = "__all__"
        fields = ["title", "album", "image"]

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.all()