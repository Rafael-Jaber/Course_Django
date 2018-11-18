from django.contrib import admin
from .models import Cliente, Telefone, CPF, Departamento

# Register your models here

class EmpregadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'email')
    list_filter = ('departamentos', )
    search_fields = ('id', 'nome')


admin.site.register(Cliente, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)
