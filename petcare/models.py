from django.db import models

# Create your models here.
class log(models.Model):
    uname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    utype=models.CharField(max_length=100)
    
    
class user(models.Model):
    username=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)
    email=models.EmailField(max_length=100) 
    phone=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(log,on_delete=models.CASCADE)
    

class doctor(models.Model):
    doctorname=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    certificate=models.FileField(max_length=100)
    clinicname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100) 
    phone=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    status=models.CharField(max_length=100,default='')
    LOGIN=models.ForeignKey(log,on_delete=models.CASCADE) 
    
    
class shop(models.Model):
    shopname=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    licenceno=models.CharField(max_length=100)
    email=models.EmailField(max_length=100) 
    phone=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(log,on_delete=models.CASCADE)


class complaint(models.Model):
    date=models.DateField(max_length=100)
    status=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    complaint=models.CharField(max_length=100)
    USER=models.ForeignKey(user,on_delete=models.CASCADE)

class feedback(models.Model):
    date=models.DateField(max_length=100)
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)


class category(models.Model):
    categoryname=models.CharField(max_length=100)


class deliveryboy(models.Model):
    name=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    SHOP=models.ForeignKey(shop,on_delete=models.CASCADE)
    LOGIN=models.ForeignKey(log,on_delete=models.CASCADE, default='')



class products(models.Model):
    CATEGORY=models.ForeignKey(category,on_delete=models.CASCADE)
    SHOP=models.ForeignKey(shop,on_delete=models.CASCADE)
    productname=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    discription=models.CharField(max_length=100)
    price=models.IntegerField(max_length=100)

class orders(models.Model):
    date=models.CharField(max_length=100)
    SHOP=models.ForeignKey(shop,on_delete=models.CASCADE)
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)
    status=models.CharField(max_length=100,default='')

class ordersub(models.Model):
    ORDER=models.ForeignKey(orders,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=100)


class allocateorder(models.Model):
    ORDER=models.ForeignKey(orders,on_delete=models.CASCADE)
    DELIVERYBOY=models.ForeignKey(deliveryboy,on_delete=models.CASCADE)



class schedule(models.Model):
    DOCTOR=models.ForeignKey(doctor,on_delete=models.CASCADE)
    date=models.DateField(max_length=100)
    fromtime=models.CharField(max_length=100)
    totime=models.CharField(max_length=100)


class appointment(models.Model):
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    SCHEDULE=models.ForeignKey(schedule,on_delete=models.CASCADE)

class prescripton(models.Model):
    date=models.DateField(max_length=100)
    APPOINTMENT=models.ForeignKey(appointment,on_delete=models.CASCADE)
    prescripton=models.CharField(max_length=100)


class payment(models.Model):
    accountno=models.CharField(max_length=100)
    accountname=models.CharField(max_length=100, default='')
    ifsc=models.CharField(max_length=100, default='')
    cvv=models.CharField(max_length=100, default='')
    balance=models.CharField(max_length=100, default='')


class stock(models.Model):
    PRODUCT=models.ForeignKey(products,on_delete=models.CASCADE)
    stock=models.CharField(max_length=100)

class cart(models.Model):
    PRODUCT=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=100)
    date=models.CharField(max_length=100)
    USER=models.ForeignKey(user,on_delete=models.CASCADE)















































    
    
    
       