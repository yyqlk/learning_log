# AUTHOR : YYQLk
"""定义learning_logs的urls"""
from django.urls import path, re_path
from . import views  # 表示从当前文件所在的文件夹里import

urlpatterns = [
    path('', views.index, name='index'),  # index
    re_path('^topic/$', views.topic, name='topic'),  # all topic
    re_path('^topic/(?P<topic_id>\\d+)/$', views.a_topic, name='a_topic'),  # one topic
    re_path('^new_topic/$', views.new_topic, name='new_topic'),
    re_path('^new_entry/(?P<topic_id>\\d+)/$', views.new_entry, name='new_entry'),
    re_path('^edit_entry/(?P<entry_id>\\d+)/$', views.edit_entry, name='edit_entry')

]