from django.shortcuts import render

def renderTemplate(request):
    myDict = {"id": 6604101365,"name": "Pakin Intalang"}
    return render(request, 'templatesApp/firstTemplate.html', context=myDict)

def renderEmployee(request):
    myDict = {"id": 6604101365, "name": "Pakin Intalang", "sal": 10000}
    return render(request, 'templatesApp/employeeTemplate.html', context=myDict)
