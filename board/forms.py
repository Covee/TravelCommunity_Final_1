from django_countries.widgets import CountrySelectWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('name', 'country')
        widgets = {'country': CountrySelectWidget()}