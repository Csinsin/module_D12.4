from django.forms import ModelForm, BooleanField
from .models import Post
  
# Создаём модельную форму
class PostForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')
    class Meta:
        model = Post
        fields = ['title', 'text','postCategory', 'author']