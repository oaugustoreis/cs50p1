from django.shortcuts import render

from markdown2 import Markdown
from . import util

def convertMd(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = convertMd(title)
    if content == None:
        return render(request,"encyclopedia/errorpage.html",{
            "message":"That content doesn't exist"
        })
    else:
        return render(request,"encyclopedia/content.html",{
            "title":title,
            "content":content
        })
        
def search(request):
    if request.method == "POST":
        entry= request.POST['q']
        content = convertMd(entry)
        if content is not None:
            return render(request,"encyclopedia/content.html",{
            "title":entry,
            "content":content
        })
        else:
            entries=util.list_entries()
            recommended = []
            for i in entries:
                if entry.lower() in i.lower():
                    recommended.append(i)
            return render(request,"encyclopedia/search.html" ,{
                "recommended":recommended
            })

def new_page(request):
    if request.method == "GET":
        return render(request,"encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/errorpage.html", {
                "title": title,
                "message": "Page already exists!"
            })
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/content.html", {
                "title": title,
                "content":convertMd(title)
            })
        