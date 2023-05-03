#                         ******   Proyecto Sombrero Seleccionador   ******
""""
Es un sombrero parlante mágico en el Colegio Hogwarts de Magia y Hechicería. El sombrero decide a cuál de las cuatro "Casas" va cada estudiante de primer año:
🦁Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin
"""

casa_gryffindor = 0
casa_ravenclaw = 0
casa_hufflepuff = 0
casa_slytherin = 0

# #. -   ******   Pregunta 1   ******s
question_p1 = int(input("P1. - Que te gusta mas? 1. - Amanecer / 2. - Anochecer: "))

if question_p1 == 1:
   print("1. - Amanecer")
   print("🦁 Gryffindor")
   print("🦅 Ravenclaw")
   print("Estas Casas SUMAN + 1 Pto.")
   resp = "1. - Amanecer"
   casa_gryffindor = casa_gryffindor +1
   casa_ravenclaw = casa_ravenclaw +1
elif question_p1 == 2:
   print("2. - Anochecer")
   print("🦡 Hufflepuff")
   print("🐍 Slytherin")
   print("Estas Casas SUMAN + 1 Pto.")
   resp = "2. - Anochecer"
   casa_hufflepuff = casa_hufflepuff +1
   casa_slytherin = casa_slytherin +1
else:
   print("Entrada INCORRECTA")

# #. -   ******   Pregunta 2   ******
question_p2 = int(input("P2. - Cuando esté muerto, quiero que la gente me recuerde como: 1. - El Bien / 2. - El Grande 3. - El Sabio / 4. - El Audaz "))

if question_p2 == 1:
   print("1. - El Bien")
   print("🦡 Hufflepuff")
   print("Esta Casa SUMAN + 2 Ptos.")
   resp = "1. - El Bien"
   casa_hufflepuff = casa_hufflepuff +2   
elif question_p2 == 2:
   print("1. - El Grande")
   print("🐍 Slytherin")
   print("Esta Casa SUMAN + 2 Ptos.")
   resp = "2. - El Grande"
   casa_slytherin = casa_slytherin +2
elif question_p2 == 3:
   print("1. - El Sabio")
   print("🦅 Ravenclaw")
   print("Esta Casa SUMAN + 2 Ptos.")
   resp = "3. - El Sabio"
   casa_ravenclaw = casa_ravenclaw +2
elif question_p2 == 4:
   print("1. - El Audaz")
   print("🦁 Gryffindor")
   print("Esta Casa SUMAN + 2 Ptos.")
   resp = "4. - El Audaz"
   casa_gryffindor = casa_gryffindor +2
else:
   print("Entrada INCORRECTA")

# #. -   ******   Pregunta 3   ******
question_p3 = int(input("P3. - Qué tipo de instrumento agrada más a tu oído? 1. - El Violin / 2. - La Trompeta / 3. - El Piano / 4. - El Tambor "))

if question_p3 == 1:
   print("1. - El Violin")
   print("🐍 Slytherin")
   print("Esta Casa SUMAN + 4 Ptos.")
   resp = "1. - El Violin"
   casa_slytherin = casa_slytherin +4
elif question_p3 == 2:
   print("1. - La Trompeta")
   print("🦡 Hufflepuff")
   print("Esta Casa SUMAN + 4 Ptos.")
   resp = "2. - La Trompeta"
   casa_hufflepuff = casa_hufflepuff +4
elif question_p3 == 3:
   print("1. - El Piano")
   print("🦅 Ravenclaw")
   print("Esta Casa SUMAN + 4 Ptos.")
   resp = "3. - El Piano"
   casa_ravenclaw = casa_ravenclaw +4
elif question_p3 == 4:
   print("1. - El Tambor")
   print("🦁 Gryffindor")
   print("Esta Casa SUMAN + 4 Ptos.")
   resp = "4. - El Tambor"
   casa_gryffindor = casa_gryffindor +4
else:
   print("Entrada INCORRECTA")

# #. -   ****** Realizando comparacion de Casa con mayor cantidad de puntos   ******

if (casa_gryffindor > casa_ravenclaw) and (casa_gryffindor > casa_hufflepuff) and (casa_gryffindor > casa_slytherin):
   print("La Casa con mas puntos es: 🦁 Gryffindor con:",casa_gryffindor, "puntos")
elif (casa_ravenclaw > casa_gryffindor) and (casa_ravenclaw > casa_slytherin) and (casa_ravenclaw > casa_hufflepuff):
   print("La Casa con mas puntos es: 🦅 Ravenclaw con:",casa_ravenclaw, "puntos")
elif (casa_hufflepuff > casa_gryffindor) and (casa_hufflepuff > casa_ravenclaw) and (casa_hufflepuff > casa_slytherin):
   print("La Casa con mas puntos es: 🦡 Hufflepuff con:",casa_hufflepuff, "puntos")
else:
   print("La Casa con mas puntos es: 🐍 Slytherin con:",casa_slytherin, "puntos")

