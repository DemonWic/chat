from django import forms

from public_chat.models import PublicRoomChatMessage

class PublicChat(forms.ModelForm):
  name = forms.CharField()

