from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import FakeData
import faker
fake = faker.Faker()

def fakedata_view(request):
    for i in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        job = fake.random_element(elements=("HR",'PM','Admin','Manager'))
        salary = fake.random_element(elements=(10000,13000,25000,40000,15000))
        city = fake.random_element(elements=('Hyd','Bang','Che','Pune','Mumbai'))
        state = fake.state()
        address = fake.address()

        data = FakeData(
            first_name=first_name,
            last_name=last_name,
            email=email,
            salary=salary,
            job=job,
            city=city,
            state=state,
            address=address
        )
        data.save()
    return HttpResponse("Data Saved")

def fetch_data(request):
    fdata = FakeData.objects.all()
    return render(request,'fakedata.html',{'fdata':fdata})







