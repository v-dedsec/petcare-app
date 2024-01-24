from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import datetime
from petcare.models import *




def login(request):
    return render(request,'login_index.html')


def loginpst(request):
    name = request.POST['username']
    password = request.POST['password']
    login = log.objects.filter(uname=name, password=password)
    if login.exists():
        logg = log.objects.get(uname=name, password=password)
        request.session['lid'] = logg.id
        request.session['log'] = 'log'
        if logg.utype == 'admin':
            return HttpResponse('''<script>alert('success');window.location='/petcare/adminhome/'</script>''')
        elif logg.utype == 'user':
            return HttpResponse('''<script>alert('success');window.location='/petcare/userhome/'</script>''')
        elif logg.utype == 'shop':
            return HttpResponse('''<script>alert('success');window.location='/petcare/shophome/'</script>''')
        elif logg.utype == 'doctor':
            return HttpResponse('''<script>alert('success');window.location='/petcare/dochome/'</script>''')
        elif logg.utype == 'deliveryboy':
            return HttpResponse('''<script>alert('success');window.location='/petcare/deliveryhome/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/petcare/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid');window.location='/petcare/login/'</script>''')

def admin_changepass(request):
    return render(request, 'changepassword.html')


def admin_changepass_post(request):
    current_paswword=request.POST['currentpass']
    new_paswword=request.POST['newpassword']
    confirm_paswword=request.POST['repassword']
    res=log.objects.filter(id=request.session['lid'],password=current_paswword)
    if res.exists():
        res = log.objects.get(id=request.session['lid'], password=current_paswword)
        if new_paswword==confirm_paswword:
            res = log.objects.filter(id=request.session['lid'], password=current_paswword).update(password=confirm_paswword)
            return HttpResponse('''<script>alert('Changing Successfully');window.location='/petcare/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('Password Mismatch');window.location='/petcare/admin_changepass/'</script>''')
    else:
        return HttpResponse('''<script>alert('Password Not Found');window.location='/petcare/admin_changepass/'</script>''')




def adminhome(request):
    return  render(request, 'admin_index.html')

def userhome(request):
    return render(request,'user_index.html')

def shophome(request):
    return render(request,'shop_index.html')

def dochome(request):
    return render(request,'doc_index.html')


def usersignup(request):
    return render(request,'usersignup.html')

def doctorsignup(request):
    return render(request,'doctorsignup.html')

def shopsignup(request):
    return render(request,'shopsignup.html')

#user
def userpost(request):
    uname=request.POST['username']
    gender=request.POST['gender']
    dob=request.POST['dob']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    pincode=request.POST['pincode']
    district=request.POST['district']
    state=request.POST['state']
    passw=request.POST['conformpassword']
    img=request.FILES['photo']

    date=datetime.datetime.now().strftime('%y%m%d-%H%M%S')+'.jpg'
    fs=FileSystemStorage()
    fs.save(date,img)
    path= fs.url(date)

    logg=log()
    logg.uname=email
    logg.password=passw
    logg.utype='user'
    logg.save()

    ubj = user()
    ubj.LOGIN=logg
    ubj.username=uname
    ubj.gender=gender
    ubj.dob=dob
    ubj.email=email
    ubj.phone=phone
    ubj.place=place
    ubj.pin=pincode
    ubj.district=district
    ubj.state=state
    ubj.photo=path
    ubj.save()
    return HttpResponse('''<script>alert('success');window.location='/petcare/login/'</script>''')

def userview(request):
    res=user.objects.all()
    return render(request,'userview.html',{"data":res})

def useruserview(request):
    res=user.objects.filter(LOGIN=request.session['lid'])
    return render(request,'useruserview.html',{"data":res})



def useredit(request,id):
    res=user.objects.get(LOGIN=id)
    return render(request,'useredit.html',{"data":res})


def usereit(request):
    id =request.POST['login']
    uname = request.POST['username']
    gender = request.POST['gender']
    dob = request.POST['dob']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    pincode = request.POST['pincode']
    district = request.POST['district']
    state = request.POST['state']


    if 'Image' in request.FILES:
        img = request.FILES['photo']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'

        fs = FileSystemStorage()
        fs.save(date, img)
        path = fs.url(date)
        res = user.objects.filter(LOGIN=id).update(username=uname,gender=gender,dob=dob,email=email,phone=phone,place=place,pin=pincode,district=district,state=state,photo=path)
        return HttpResponse("Updated")
    else:
        res = user.objects.filter(LOGIN=id).update(username=uname, gender=gender, dob=dob, email=email, phone=phone, place=place, pin=pincode, district=district, state=state)
        return HttpResponse("Updated")



#shop
def shoppost(request):
    uname=request.POST['shopname']
    lino=request.POST['lisenceno']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    pincode=request.POST['pincode']
    district=request.POST['district']
    state=request.POST['state']
    passw=request.POST['confirmpassword']
    img=request.FILES['photo']

    date=datetime.datetime.now().strftime('%y%m%d-%H%M%S')+'.jpg'
    fs=FileSystemStorage()
    fs.save(date,img)
    path= fs.url(date)

    logg=log()
    logg.uname=email
    logg.password=passw
    logg.utype='pending'
    logg.save()

    sbj = shop()
    sbj.LOGIN=logg
    sbj.shopname=uname
    sbj.licenceno=lino
    sbj.email=email
    sbj.phone=phone
    sbj.place=place
    sbj.pin=pincode
    sbj.district=district
    sbj.state=state
    sbj.photo=path
    sbj.status="pending"
    sbj.save()
    return HttpResponse('''<script>alert('success');window.location='/petcare/login/'</script>''')


def shopview(request):
    res=shop.objects.all()
    return render(request,'shopview.html',{"data":res})

def shopshopview(request):
    res=shop.objects.get(LOGIN=request.session['lid'])
    return render(request,'shopview.html',{"i":res})

def adshopview(request):
    res=shop.objects.filter(status='pending')
    return render(request,'adviewshop.html',{"data":res})

def admin_approve_shop(request,id):
    res=shop.objects.filter(LOGIN__id=id).update(status="approved")
    res1=log.objects.filter(id=id).update(utype="shop")
    return HttpResponse('''<script>alert('Approve Successfull');window.location='/petcare/adminshopapp/'</script>''')

def admin_reject_shop(request,id):
    res=shop.objects.filter(LOGIN__id=id).update(status="rejected")
    res1=log.objects.filter(id=id).update(utype="rejected")
    return HttpResponse('''<script>alert('Rejected');window.location='/petcare/adminshopreject/'</script>''')



def adshopapproved(request):
    res=shop.objects.filter(status='approved')
    return render(request,'adshopapprove.html',{"data":res})

def adshopreject(request):
    res=shop.objects.filter(status='rejected')
    return render(request,'asshopreject.html',{"data":res})

def shopedit(request,id):
    res=shop.objects.get(LOGIN=id)
    return render(request,'shopedit.html',{"data":res})


def shopeit(request):
    id =request.POST['login']
    uname = request.POST['shopname']
    lino = request.POST['lisenceno']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    pincode = request.POST['pincode']
    district = request.POST['district']
    state = request.POST['state']


    if 'Image' in request.FILES:
        img = request.FILES['photo']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'

        fs = FileSystemStorage()
        fs.save(date, img)
        path = fs.url(date)
        res = shop.objects.filter(LOGIN=id).update(shopname=uname,licenceno=lino,email=email,phone=phone,place=place,pin=pincode,district=district,state=state,photo=path)
        return HttpResponse("Updated")
    else:
        res = shop.objects.filter(LOGIN=id).update(shopname=uname,licenceno=lino , email=email, phone=phone, place=place, pin=pincode, district=district, state=state)
        return HttpResponse("Updated")



#doctor

def doctorpost(request):
    uname=request.POST['doctorname']
    gender=request.POST['gender']
    exp=request.POST['experience']
    quli=request.POST['qualication']
    clinic=request.POST['clinicname']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    pincode=request.POST['pincode']
    district=request.POST['district']
    state=request.POST['state']
    passw=request.POST['conformpassword']

    pdf = request.FILES['certificate']

    date = datetime.datetime.now().strftime('%y%m%d-%H%M%S') + '.pdf'
    fs = FileSystemStorage()
    fs.save(date, pdf)
    pd = fs.url(date)

    img=request.FILES['photo']

    date=datetime.datetime.now().strftime('%y%m%d-%H%M%S')+'.jpg'
    fs=FileSystemStorage()
    fs.save(date,img)
    path= fs.url(date)

    logg=log()
    logg.uname=email
    logg.password=passw
    logg.utype='pending'
    logg.save()

    dbj = doctor()
    dbj.LOGIN=logg
    dbj.doctorname=uname
    dbj.gender=gender
    dbj.experience=exp
    dbj.qualification=quli
    dbj.clinicname=clinic
    dbj.certificate=pd
    dbj.email=email
    dbj.phone=phone
    dbj.place=place
    dbj.pin=pincode
    dbj.district=district
    dbj.state=state
    dbj.photo=path
    dbj.status='pending'
    dbj.save()
    return HttpResponse('''<script>alert('success');window.location='/petcare/login/'</script>''')


def doctorview(request):
    res=doctor.objects.all()
    return render(request,'docview.html',{"data":res})

def docdocview(request):
    res=doctor.objects.filter(LOGIN=request.session['lid'])
    return render(request,'docview.html',{"data":res})

def userdocview(request):
    res=doctor.objects.all()
    return render(request,'userviewdoc.html',{"data":res})


def adviewdoc(request):
    res=doctor.objects.filter(status='pending')
    return render(request,'adviewdoc.html',{"data":res})

def admin_approve_doc(request,id):
    res=doctor.objects.filter(LOGIN__id=id).update(status="approved")
    res1=log.objects.filter(id=id).update(utype="doctor")
    return HttpResponse('''<script>alert('Approve Successfull');window.location='/petcare/adminappdoc/'</script>''')

def admin_reject_doc(request,id):
    res=doctor.objects.filter(LOGIN__id=id).update(status="rejected")
    res1=log.objects.filter(id=id).update(utype="rejected")
    return HttpResponse('''<script>alert('Rejected');window.location='/petcare/adminrejdoc/'</script>''')

def addocapproved(request):
    res=doctor.objects.filter(status='approved')
    return render(request,'adminapprovedoctor.html',{"data":res})

def addocreject(request):
    res=doctor.objects.filter(status='rejected')
    return render(request,'adminrejectdoctor.html',{"data":res})



def docedit(request,id):
    res=doctor.objects.get(LOGIN=id)
    return render(request,'docedit.html',{"data":res})

def doctoredit(request):
    id=request.POST['login']
    uname = request.POST['doctorname']
    gender = request.POST['gender']
    exp = request.POST['experience']
    quli = request.POST['qualication']
    clinic = request.POST['clinicname']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    pincode = request.POST['pincode']
    district = request.POST['district']
    state = request.POST['state']
    if 'photo'  in request.FILES:
        img = request.FILES['photo']
        date1 = datetime.datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
        fs1 = FileSystemStorage()
        fs1.save(date1, img)
        path1 = fs1.url(date1)
        res = doctor.objects.filter(LOGIN=id).update(photo=path1)
    if 'certificate' in request.FILES:
        pdf = request.FILES['certificate']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S') + '.pdf'

        fs = FileSystemStorage()
        fs.save(date, pdf)
        pd = fs.url(date)
        res = doctor.objects.filter(LOGIN=id).update(certificate=pd)
    else:
        res = doctor.objects.filter(LOGIN=id).update(doctorname=uname, gender=gender, experience=exp, phone=phone,
                                                     place=place, pin=pincode, district=district, state=state,
                                                     qualification=quli, clinicname=clinic,email=email)
    return HttpResponse('bye')



 #category

def catgory(request):
    return render(request,'category.html')


def catepost(request):
    cate=request.POST['category']

    cbj=category()
    cbj.categoryname=cate
    cbj.save()
    return HttpResponse('sucess')

def cateview(request):
    res=category.objects.all()
    return render(request,'cateview.html',{"data":res})

def cateedit(request,id):
    res = category.objects.get(pk=id)
    return render(request, 'cateedit.html', {"data": res})

def catedp(request):
    id = request.POST['id']
    cate = request.POST['category']
    res = category.objects.filter(pk=id).update(categoryname=cate)
    return HttpResponse("Updated")

#product
def product(request):

    res1=category.objects.all()
    return render(request,'product.html',{'data1':res1})




def productpost(request):
    cate=request.POST['cate']
    prod=request.POST['prod']
    dis=request.POST['dis']
    price=request.POST['price']
    ss=shop.objects.get(LOGIN=request.session['lid'])

    img = request.FILES['photo']
    date = datetime.datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
    fs = FileSystemStorage()
    fs.save(date, img)
    path = fs.url(date)

    pobj=products()

    pobj.productname=prod
    pobj.SHOP=ss


    pobj.discription=dis
    pobj.price=price
    pobj.photo=path
   
    res=category.objects.get(id=cate)
    pobj.CATEGORY=res
    pobj.save()

    return HttpResponse('sucess')

def productedit(request):
    id = request.POST['id']
    cate = request.POST['cate']
    prod = request.POST['prod']
    dis = request.POST['dis']
    price = request.POST['price']

    if 'Image' in request.FILES:
        img = request.FILES['photo']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'

        fs = FileSystemStorage()
        fs.save(date, img)
        path = fs.url(date)
        res = products.objects.filter(pk=id).update(CATEGORY=cate,productname=prod,discription=dis,price=price,photo=path)
        return HttpResponse("Updated")
    else:
        res = products.objects.filter(pk=id).update(CATEGORY=cate, productname=prod, discription=dis, price=price)
        return HttpResponse("Updated")





def productview(request):
    res = products.objects.all()
    return render(request, 'productview.html', {"data": res})

def user_productview(request):
    res=products.objects.all()
    return render(request,'userviewproduct.html',{"data":res})

def producted(request,id):
    res = products.objects.get(pk=id)
    res1 = category.objects.all()
    return render(request, 'productedit.html', {"data": res, "data1": res1})

#cart

def product_cart(request,id):
    res = products.objects.get(pk=id)
    return render(request,'cart.html',{'data':res})

def cartpost(request):
    id=request.POST['id']
    quan=request.POST['quantity']
    user_id=user.objects.get(LOGIN=request.session['lid'])
    date=datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')

    cbj=cart()
    cbj.quantity=quan
    cbj.USER=user_id
    cbj.date=date
    cbj.PRODUCT=products.objects.get(id=id)
    cbj.save()
    return HttpResponse("sucess")



def viewcart(request):
    res=cart.objects.filter(USER__LOGIN_id=request.session['lid'])
    l=[]
    total=0
    for i in res:
        total+=i.PRODUCT.price*i.quantity
        l.append({"pid":i.PRODUCT.id, 'Productname': i.PRODUCT.productname,'description': i.PRODUCT.discription,'price': i.PRODUCT.price,'quatity':i.quantity,'productimage': i.PRODUCT.photo})
    return render(request,'viewcart.html',{"data":l,"total":total})


def user_delete_cart(request,id):
    res = cart.objects.filter(pk=id).delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/petcare/viewcart/'</script>''')


def pay(request,total):
    return render(request, 'payment.html',{'total':total})


def paypost(request):
    lid=request.session['lid']
    accno=request.POST['accno']
    accname=request.POST['accnme']
    ifsc=request.POST['ifsc']
    cvv=request.POST['cvv']
    t=float(request.POST['total'])

    if payment.objects.filter(accountno=accno, accountname=accname, ifsc=ifsc, cvv=cvv, balance__gte=t).exists():

        res = cart.objects.filter(USER__LOGIN_id=lid).values_list('PRODUCT__SHOP_id').distinct()

        for i in res:
            print(i)
            res2 = cart.objects.filter(USER__LOGIN_id=lid, PRODUCT__SHOP_id=i[0])
            boj = orders()
            boj.USER = user.objects.get(LOGIN_id=lid)
            # t=i.amount*i.qty
            boj.amount = 0
            import datetime
            boj.date = datetime.datetime.now().date().today()
            boj.SHOP_id = i[0]
            boj.save()

            # res3 =
            mytotal = 0
            for j in res2:
                # print(j)
                bs = ordersub()
                bs.ORDER_id = boj.id
                bs.PRODUCT_id = j.PRODUCT.id
                bs.quantity = j.quantity
                bs.save()

                mytotal += (float(j.PRODUCT.price) * j.quantity)
                print(mytotal)
            cart.objects.filter(PRODUCT__SHOP_id=i[0], USER__LOGIN_id=lid).delete()
            boj = orders.objects.get(id=boj.id)
            boj.amount = mytotal
            boj.save()
        return HttpResponse('sucess')
    else:
        return HttpResponse('error')















#delevery

def delivery(request):
    return render(request,'delivery.html')

def deliveryhome(request):
    return  render(request,'delivery_index.html')


def deliverypost(request):
    uname = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    shop_id=shop.objects.get(LOGIN=request.session['lid'])

    img = request.FILES['photo']

    date = datetime.datetime.now().strftime('%y%m%d-%H%M%S') + '.jpg'
    fs = FileSystemStorage()
    fs.save(date, img)
    path = fs.url(date)

    logg = log()
    logg.uname = email
    logg.password = phone
    logg.utype = 'deliveryboy'
    logg.save()




    dobj=deliveryboy()

    dobj.name=uname
    dobj.LOGIN=logg
    dobj.email=email
    dobj.phone=phone
    dobj.SHOP=shop_id
    dobj.photo=path
    dobj.save()
    return HttpResponse('sucess')

def viewdelivery(request):
    res = deliveryboy.objects.all()
    return render(request, 'viewdeliveryboy.html', {"data": res})

def boyboyview(request):
    res=deliveryboy.objects.filter(LOGIN=request.session['lid'])
    return render(request,'viewdeliveryboy.html',{"data":res})




#complaint
def complain(request):
    return render(request,'complaint.html')

def complaintpost(request):
    date=request.POST['date']
    comp=request.POST['complaint']
    u_id=user.objects.get(LOGIN=request.session['lid'])


    cobj=complaint()
    cobj.date=date
    cobj.complaint=comp
    cobj.reply='pending'
    cobj.status='pending'
    cobj.USER=u_id
    cobj.save()
    return HttpResponse('''<script>alert('success');window.location='/petcare/complaint/'</script>''')


def adminview_comp(request):
    res = complaint.objects.all()
    return render(request, 'complaintview.html', {"data": res})

def userview_comp(request):
    res = complaint.objects.all()
    return render(request,'userviewcomp.html',{"data":res})

def admin_reply(request,id):
    res = complaint.objects.get(pk=id)
    return render(request,'reply.html' ,{"data": res})

def reply_post(request):
    id = request.POST['id']
    reply = request.POST['reply']
    res = complaint.objects.filter(pk=id).update(reply=reply,status='ok')
    return HttpResponse('updated')




#feedback

def feed(request):
    return render(request,'feedback.html')


def feedpost(request):
    date = request.POST['date']
    feedb = request.POST['feedback']
    u_id=user.objects.get(LOGIN=request.session['lid'])

    fobj=feedback()
    fobj.date=date
    fobj.feedback=feedb
    fobj.USER=u_id
    fobj.save()
    return HttpResponse('updated')

def adminview_feedback(request):
    res = feedback.objects.all()
    return render(request, 'viewfeedback.html', {"data": res})


#shedule

def shed(request):
    return render(request,'schedule.html')

def shedpost(request):
    date=request.POST['date']
    fromtime=request.POST['fromtime']
    totime=request.POST['totime']
    doc_id=doctor.objects.get(LOGIN=request.session['lid'])

    sobj=schedule()
    sobj.date=date
    sobj.fromtime=fromtime
    sobj.totime=totime
    sobj.DOCTOR=doc_id
    sobj.save()
    return HttpResponse("sucess")

def viewsheduledoc(request):
    res = schedule.objects.filter(DOCTOR__LOGIN_id=request.session['lid'])
    return render(request, 'viewsheduledoc.html', {"data": res})


def viewsheduleuser(request,id):
    res = schedule.objects.filter(DOCTOR=id)
    return render(request, 'viewshedule.html', {"data": res})



def stoc(request):
    res = products.objects.all()
    return render(request, 'stock.html', {'data': res})

def stocpost(request):
    pro=request.POST['product']
    sto=request.POST['stock']

    sbj=stock()
    sbj.stock=sto
    res=products.objects.get(id=pro)
    sbj.PRODUCT=res
    sbj.save()
    return HttpResponse('''<script>alert('success');window.location='/petcare/stock/'</script>''')


def stockview(request):
    res=stock.objects.all()
    return render(request,'stockview.html', {"data":res})


def stedit(request,id):
    res=stock.objects.get(pk=id)
    res1=products.objects.all()
    return render(request,'stockedit.html',{"data":res,"data1":res1})

def stockedit(request):
    id=request.POST['id']
    pro = request.POST['product']
    sto = request.POST['stock']

    res=stock.objects.filter(pk=id).update(PRODUCT=pro,stock=sto)
    return HttpResponse('''<script>alert('success');window.location='/petcare/stockview/'</script>''')


#allocate

def allocate(request,id):
    res = deliveryboy.objects.all()
    return render(request, 'allocate.html', {'data': res,'id':id})

def allocatepost(request):
    boy = request.POST['boy']
    id=request.POST['id']

    aabj=allocateorder()
    aabj.DELIVERYBOY_id=boy
    aabj.ORDER_id=id
    aabj.save()
    return HttpResponse('''<script>alert('success');window.location='/petcare/shopvieworder/'</script>''')

def viewallocate(request):
    res=allocateorder.objects.filter(DELIVERYBOY__LOGIN_id=request.session['lid'])
    return render(request, 'vieworderboy.html', {"data": res})



# def delivery_ordered(request,id):
#     res=orders.objects.get(id=id).update(status="deliverd")
#     return HttpResponse('''<script>alert('Approve Successfull');window.location='/petcare/deliveryhome/'</script>''')

def delivery_ordered(request, id):
    try:
        order = orders.objects.get(id=id)
        order.status = "delivered"
        order.save()
        res = "Order status updated successfully."
    except orders.DoesNotExist:
        res = "Order not found."

    return HttpResponse('<script>alert("Delivery Successfull"); window.location="/petcare/deliveryhome/";</script>')






#shopview
def shop_view_order(request):
    res=orders.objects.filter(SHOP__LOGIN_id=request.session['lid'])
    return render(request,'shopvieworder.html', {'data': res})

def more(request,id):
    res = ordersub.objects.filter(ORDER=id)
    return render(request,'more.html',{"data":res})
def usermore(request,id):
    res = ordersub.objects.filter(ORDER=id)
    return render(request,'usermore.html',{"data":res})

def user_view_order(request):
    res=orders.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'uservieworder.html', {'data': res})


#--------Appoiment
def appoiment(request,id):
    user_id = user.objects.get(LOGIN=request.session['lid'])
    sid=id

    apbj=appointment()
    apbj.USER=user_id
    apbj.status='pending'
    apbj.SCHEDULE_id=sid
    apbj.save()
    return HttpResponse('''<script>alert('success');window.location='/petcare/userdocview/'</script>''')

def viewapp(request):
    res=appointment.objects.filter(SCHEDULE__DOCTOR__LOGIN_id=request.session['lid'])
    return render(request,'app.html', {'data': res})

#------prescription
def pres(request,id):
    return render(request,'prescription.html',{"id":id})

def Prescripton(request):
    pres=request.POST['pres']
    id=request.POST['id']


    pbj=prescripton()
    pbj.prescripton=pres
    pbj.date=datetime.datetime.now().date().today()
    pbj.APPOINTMENT_id=id
    pbj.save()
    return HttpResponse('''<script>alert('success');window.location='/petcare/viewapp/'</script>''')

def viewpres(request,id):
    res=prescripton.objects.filter(APPOINTMENT=id)
    return render(request,'viewpre.html', {'data': res})

def viewpresuser(request,id):
    res=prescripton.objects.filter(APPOINTMENT__SCHEDULE__DOCTOR=id)
    return render(request,'viewpre.html', {'data': res})

def logout(request):
    request.session['log']=''
    return HttpResponse('''<script>alert('success');window.location='/petcare/login/'</script>''')








































