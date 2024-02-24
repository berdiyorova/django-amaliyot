from django.shortcuts import render, redirect
from django.views import View

from .forms import SendMessageForm
from .models import Contact


class ContactView(View):

    def get(self, request):
        create_form = SendMessageForm()
        context = {
            'form': create_form
        }
        return render(request, 'contact.html', context)

    def post(self, request):
        create_form = SendMessageForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('messages')

        return render(request, 'contact.html', {'form': create_form})



class ContactListView(View):

    def get(self, request):
        messages = Contact.objects.all().order_by('-sent_time')
        count = 0

        return render(request, 'message_list.html', {'messages': messages, 'count': count})
