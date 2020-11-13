repas=6
semaine=3
x=int(input("combien de semaines avez vous mangé dans l'année? "))
semaines=x
prix=(repas*semaine*semaines)
poche=int(600 - prix)
print( "vous avez dépensé", prix , "euros")
print ("il vous reste" , poche ,"euros")