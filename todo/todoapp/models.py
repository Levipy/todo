from django.db import models
from django.utils.timezone import now
# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=64,default='',null=True,verbose_name='标题')
    content = models.CharField(default='',max_length=1024,null=True,verbose_name='内容')
    create_time =models.DateTimeField(default=now,verbose_name='创建时间')
    todo_status = models.BooleanField(default=True,verbose_name='处理状态')

    def __str__(self):
        return '标题{},处理状态{}'.format(self.title,self.todo_status)