import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudfbvproject.settings')
import django
django.setup()

from crudfbvapp.models import EmployeeModel
from faker import Faker
from random import *
fake = Faker()

def populate(n):
    for i in range(n):
        eno = randint(1111,9999)
        ename = fake.name()
        esal = randint(20000,50000)
        eaddr = fake.city()
        emp_records = EmployeeModel.objects.get_or_create(eno=eno,ename=ename,esal=esal,eaddr=eaddr)
populate(25)
