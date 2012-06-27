from listbook.models import Book
from django.contrib import admin
import string

def duplicate(modeladmin, request, queryset):
   for object in queryset:
           object.id = None
           object.save()
duplicate.short_description = "Duplicate selected record"

def duplicateSeries(modeladmin, request, queryset):
   for object in queryset:
      for obj in object.seri.split("$"):
           object.id = None
           object.seri = obj
           object.save()
   queryset.delete()
duplicateSeries.short_description = "Duplicate selected record split by ' ' series"

def duplicateSeriesS(modeladmin, request, queryset):
   for object in queryset:
      for obj in object.seri.split("$"):
           object.id = None
           object.seri = obj
           object.save()
   queryset.delete()
duplicateSeriesS.short_description = "Duplicate selected record split by $ series"

def duplicateSeries2(modeladmin, request, queryset):
   for object in queryset:
      number = object.seri.split("-")
      for obj in range(int(number[0]), int(number[1])+1):
           object.id = None
           object.seri = obj
           object.save()
   queryset.delete()
duplicateSeries2.short_description = "Duplicate selected record split by - series"

class BookAdmin(admin.ModelAdmin):
      list_display = ('judul', 'seri', 'tipe', 'harga_display')
      search_fields = ['judul', 'tipe', 'seri']
      actions = [duplicate, duplicateSeries, duplicateSeriesS, duplicateSeries2]
      ordering = ('judul',)
      def get_form(self,request,obj=None, **kwargs): 
        self.exclude = [] 
        self.readonly_fields = []
        if not request.user.is_superuser: 
           self.exclude.append('harga_modal') 
           self.readonly_fields.append('harga_display')
        return super(BookAdmin,self).get_form(request, obj=None, **kwargs)

admin.site.register(Book, BookAdmin)
