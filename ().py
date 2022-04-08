# coding: utf-8
from store.models import Category
Category.objects.all()
Category.objects.create(id='22',name='Điện thoại')
Category.objects.create(id='32',name='Điện thoại')
Category.objects.update(id='22',name='Điện thoại')
Category.objects.update(id='82',name='Điện thoại')
b.id
b = Category.objects[0]
b = Category.object[0]
b = Category.object.filter(name = 'Women-clothing')
b = Category.objects.filter(name = 'Women-clothing')
b
b.id
b.name = 'Điện thoại'
b.save()
Category.objects.filter(name = 'Women-clothing').name = 'Điện thoại'
get_ipython().run_line_magic('save', '')
