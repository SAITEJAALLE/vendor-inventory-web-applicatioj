from django import forms
from .models import Product
from .models import Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price']
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if 'user' in kwargs:
            self.fields['vendor'].queryset = kwargs['user'].vendorprofile_set.all()

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']
    
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()