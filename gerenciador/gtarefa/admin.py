# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from gtarefa.models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(ProjetoUsuario)
admin.site.register(Tarefa)
