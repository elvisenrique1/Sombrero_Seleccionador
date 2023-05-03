#                         ******   Proyecto Sombrero Seleccionador   ******
""""
Es un sombrero parlante mágico en el Colegio Hogwarts de Magia y Hechicería. El sombrero decide a cuál de las cuatro "Casas" va cada estudiante de primer año:
🦁Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin
"""

casa_gryffindor_p1 = 0
casa_gryffindor_p2 = 0
casa_gryffindor_p3 = 0
casa_ravenclaw_p1 = 0
casa_ravenclaw_p2 = 0
casa_ravenclaw_p3 = 0
casa_hufflepuff_p1 = 0
casa_hufflepuff_p2 = 0
casa_hufflepuff_p3 = 0
casa_slytherin_p1 = 0
casa_slytherin_p2 = 0
casa_slytherin_p3 = 0

tp_casa_gryffindor = casa_gryffindor_p1 + casa_gryffindor_p2 + casa_gryffindor_p3
tp_casa_ravenclaw = casa_ravenclaw_p1 + casa_ravenclaw_p2 + casa_ravenclaw_p3
tp_casa_hufflepuff = casa_hufflepuff_p1 + casa_hufflepuff_p2 + casa_hufflepuff_p3
tp_casa_slytherin = casa_slytherin_p1 + casa_slytherin_p2 + casa_slytherin_p3

total_ptos = 0

# #. -   ******   Pregunta 1   ******s
question_p1 = int(input("P1. - Que te gusta mas? 1. - Amanecer / 2. - Anochecer: "))

if question_p1 == 1:
   print("1. - Amanecer")
   print("🦁 Gryffindor")
   print("🦅 Ravenclaw")
   print("Estas Casas SUMAN + 1 Pto.")
   resp = "1. - Amanecer"
   tp_casa_gryffindor = casa_gryffindor_p1 +1
   tp_casa_ravenclaw = casa_ravenclaw_p1 +1
elif question_p1 == 2:
   print("2. - Anochecer")
   print("🦡 Hufflepuff")
   print("🐍 Slytherin")
   print("Estas Casas SUMAN + 1 Pto.")
   resp = "2. - Anochecer"
   tp_casa_hufflepuff = casa_hufflepuff_p1 +1
   tp_casa_slytherin = casa_slytherin_p1 +1
else:
   print("Entrada INCORRECTA")

# #. -   ******   Pregunta 2   ******
question_p2 = int(input("P2. - Cuando esté muerto, quiero que la gente me recuerde como: 1. - El Bien / 2. - El Grande 3. - El Sabio / 4. - El Audaz "))

if question_p2 == 1:
   print("1. - El Bien")
   print("🦡 Hufflepuff")
   print("Esta Casa SUMAN + 2 Ptos.")
   resp = "1. - El Bien"
   tp_casa_hufflepuff = casa_hufflepuff_p2 +2   
elif question_p2 == 2:
   print("1. - El Grande")
   print("🐍 Slytherin")
   print("Esta Casa SUMAN + 2 Ptos.")
   resp = "2. - El Grande"
   tp_casa_slytherin = casa_slytherin_p2 +2
elif question_p2 == 3:
   print("1. - El Sabio")
   print("🦅 Ravenclaw")
   print("Esta Casa SUMAN + 2 Ptos.")
   resp = "3. - El Sabio"
   tp_casa_ravenclaw = casa_ravenclaw_p2 +2
elif question_p2 == 4:
   print("1. - El Audaz")
   print("🦁 Gryffindor")
   print("Esta Casa SUMAN + 2 Ptos.")
   resp = "4. - El Audaz"
   tp_casa_gryffindor = casa_gryffindor_p2 +2
else:
   print("Entrada INCORRECTA")

# #. -   ******   Pregunta 3   ******
question_p3 = int(input("P3. - Qué tipo de instrumento agrada más a tu oído? 1. - El Violin / 2. - La Trompeta / 3. - El Piano / 4. - El Tambor "))

if question_p3 == 1:
   print("1. - El Violin")
   print("🐍 Slytherin")
   print("Esta Casa SUMAN + 4 Ptos.")
   resp = "1. - El Violin"
   tp_casa_slytherin = casa_slytherin_p3 +4
elif question_p3 == 2:
   print("1. - La Trompeta")
   print("🦡 Hufflepuff")
   print("Esta Casa SUMAN + 4 Ptos.")
   resp = "2. - La Trompeta"
   tp_casa_hufflepuff = casa_hufflepuff_p3 +4
elif question_p3 == 3:
   print("1. - El Piano")
   print("🦅 Ravenclaw")
   print("Esta Casa SUMAN + 4 Ptos.")
   resp = "3. - El Piano"
   tp_casa_ravenclaw = casa_ravenclaw_p3 +4
elif question_p3 == 4:
   print("1. - El Tambor")
   print("🦁 Gryffindor")
   print("Esta Casa SUMAN + 4 Ptos.")
   resp = "4. - El Tambor"
   tp_casa_gryffindor = casa_gryffindor_p3 +4
else:
   print("Entrada INCORRECTA")

# #. -   ****** Realizando comparacion de Casa con mayor cantidad de puntos   ******

if (tp_casa_gryffindor > tp_casa_ravenclaw) and (tp_casa_gryffindor > tp_casa_hufflepuff) and (tp_casa_gryffindor > tp_casa_slytherin):
   print("La Casa con mas puntos es: 🦁 Gryffindor con:",tp_casa_gryffindor, "puntos")
elif (tp_casa_ravenclaw > tp_casa_gryffindor) and (tp_casa_ravenclaw > tp_casa_slytherin) and (tp_casa_ravenclaw > tp_casa_hufflepuff):
   print("La Casa con mas puntos es: 🦅 Ravenclaw con:",tp_casa_ravenclaw, "puntos")
elif (tp_casa_hufflepuff > tp_casa_gryffindor) and (tp_casa_hufflepuff > tp_casa_ravenclaw) and (tp_casa_hufflepuff > tp_casa_slytherin):
   print("La Casa con mas puntos es: 🦡 Hufflepuff con:",tp_casa_hufflepuff, "puntos")
else:
   print("La Casa con mas puntos es: 🐍 Slytherin con:",tp_casa_slytherin, "puntos")





