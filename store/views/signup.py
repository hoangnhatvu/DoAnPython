from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Vui lòng nhập Họ của bạn."
        elif (not customer.last_name):
            error_message = 'Vui lòng nhập Tên của bạn.'
        elif (not customer.phone):
            error_message = 'Vui lòng nhập số điện thoại.'
        elif not 10 <= len(customer.phone) <= 15:
            error_message = 'Số điện thoại không hợp lệ.'
        elif len (customer.password) < 5:
            error_message = 'Mật khẩu phải có độ dài hơn 5 ký tự'
        elif len (customer.email) < 5:
            error_message = 'Địa chỉ Email không hợp lệ.'
        elif customer.isExists ():
            error_message = 'Tài khoản Email này đã tồn tại !!!'
        # saving

        return error_message
