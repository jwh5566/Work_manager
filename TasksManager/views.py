from django.shortcuts import render


def page(request):
    my_variable = "Hello World!"
    years_old = 15
    array_city_capitale = ["Paris", "London", "Washington"]
    return render(request, 'index.html',{
        "my_var": my_variable,
        "years": years_old,
        "array_city": array_city_capitale,
        "product": 1
    })

def connection_page(request):
    return render(request, 'connection.html')