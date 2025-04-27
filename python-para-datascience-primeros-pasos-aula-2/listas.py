lenguaje = 'Python'
print(lenguaje[0], lenguaje[1], lenguaje[2], lenguaje[-3], lenguaje[-2], lenguaje[-1])

pregunta = '¿Quién vino primero? ¿El huevo? ¿O fue la serpiente?'
lista_palabras = pregunta.split('?')
print(lista_palabras)

mezclas = ['Pinturas: rojo, azul y amarillo',
            'Verde: mezcla de azul y amarillo',
            'Naranja: mezcla de rojo y amarillo',
            'Morado: mezcla de rojo y azul']
print(mezclas)

unificador = '. '
cadena_mezclas = unificador.join(mezclas)
print(cadena_mezclas)

pregunta = '¿Quién vino primero? ¿El huevo? ¿O fue la serpiente?'

lista_palabras = pregunta.split()
print(lista_palabras)
razas_de_perros = ['Labrador Retriever',
                   'Bulldog Francés',
                   'Pastor Alemán',
                   'Poodle']

print(len(razas_de_perros))

razas_de_perros.insert(1, 'Golden Retriever')
print(razas_de_perros)
razas_de_perros.sort()
razas_de_perros
print(len(razas_de_perros))

razas_de_perros.insert(0,"Pastor Australiano")
print(razas_de_perros)
razas_de_perros.sort()
razas_de_perros
print(len(razas_de_perros))

razas_de_perros.pop(4)
print(razas_de_perros)
print(len(razas_de_perros))

tienda = {'nombres': ['televisión', 'celular', 'notebook', 'geladeira', 'estufa'],
          'precios': [2000, 1500, 3500, 4000, 1500]}

for clave, elementos in tienda.items():
      print(f'Clave: {clave}\nElementos:')
      for dato in elementos:
        print(dato)

precios = [100.0, 400.0, 200.0]
suma = sum(precios)
suma

help(print)
lista = [1,2,3]
dir(lista)

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']