# -*- coding: utf-8 -*

from django.db import models
from django.core.urlresolvers import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)  # 博客题目
    category = models.CharField(max_length=50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 博客文章正文

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'article_id': self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Article, self).save()
        if not self.category:
            self.category = 'uncategorized'
            self.save()

    class Meta:  # down sort by date time
        ordering = ['-date_time']
