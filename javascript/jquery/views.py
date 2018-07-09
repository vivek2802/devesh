from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.http import JsonResponse

# from django.views import generic
# from django.views.generic import View
from .models import Person,Map
from django.views.generic.list import ListView

# Create your views here.
#class personListView(ListView):
  #  model = person

def formsubmit(request):

    person=Person()
    #context={"person": person}

    if request.method == 'POST':
        person.first_name = request.POST['fname']
        person.designation=request.POST['desg']
        person.save()
        print("asdfsdafd")
        return JsonResponse({'first_name': person.first_name , 'designation':person.designation, 'person_id' : person.id})


    else:
        person = Person()
    print('asdfsdadfasd')
    return render (request, 'jquery/form.html',{"person":person})


class person_list(ListView):
    model = Person

def delete(request,person_id):
    request.method ="POST"
    person=Person.objects.get(pk=person_id)
    person.delete()
    return JsonResponse("thanks",safe=False)


def update(request,id):
    person=get_object_or_404(Person,id=id)
    if request.method=='POST':

        person.first_name = request.POST['fname1']
        person.designation = request.POST['desg1']
        person.save()
        return JsonResponse(
            data={'first_name': person.first_name, 'designation': person.designation, 'person_id': id})



def address_submit(request):

    map =Map()

    if request.method == "POST":

        map.address=request.POST['address']
        map.country=request.POST['address2']
        map.postal_code=request.POST['address1']
        map.save()
        return JsonResponse(
            data={'address': map.address, 'country': map.country,'postal_code':map.postal_code,})
    else:
        map=Map.objects.all()
    return render(request, 'jquery/google map1.html', {"map": map})


def deletemap(request,map_id):
    request.method ="POST"
    map=Map.objects.get(pk=map_id)
    map.delete()
    return JsonResponse("thanks",safe=False)









