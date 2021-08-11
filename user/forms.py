from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta :
        model = Profile
        fields = ['image','nickname','description']

    def __str__(self): #어디선가 객체가 호출될떄의 이름표설정하는 것과 같음.
        return self.nickname

    def summary(self):
        return self.body[:100]