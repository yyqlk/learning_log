# AUTHOR : YYQLK
from django import forms
from .models import Topic
from .models import Entry


class TopicForm(forms.ModelForm):
    class Meta:  # 内嵌的Meta类，告诉django根据那个model创建表单，表单里有那些文件
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # 不为text生成标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}



