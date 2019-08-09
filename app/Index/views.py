import json
from django.http import HttpResponse
import datetime
from django.core import serializers

from .models import User,Product,Like,Buy

from django.db.models import Max

# register
def register(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user_name = request.POST.get('user_name')
    address = request.POST.get('address')
    cellphone = request.POST.get('cellphone')
    paypal_number = request.POST.get('paypal_number')
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = User.objects.filter(email=email)
    if len(data):
        return HttpResponse(json.dumps({"code": 0, "err_msg": "email have already"}, ensure_ascii=False))
    else:
        user = User(email=email, password=password,user_name=user_name,address=address,cellphone=cellphone,paypal_number=paypal_number,
                    create_time = create_time, status= 'active')
        user.save()
        return HttpResponse(json.dumps({"code": 1, "data": "register success"}, ensure_ascii=False))

# change personal information

def up_user_info(request):
    id = request.POST.get('id')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user_name = request.POST.get('user_name')
    address = request.POST.get('address')
    cellphone = request.POST.get('cellphone')
    paypal_number = request.POST.get('paypal_number')
    User.objects.filter(id=id).update(email=email, password=password,user_name=user_name,address=address,cellphone=cellphone,paypal_number=paypal_number,
                    )
    return HttpResponse(json.dumps({"code": 1, "data": "success"}, ensure_ascii=False))

# dis-regist and show the reason
def del_user_info(request):
    uid = request.POST.get('uid')
    desc = request.POST.get('desc')
    User.objects.filter(id=uid).update(status='inactive',desc=desc)
    return HttpResponse(json.dumps({"code": 1, "data": "success"}, ensure_ascii=False))

# liked product 
def get_liked(request):
    user_id = request.POST.get('user_id')

    all_data = Like.objects.filter(user_id=user_id)

    arr = []
    for item in all_data:
        arr.append(serializers.serialize("json", Product.objects.filter(id=item.product_id)))
    return HttpResponse(json.dumps({"code": 1, "data": arr}, ensure_ascii=False))



# login

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    data = serializers.serialize("json", User.objects.filter(email=email,password=password,status='active'))
    if( len(json.loads(data)) ):
        return HttpResponse(json.dumps({"code": 1, "data": json.loads(data)[0]}, ensure_ascii=False))
    else:
        return HttpResponse(json.dumps({"code": 0, "err_msg": "email or password error"}, ensure_ascii=False))

# post product
def publish(request):
    user_id  =  request.POST.get('user_id')
    category =  request.POST.get('category')
    sub_category =  request.POST.get('sub_category')
    product_photo =  request.POST.get('product_photo')
    product_condition =  request.POST.get('product_condition')
    min_price =  request.POST.get('min_price')
    start_time =  request.POST.get('start_time')
    end_time =  request.POST.get('end_time')
    desc = request.POST.get('desc')
    delivery =  request.POST.get('delivery')
    freight =  request.POST.get('freight')
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    product = Product(category=category, sub_category=sub_category, product_photo=product_photo, product_condition=product_condition, min_price=min_price,
                      start_time=start_time,
                      end_time=end_time,
                      desc=desc,
                      delivery=delivery,
                      freight=freight,
                      user_id =user_id,
                create_time=create_time)
    product.save()
    return HttpResponse(json.dumps({"code": 1, "data": "register success"}, ensure_ascii=False))


def get_product_list(request):
    sub_category = request.GET.get('sub_category')
    value = request.GET.get('value')
    type = request.GET.get('type')

    if sub_category :


        if type:
            data = serializers.serialize("json",
                                         Product.objects.filter(product_condition=type, sub_category=sub_category,
                                                                desc__contains=value))
        else:
            data = serializers.serialize("json", Product.objects.filter(sub_category=sub_category,desc__contains=value))
        return HttpResponse(json.dumps({"code": 1, "data": data}, ensure_ascii=False))
    else:
        if type:
            data = serializers.serialize("json", Product.objects.filter(product_condition=type, desc__contains=value))
        else:
            data = serializers.serialize("json", Product.objects.filter(desc__contains=value))
        return HttpResponse(json.dumps({"code": 1, "data": data}, ensure_ascii=False))


def get_prise(request):
    product_id = request.GET.get('product_id')
    user_id = request.GET.get('user_id')
    data = serializers.serialize("json", Like.objects.filter(product_id=product_id,user_id=user_id))
    return HttpResponse(json.dumps({"code": 1, "data": data}, ensure_ascii=False))


def add_prise(request):
    product_id = request.POST.get('product_id')
    user_id = request.POST.get('user_id')
    like = request.POST.get('like')
    data = serializers.serialize("json", Like.objects.filter(product_id=product_id,user_id=user_id))
    if (len(json.loads(data))):
    #     更新
        Like.objects.filter(product_id=product_id,user_id=user_id).update(like=like)
    else:
        liker = Like(product_id=product_id, user_id=user_id, like=like)
        liker.save()
    return HttpResponse(json.dumps({"code": 1, "data": "success"}, ensure_ascii=False))


# auction
def add_buy(request):
    product_id = request.POST.get('product_id')
    user_id = request.POST.get('user_id')
    buy_price = request.POST.get('buy_price')
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = Buy.objects.filter(product_id=product_id, user_id=user_id)
    if len(data):
        return HttpResponse(json.dumps({"code": 0, "err_msg": "already buy over"}, ensure_ascii=False))
    else:
        buyr = Buy(product_id=product_id, user_id=user_id,buy_price=buy_price,if_success=0,create_time=create_time)
        buyr.save()
        return HttpResponse(json.dumps({"code": 1, "data": "success"}, ensure_ascii=False))



# get auction list
def get_auction_list(request):
    now = datetime.datetime.now()
    all_data = Product.objects.filter(end_time__lt=now)
    print(len(all_data))

    for item in all_data:
        buy_data = Buy.objects.filter(product_id=item.id).aggregate(Max('buy_price'))
        if buy_data["buy_price__max"]:
            uid = Buy.objects.get(product_id=item.id,buy_price=buy_data["buy_price__max"]).user_id
            Product.objects.filter(id=item.id).update(buy_user_id=uid)




    user_id = request.POST.get('user_id')
    data = Buy.objects.filter(user_id=user_id)


    arr = []
    for item in data:
        arr.append(serializers.serialize("json",  Product.objects.filter(id=item.product_id)  )   )


    return HttpResponse(json.dumps({"code": 1, "data": arr}, ensure_ascii=False))


def get_post_list(request):
    user_id = request.POST.get('user_id')
    all_data = Product.objects.filter(user_id=user_id)

    arr = []
    for value in all_data:
        print(value.desc)
    #    get post list 
        list =  Buy.objects.filter(product_id=value.id)
        list_arr = []
        for list_value in list:
            data = User.objects.get(id=list_value.user_id)
            list_arr.append({
                "user_id": data.user_name,
                "buy_price":list_value.buy_price
            })
        arr.append({
            "value":{
                "product_photo":value.product_photo,
                "desc":value.desc
            },
            "list": list_arr
        })
    return HttpResponse(json.dumps({"code": 1, "data": arr}, ensure_ascii=False))


# end buyer 
def update_end_success(request):
    pid = request.POST.get('pid')
    uid = request.POST.get('uid')
    Product.objects.filter(id=pid).update( end_success_user_id=uid)
    return HttpResponse(json.dumps({"code": 1, "data": "success"}, ensure_ascii=False))