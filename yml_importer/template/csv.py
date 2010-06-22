# -*- coding: utf-8 -*-
# csv шаблон для импорта категорий в virtualmart
# Автор: zerc.ru

header = '^'.join((
'~category_path~',
'~category_description~',
'~category_full_image~',
'~category_thumb_image~',
'~category_products_per_row~',
'~category_browsepage~',
'~category_flypage~',
'~category_publish~',
'~category_list_order~'))

row = '^'.join((
'~%s~',
'~~',
'~~',
'~~',
'~1~',
'~browse_1~',
'~flypage.tpl~',
'~Y~',
'~%s~'))
