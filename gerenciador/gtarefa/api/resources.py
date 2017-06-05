# -*- coding: utf-8 -*-
from tastypie.resources import ModelResource
from tastypie import fields, utils
from gtarefa.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class UsuarioResource(ModelResource):
	def obj_delete_list(self, bundle, **kwargs):
		raise Unauthorized("Nao e possivel deletar todos os itens")
	class Meta:
		queryset = Usuario.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "nome": ('exact', 'startswith')
        }

class UserResource(ModelResource):
	
	class Meta:
		queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']
        

class ProjetoResource(ModelResource):
	def obj_delete_list(self, budle, **kwargs):
		raise Unauthorized("Nao e possivel deletar todos os itens")
	
	class Meta:
		queryset = Projeto.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()

class ProjetoUsuarioResource(ModelResource):
	def obj_delete_list(self, bundle, **kwargs):
		raise Unauthorized("Nao e possivel deletar todos os itens")
	usuario = fields.ToOneField(UsuarioResource, 'usuario')
	projeto = fields.ToOneField(ProjetoResource, 'projeto')
	class Meta:
		queryset = ProjetoUsuario.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        

class TarefaResource(ModelResource):
    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Nao e possivel deletar todos os itens")

    def obj_create(self, bundle, **kwargs):
        u = bundle.data['usuario'].split('/')
        p = bundle.data['projeto'].split('/')
        print (bundle.data)

        if not(Tarefa.objects.filter(nome=bundle.data['nome'])):
            ta = Tarefa()
            ta.nome = bundle.data['nome']
            ta.dataHora = bundle.data['dataHora']
            ta.usuario = Usuario.objects.get(pk = u[4])
            ta.projeto = Projeto.objects.get(pk = p[4])

            ta.save()
            bundle.obj = ta
            return bundle
        else:
            raise Unauthorized("Nao e possivel deletar todos os itens")

    usuario = fields.ToOneField(UsuarioResource, 'usuario')
    projeto = fields.ToOneField(ProjetoResource, 'projeto')
    class Meta:
        queryset = Tarefa.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }
