# Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. 
# A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. 


goal = float(input('how much money do you wanna save?'))
saved = 0.0 
while saved > goal:
    saved = float(input('How much money you wanna save this time?'))
print("You've reached your goal!")
