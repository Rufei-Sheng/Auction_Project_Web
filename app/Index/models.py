from django.db import models

# Create your models here.


# User table
class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=200)
    paypal_number = models.CharField(max_length=200)# paypay number
    create_time = models.DateTimeField() # regidter time
    update_time = models.DateTimeField(auto_now=True) # update time
    status = models.CharField(max_length=200)  #  active/inactive
    desc = models.CharField(max_length=200)  # the reason for dis-register

# Post product table
class Product(models.Model):
    category= models.CharField(max_length=200) # category 
    sub_category= models.CharField(max_length=200) # sub-category
    product_photo= models.CharField(max_length=200) # product picture 
    product_condition= models.CharField(max_length=200) # product condition: poor   average   good  excellent
    min_price= models.IntegerField() # auction mim price
    start_time= models.DateTimeField() # auction start time
    end_time= models.DateTimeField() # auction end time
    desc= models.CharField(max_length=200)  # description
    delivery= models.CharField(max_length=200)  # whether delivery
    create_time= models.DateTimeField() # post time
    freight=  models.IntegerField()# delivery price

    buy_user_id = models.IntegerField(default=0) # auction person
    end_success_user_id= models.IntegerField(default=0) # end buyer 
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='p_user')



# Liked table
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='l_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='l_product')
    like = models.IntegerField()  # whether liked the product 0/1



# Buy table
class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='b_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='b_product')
    buy_price=  models.IntegerField()  # auction price
    if_success= models.IntegerField()  # whether auction successfully  0/1
    create_time = models.DateTimeField()  # create time