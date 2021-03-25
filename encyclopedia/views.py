from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request,name):
    entryList=[x.lower() for x in util.list_entries()]
    if name.lower() in entryList:
        return render(request,"encyclopedia/wikiPages.html",\
            {"content":util.get_entry(name),"title":name})
    else:
        #return render(request,"encyclopedia/wikiPages.html",{"content":f"Page {name} not Found!","title":"Error"})
        return render(request,"encyclopedia/error.html",{"title":name})

