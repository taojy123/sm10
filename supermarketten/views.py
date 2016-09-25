# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from models import *
import os
import uuid
from PIL import Image
from django.contrib.auth.models import User
from StringIO import StringIO
import smtplib
import traceback



def index(request):
    types = Type.objects.all().order_by("id")

    products = Product.objects.filter(sn__icontains="A")
    pd1 = products[:3]

    if 'SERVER_SOFTWARE' in os.environ:
        import sae.storage
        tw = 1300
        th = 500
        mode = "full"
        type = "jpeg"

        for i in range(3):
            if len(pd1) <= i:
                continue
            src = pd1[i].pic
            filename = src.split("/")[-1]
            s = sae.storage.Client()
            try:
                p = s.get('thumbnail', "%d_%d_%s_%s"%(tw, th, mode, filename))
                if p:
                    url = s.url('thumbnail', "%d_%d_%s_%s"%(tw, th, mode, filename))
                    pd1[i].pic = url
                else:
                    raise
            except:
                try:
                    data = s.get('product', filename).data
                    imb = Image.open(StringIO(data))
                    ow, oh = imb.size
                    if th * ow > oh * tw: #如转换后的高宽比更大，则锁定高度截去不必要的宽度
                        h = th
                        w = int(h*ow/oh)
                        imc = imb.resize((w, h))
                        a = int((w - tw)/2)
                        b = 0
                        c = int(w - a)
                        d = th
                    else:   #否则锁定宽度截去不必要的高度
                        w = tw
                        h = int(w*oh/ow)
                        imc = imb.resize((w, h))
                        a = 0
                        b = int((h - th)/2)
                        c = tw
                        d = int(h - b)
                    imc = imc.crop((a,b,c,d))
                    pic = StringIO()

                    try:
                        imc.save(pic, type)
                    except:
                        imc.save(pic, 'png')
                    pic.seek(0)
                    p = sae.storage.Object(pic.read())
                    url = s.put('thumbnail', "%d_%d_%s_%s"%(tw, th, mode, filename), p)
                    pd1[i].pic = url
                except:
                    pass

    else:
        for i in range(3):
            if len(pd1) <= i:
                continue
            pd1[i].pic = "/thumbnail?w=1300&h=500&src=" + pd1[i].pic

    return render_to_response('index.html', locals())


def admin(request):
    return HttpResponseRedirect("/admin_order")


def admin_login(request):
    rp = HttpResponseRedirect("/admin")
    password = request.REQUEST.get("password")
    if password == "admin123456":
        rp.set_cookie("admin", "login")
    return rp

def admin_type(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    rs = Type.objects.all()
    return render_to_response('admin_type.html', locals())


def add_type(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    name = request.REQUEST.get('name')
    info = request.REQUEST.get('info')
    ob = Type()
    ob.name = name
    ob.info = info
    ob.save()
    return HttpResponseRedirect("/admin_type")

def del_type(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    id = request.REQUEST.get('id')
    Type.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin_type")

def update_type(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    id = request.REQUEST.get('id')
    name = request.REQUEST.get('name')
    info = request.REQUEST.get('info')
    ob = Type.objects.get(id=id)
    ob.name = name
    ob.info = info
    ob.save()
    return HttpResponseRedirect("/admin_type")


def admin_product(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    rs = Product.objects.all()
    types = Type.objects.all().order_by("id")
    return render_to_response('admin_product.html', locals())

def add_product(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    sn = request.REQUEST.get('sn')
    type_id = request.REQUEST.get('type_id')
    name = request.REQUEST.get('name')
    info = request.REQUEST.get('info')
    details = request.REQUEST.get('details')
    price = request.REQUEST.get('price', 0)
    pic = request.FILES.get('pic')
    ob = Product()
    ob.sn = sn
    ob.type = Type.objects.get(id=type_id)
    ob.name = name
    ob.info = info
    ob.details = details
    ob.price = float(price)
    if pic:
        filename =  pic.name
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            pic = s.put('product', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'product', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            pic = "/static/product/" + filename
        ob.pic = pic
    ob.save()
    return HttpResponseRedirect("/admin_product")

def del_product(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    id = request.REQUEST.get('id')
    Product.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin_product")

def update_product(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    id = request.REQUEST.get('id')
    sn = request.REQUEST.get('sn')
    type_id = request.REQUEST.get('type_id')
    name = request.REQUEST.get('name')
    info = request.REQUEST.get('info')
    details = request.REQUEST.get('details')
    price = request.REQUEST.get('price', 0)
    pic = request.FILES.get('pic')
    ob = Product.objects.get(id=id)
    ob.sn = sn
    ob.type = Type.objects.get(id=type_id)
    ob.name = name
    ob.info = info
    ob.details = details
    ob.price = float(price)
    print os.getcwd()
    if pic:
        filename =  pic.name
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            pic = s.put('product', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'product', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            pic = "/static/product/" + filename
        ob.pic = pic
    ob.save()
    return HttpResponseRedirect("/admin_product")


def admin_order(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    rs = Order.objects.exclude(status=0).order_by("-time").all()
    return render_to_response('admin_order.html', locals())

def del_order(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    id = request.REQUEST.get('id')
    Order.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin_order")

def check_order(request):
    if not request.COOKIES.get("admin"):
        return render_to_response('admin_login.html')
    id = request.REQUEST.get('id')
    ob = Order.objects.get(id=id)
    ob.status += 1
    ob.urge = 0
    ob.save()
    return HttpResponseRedirect("/admin_order")





def type(request, id):
    types = Type.objects.all().order_by("id")
    type = Type.objects.get(id=id)
    pds = Product.objects.filter(type=type)
    return render_to_response('type.html', locals())


def product(request, id):
    types = Type.objects.all().order_by("id")
    product = Product.objects.get(id=id)
    comments = Comment.objects.filter(product=product)
    return render_to_response('product.html', locals())


def cart(request):
    types = Type.objects.all().order_by("id")
    cart = request.COOKIES.get("cart", "{}")
    cart = eval(cart)
    rs = []
    total = 0
    for product_id, quantity in cart.iteritems():
        r = Product.objects.filter(id=product_id)
        if r and quantity:
            rs.append((r[0], quantity))
            price = r[0].price * quantity
            total += price
    return render_to_response('cart.html', locals())



def addtocart(request, product_id, quantity):
    cart = request.COOKIES.get("cart", "{}")
    cart = eval(cart)
    quantity = int(cart.get(product_id, 0)) + int(quantity)
    cart[product_id] = quantity
    cart = str(cart)
    rp = HttpResponseRedirect("/cart")
    rp.set_cookie("cart", cart, 3600*24*7)
    return rp



def delcart(request, product_id):
    cart = request.COOKIES.get("cart", "{}")
    cart = eval(cart)
    cart[product_id] = 0
    del  cart[product_id]
    cart = str(cart)
    rp = HttpResponseRedirect("/cart")
    rp.set_cookie("cart", cart, 3600*24*7)
    return rp




def addtoorder(request, product_id, quantity):
    types = Type.objects.all().order_by("id")

    order = Order()
    order.sn = str(uuid.uuid4())
    order.save()

    pd = Product.objects.get(id=product_id)

    b = Bom()
    b.order =order
    b.product = pd
    b.quantity = int(quantity)
    b.save()

    return render_to_response('order.html', locals())



def carttoorder(request):
    types = Type.objects.all().order_by("id")
    cart = request.COOKIES.get("cart", "{}")
    cart = eval(cart)
    if cart:
        order = Order()
        order.sn = str(uuid.uuid4())
        order.save()
        for product_id, quantity in cart.iteritems():
            r = Product.objects.filter(id=product_id)
            if r and quantity:
                b = Bom()
                b.order = order
                b.product = r[0]
                b.quantity = quantity
                b.save()

    rp = render_to_response('order.html', locals())
    rp.set_cookie("cart", "{}", 3600*24*7)
    return rp


def submit_order(request):
    types = Type.objects.all().order_by("id")
    order_id = request.REQUEST.get("order_id")
    name = request.REQUEST.get("name")
    address = request.REQUEST.get("address")
    phone = request.REQUEST.get("phone")
    email = request.REQUEST.get("email")

    order = Order.objects.get(id=order_id)
    order.name = name
    order.address = address
    order.phone = phone
    order.email = email
    order.time = datetime.datetime.now()
    order.status = 1
    order.save()

    if email:
        try:
            smtp = smtplib.SMTP()
            smtp.connect("smtp.163.com", "25")
            smtp.login('watchmen123456', 'wm123456')
            content = u"亲爱的顾客 您好，你在 十分钟超市 购买的商品订单提交成功，我们会尽快安排送货，订单号为 %s ,可以在我们网站上查看到订单的最新状态，谢谢~" % order.sn
            msg = u"From: watchmen123456@163.com\r\nTo: %s\r\nSubject: 十分钟超市 订单提交成功 \r\n\r\n%s" % (email, content)
            msg = msg.encode("gbk")
            smtp.sendmail('watchmen123456@163.com', email, msg)
            smtp.quit()
        except:
            pass

    orders = request.COOKIES.get("orders", "[]")
    orders = eval(orders)
    orders.append(order.sn)
    orders = str(orders)

    rp = render_to_response('order_finish.html', locals())
    rp.set_cookie("name", name.encode("utf8"), 3600*24*30)
    rp.set_cookie("address", address.encode("utf8"), 3600*24*30)
    rp.set_cookie("phone", phone.encode("utf8"), 3600*24*30)
    rp.set_cookie("email", email.encode("utf8"), 3600*24*30)
    rp.set_cookie("orders", orders.encode("utf8"), 3600*24*30)
    return rp


def add_comment(request):
    product_id = request.REQUEST.get("product_id")
    name = request.REQUEST.get("name")
    content = request.REQUEST.get("content")
    product = Product.objects.get(id=product_id)
    if name:
        user = name
    else:
        user = u"游客"
    if content:
        c = Comment()
        c.product = product
        c.content = content
        c.user = user
        c.save()
    rp = HttpResponseRedirect("/product/" + product_id)
    if name:
        rp.set_cookie("name", name.encode("utf8"), 3600*24*30)
    return rp


def del_comment(request):
    comment_id = request.REQUEST.get("comment_id")
    Comment.objects.filter(id=comment_id).delete()
    return HttpResponseRedirect("/")


def order_search(request):
    types = Type.objects.all().order_by("id")

    sn = request.REQUEST.get("sn", "")
    urge = request.REQUEST.get("urge", "")
    if sn:
        order = Order.objects.filter(sn=sn)
        if order:
            order = order[0]


    orders = request.COOKIES.get("orders", "[]")
    orders = eval(orders)

    return render_to_response("order_search.html", locals())

def urge(request):
    sn = request.REQUEST.get("sn")
    order = Order.objects.get(sn=sn)
    order.urge = 1
    order.save()
    return HttpResponseRedirect("/order_search?urge=true")

def cancel(request):
    sn = request.REQUEST.get("sn")
    order = Order.objects.get(sn=sn)
    order.status = -1
    order.urge = 0
    order.save()
    return HttpResponseRedirect("/order_search?urge=true")


def thumbnail(request):
    src = request.REQUEST.get("src")
    w = request.REQUEST.get("w")
    h = request.REQUEST.get("h")
    mode = request.REQUEST.get("mode", "full")
    type = request.REQUEST.get("type", "jpeg")

    tw = int(w)
    th = int(h)

    if 'SERVER_SOFTWARE' in os.environ:
        import sae.storage
        filename = src.split("/")[-1]
        s = sae.storage.Client()
        try:
            rs = s.get('thumbnail', "%d_%d_%s_%s"%(tw, th, mode, filename)).data
            if rs:
                return HttpResponse(rs, mimetype="image")
            else:
                raise
        except:
            try:
                data = s.get('product', filename).data
                imb = Image.open(StringIO(data))
            except:
                pass
    else:
        src = src[src.find("static/"):]
        tmpname = src.replace("/","_") + "_%d_%d_%s" %(tw, th, mode)
        tmpfile = os.path.join(os.getcwd(), 'static', 'thumbnail', tmpname)
        if os.path.exists(tmpfile):
            #如果该尺寸的缩略图已存在，则直接返回该图片
            rs = open(tmpfile, "rb").read()
            return HttpResponse(rs, mimetype="image")

        dirs = src.split("/")
        imfile = os.path.join(os.getcwd(), *dirs)
        imb = Image.open(imfile)



    ow, oh = imb.size
    if mode == "full":  # 填充模式，图片占满整个区域 多余部分剪掉
        if th * ow > oh * tw: #如转换后的高宽比更大，则锁定高度截去不必要的宽度
            h = th
            w = int(h*ow/oh)
            imc = imb.resize((w, h))
            a = int((w - tw)/2)
            b = 0
            c = int(w - a)
            d = th
        else:   #否则锁定宽度截去不必要的高度
            w = tw
            h = int(w*oh/ow)
            imc = imb.resize((w, h))
            a = 0
            b = int((h - th)/2)
            c = tw
            d = int(h - b)
        imc = imc.crop((a,b,c,d))
    else:   # 适应模式，图片在区域中保持比例，多出部分用空白填满 (fit)
        if th * ow > oh * tw: #如转换后的高宽比更大，则锁定宽度，高度用空白填充
            imc = Image.new("RGBA", (tw,th), (255,255,255,0))
            w = tw
            h = int(w*oh/ow)
            imt = imb.resize((w, h))
            imc.paste(imt, (0,(th-h)/2))
        else:   #否则锁定高度，宽度用空白填充
            imc = Image.new("RGBA", (tw,th), (255,255,255,0))
            h = th
            w = int(h*ow/oh)
            imt = imb.resize((w, h))
            imc.paste(imt, ((tw-w)/2,0))

    try:
        w, h = imc.size
        for i in range(w):
            for j in range(h):
                if imc.getpixel((i,j))[3] == 0:
                    imc.putpixel((i,j), (255,255,255,0))
    except:
        pass

    if 'SERVER_SOFTWARE' in os.environ:
        import sae.storage
        pic = StringIO()
        try:
            imc.save(pic, type)
        except:
            imc.save(pic, 'png')
        pic.seek(0)

        s = sae.storage.Client()
        p = sae.storage.Object(pic.read())
        pic = s.put('thumbnail', "%d_%d_%s_%s"%(tw, th, mode, filename), p)
        rs = s.get('thumbnail', "%d_%d_%s_%s"%(tw, th, mode, filename)).data
    else:
        try:
            imc.save(tmpfile, type)
        except:
            imc.save(tmpfile, 'png')
        rs = open(tmpfile, "rb").read()
    return HttpResponse(rs, mimetype="image")



def remind(request):
    sns = []
    urges = []
    for order in Order.objects.exclude(status=0):
        sns.append(order.sn)
    for order in Order.objects.filter(urge=1):
        urges.append(order.sn)
    rs = str(sns) + "+++" + str(urges)
    return HttpResponse(rs)




#====================login=============================================
def login(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponseRedirect("/admin/")

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect("/admin/")
#======================================================================
