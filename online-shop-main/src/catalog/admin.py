from django.contrib import admin
from . import models
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(models.Category)

admin.site.register(models.Category, CategoryAdmin)