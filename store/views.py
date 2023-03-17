from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class BaseView(View):
    my_view = {}
    my_view['products'] = Product.objects.all()
    my_view['carousels'] = Carousel.objects.all()
    my_view['blocks'] = Block.objects.all()
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

# class SigninView(BaseView):
#     def get(self, request):
#
#         if request.method == "POST":
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 name = user.username
#                 messages.success(request, "Login Sucessful!")
#                 return redirect('home')
#
#
#             else:
#                 messages.error(request, "Username or Password Does not match")
#                 return redirect('home')
#
#         return render(request, 'signin.html',self.my_view)

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            name = user.username
            messages.success(request,"Login Sucessful!")
            return render(request,'index.html',{"name": name})


        else:
            messages.error(request,"Username or Password Does not match")
            return redirect('/signin')


    return render(request,'signin.html')
def signup(request):

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'The email is already taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                messages.success(request, "Account Created sucessfully!")
                return redirect('/signin')
        else:
            messages.error(request, 'Password does not match')
    context = {}
    return render(request,'signup.html', context)
def signout(request):
    logout(request)
    messages.success(request,"Logged out Sucessfully!")
    return redirect('home')