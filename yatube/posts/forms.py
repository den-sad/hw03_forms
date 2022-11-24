from django import forms
from .models import Post, Group


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        group = forms.ModelChoiceField(
            queryset=Group.objects.all(),
            to_field_name="group")
        fields = ("text", "group")
        help_texts = {'text': "Текст поста",
                      'group': 'Группа, к которой будет относиться пост'}
        labels = {'text': "Текст поста",
                  'group': 'Группа'}
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'cols': '40',
                                          'rows': '10',
                                          }
                                   )
        }
