#--coding=utf-8
from haystack import indexes
from .models import Post

# 对指定的某个类的某些数据建立索引
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
 # broken field, should be char field
    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()