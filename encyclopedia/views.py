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
        return render(request,"encyclopedia/errorpage.html")
    else:
        return render(request,"encyclopedia/content.html")