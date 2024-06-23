from tortoise.models import Model
from tortoise import fields
from data_classes import Meme


class MemeModel(Model):
    id = fields.IntField(primary_key=True)
    text = fields.TextField()
    picture = fields.CharField(max_length=1024)

    def __str__(self):
        return self.text

    def to_meme(self):
        return Meme(id=self.pk, text=self.text, picture=self.picture)
