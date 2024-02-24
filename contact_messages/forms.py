from django import forms

from contact_messages.models import Contact


class SendMessageForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

    def save(self, commit=True):
        message = super().save(commit)
        message.save()

        return message
