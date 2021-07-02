from .. import models
from django import forms

class NewProductForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            'id': 'titleInput',
            'placeholder': 'Title'}),
        max_length = 32, 
        label="Title",
        label_suffix="")
    
    author = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            'id': 'authorInput',
            'placeholder': 'Author Name'}),
        max_length = 18, 
        label="Author Name",
        label_suffix="")

    category= forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-select',
            'id': 'categoryInput'}),
        label="Category",
        label_suffix="",
        queryset=models.Categories.objects.all(),
        empty_label="Select a Category"
        )
        
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control',
            'id': 'description',
            'placeholder': 'Description',
            'style': 'height: 100px;'}),
        max_length = 200, 
        label="Description",
        label_suffix="")
    

    image_URl = forms.ImageField(
        widget=forms.FileInput(
            attrs={'class': 'form-control',
            'id': 'imgInput'}),
        max_length = 200, 
        label="Upload Image",
        label_suffix="")

    price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class':'form-control',
            'id': 'priceInput',
            'placeholder': 'Price',
            'min': '0'}),
        label="Price",
        label_suffix=""       
    )

    class Meta:
        model = models.Products
        fields = ['title', 'author', 'description', 'category', 'image_URl', 'price']

    


    



