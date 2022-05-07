import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","demo.settings")

import django
django.setup()

from faker import Faker

fake = Faker()

from random import randint

from app1.models import Employee


def populate(vlaue):
    for i in range(vlaue):
        eid = randint(1,122)
        ename = fake.name()
        esal = randint(12222,122222)
        obj = Employee.objects.get_or_create(eid=eid,ename=ename,esal=esal)


def main():
    value = int(input("enter a name: "))

    populate(value)


if __name__ == "__main__":
    main()
