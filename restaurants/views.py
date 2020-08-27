from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
    "my_list" : [
    {"restaurant_name": "Five Guys","food_type": "American Cuisine"},
    {"restaurant_name": "Forchetta","food_type": "Italian Cuisine"},
    {"restaurant_name": "Tokyo","food_type": "Japanese Cuisine"}

]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object": {
    "restaurant_name": "Five Guys",
    "food_type": "American Cuisine"
    }

    }
    return render(request, 'detail.html', context)
