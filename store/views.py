from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *

# Create your views here.
class BaseView(View):
    my_view = {}
    my_view['products'] = Product.objects.all()

    # my_view['brands'] = Brand.objects.all()
    # my_view['sales'] = Product.objects.filter(labels='sale')
    # my_view['no_counts'] = NoCart.objects.all()



class HomeView(BaseView):
    def get(self,request):
        self.my_view
        self.my_view['carousels'] = Carousel.objects.all()
        self.my_view['blocks'] = Block.objects.all()
        self.my_view['products'] = Product.objects.all()



        return render(request,'index.html',self.my_view)


class ShopView(BaseView):
    def get(self,request):
        self.my_view
        return render(request,'product.html',self.my_view)

class ProductDetailView(BaseView):
    def get(self,request):
        self.my_view
        self.my_view['products'] = Product.objects.all()
        self.my_view['categories'] = Category.objects.all()


        return render(request,'product-detail.html',self.my_view)




class CartView(BaseView):
    def get(self,request):
        self.my_view
        return render(request,'shopping-cart.html',self.my_view)

class ContactView(BaseView):
    def get(self,request):
        self.my_view
        return render(request,'contact.html',self.my_view)

class AboutView(BaseView):
    def get(self,request):
        self.my_view
        return render(request,'about.html',self.my_view)