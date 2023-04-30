
from django.db import models


class Todos(models.Model):
    todo_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.todo_text


class Notes(models.Model):
    todos = models.ForeignKey(Todos, on_delete=models.CASCADE)
    notes_text = models.CharField(max_length=200)

    def __str__(self):
        return self.notes_text