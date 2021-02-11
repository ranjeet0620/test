from django.shortcuts import render
from fbv.models import Employee,Address

# Create your views here.
def add_or_update(req):
    msg=''
    if req.method=='POST':
        data=req.POST
        print(data)
        eid=data.get('id')
        dbemp=Employee.objects.filter(id=eid).first()
        print(dbemp)
        emp=Employee(name=data.get('name'),age=data.get('age'),email=data.get('email'))
        if dbemp:
            dbemp.name= emp.name
            dbemp.age = emp.age
            dbemp.email = emp.email
            dbemp.save()
            print('in if dbemp')
            msg='Employee Record Updated'
        else:
            emp.save()
            msg='Employee added succssfully'
    return render(req,'welcome.html',context={'msg':msg,'emplist':Employee.objects.all()})


def edit(req,eid):
    return render(req, 'welcome.html',
                  context={ 'emplist': Employee.objects.all(),
                            'emp':Employee.objects.filter(id=eid).first(),
                            'msg':''
                            })

def delete(req,eid):
    emprec=Employee.objects.filter(id=eid).first()

    if emprec:
        emprec.delete()
        msg='Employee Deleted Successfully'
        emplist = Employee.objects.all()

    else:
        msg='Employee With Given Id not Present'
        emplist = Employee.objects.all()


    return render(req, 'welcome.html', context={'msg': msg, 'emplist': emplist})

'''--------------------------------------------------------------------------'''

def add_or_update_address(req):
    msg=''

    if req.method=='POST':
        data=req.POST
        aid=data.get('aid')
        dbadd=Address.objects.filter(id=aid).first()
        adr=Address(city=data.get('city'),pin=data.get('pin'))
        if dbadd:
            dbadd.city= adr.city
            dbadd.pin = adr.pin
            dbadd.empref = adr.empref

            dbadd.save()

            msg='Address Record Updated'
        else:
            adr.save()
            msg='Address added succssfully'
    return render(req,'address.html',context={'msg':msg,'adrlist':Address.objects.all(),'emplist':Employee.objects.all()})


def edit_address(req,aid):
    return render(req, 'address.html',
                  context={ 'adrlist': Address.objects.all(),
                            'adr':Address.objects.filter(id=aid).first(),
                            'msg':''
                            })

def delete_adr(req,aid):
    adrrec=Address.objects.filter(id=aid).first()

    if adrrec:
        adrrec.delete()
        msg='Employee Deleted Successfully'
        adrlist = Address.objects.all()

    else:
        msg='Address With Given Id not Present'
        adrlist = Address.objects.all()


    return render(req, 'address.html', context={'msg': msg, 'adrlist': adrlist})




