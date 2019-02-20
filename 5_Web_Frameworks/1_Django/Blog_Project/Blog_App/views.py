from django.shortcuts import render
from django.http import HttpResponse 

# dummy data representing users' posts from DB
posts = [
    {
        "author": "Albert Einstein",
        "title": "Blog Post #1",
        "content": "First post",
        "date_posted": "Feb. 5 2019"
    },
    {
        "author": "Pablo Escobar",
        "title": "Blog Post #1",
        "content": "First post",
        "date_posted": "Feb. 5 2019"
    } 
]

# render() function will take DB Data as its 3rd arg
# and then pass it to the template and 
# we will have access to context's keys in the template 
context = {
    "posts": posts
}


def home(request):
    # return HttpResponse("<h1>This is Blog Home</h1>")

    # It starts looking through templates folder to find templates. 
    # So, begin the path from inside "templates" directory. 
    return render(request, "Blog_App/home.html", context)

def about(request):
    # return HttpResponse("<h2>This is a about</h2>")

    return render(request, "Blog_App/about.html", {"title": "About"})

