from django.db import models

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
        #abstract 는 데이터베이스에 추가가 안됨 그래서 이렇게 타임스탬프를 쓸수 있음

class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length = 140)
    caption = models.TextField()

class Comment(TimeStampedModel):

    message = models.TextField()
