import random
import turtle

ventana = turtle.Screen()
ventana.title("Carrera de Tortus")
ventana.bgcolor('black')
ventana.setup(width=800, height=600)

caracol_1 = turtle.Turtle()
caracol_1.shape("turtle")
caracol_1.color("red")
caracol_1.penup()
caracol_1.goto(-300,100)

caracol_2 = turtle.Turtle()
caracol_2.shape("turtle")
caracol_2.color("green")
caracol_2.penup()
caracol_2.goto(-300,0)

meta = 300
while True:
    avance_caracaol_1 = random.randint(1,20)
    avance_caracaol_2 = random.randint(1,20)
    
    caracol_1.forward(avance_caracaol_1)
    caracol_2.forward(avance_caracaol_2)
    
    print(f"El caracol_1 avanza {caracol_1}, para un total de: {caracol_1.xcor()}")
    print(f"El caracol _2 avanza {caracol_2}, para un total de: {caracol_2.xcor()}")
    print(f"-------------------------")
    
    if caracol_1.xcor() >=meta or caracol_2.xcor()>=meta:
        break


if caracol_1.xcor()  > caracol_2.xcor() :
    print("Felicidades sr. Caracol_1, ha llegado a la meta")
elif caracol_2.xcor()  > caracol_1.xcor() :
    print("Felicidades sr. Caracol_2, ha llegado a la meta")
else:
    print("Ambos caracoles han llegado a la meta")

ventana.exitonclick()

