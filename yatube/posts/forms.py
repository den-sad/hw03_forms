from django import forms
from .models import Post, Group


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        group = forms.ModelChoiceField(
            queryset=Group.objects.all(),
            to_field_name="group")
        fields = ("text", "group")
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'cols': '40',
                                          'rows': '10'}),
        }
