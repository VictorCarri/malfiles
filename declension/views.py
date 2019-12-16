from django.http import HttpResponse
from django.template import loader

from declension.maldecl.decline import decline


# The main index page
def index(req=None):
    template = loader.get_template("declension/index.html")
    ctx = {} # Unnecessary, but we should provide it
    return HttpResponse(template.render(ctx, req))

# Shows the full declension of a single noun
def showDeclension(req=None, noun=""):
    template = loader.get_template("declension/noun.html")
    ctx = {
        "noun": noun, # Pass the noun which was sent in
        "declensions": decline(noun) # Pass the noun's declined forms
    }
    return HttpResponse(template.render(ctx, req))

def hello(req=None):
    return HttpResponse("Hello, World!")