from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(req):

    if req.method == 'GET':

        form = ContactForm()

        return render(req, 'contact/index.html', {'form': form})

    elif req.method == 'POST':

        form = ContactForm(req.POST)

        msg = {}

        if form.is_valid():

            msg['status'] = 'success'
            msg['msg'] = 'Mensagem enviada!'

            form.save()

            return render(req, 'contact/index.html', {'msg': msg})

        else:
            return render(req, 'contact/index.html', {'form': form})

