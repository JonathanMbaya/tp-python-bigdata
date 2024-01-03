from random import randint



populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 13, "name" : "Brice" },
    { "id" : 14, "name" : "Alice" },
    { "id" : 15, "name" : "Sophia" },
    { "id" : 16, "name" : "Rasmus" },
    { "id" : 18, "name" : "Taylor" },
    { "id" : 19, "name" : "Olivia" },
    { "id" : 20, "name" : "Jessica" },
    { "id" : 21, "name" : "Anna" },
    { "id" : 22, "name" : "Samantha" },
    { "id" : 23, "name" : "Grace" },
    { "id" : 24, "name" : "Anna" },
    { "id" : 25, "name" : "Alexis" },
    { "id" : 26, "name" : "Madison" },
    { "id" : 27, "name" : "Nicole" },
    { "id" : 28, "name" : "Amanda" },
    { "id" : 29, "name" : "Haley" }  
]

# Ajouter un champ lenChar qui compte le nbre de lettre

# nom = input ('')
# nomLen =  len(nom)

# print ( f"{nom} contient exactement {nomLen} de lettre(s)")


'''
Etape 1
Ajoutez un champ lenChar qui détermine la longueur de chaque nom.

'''
# Ajoutez le champ lenChar à chaque entrée du tableau
for person in populations:
    person['lenChar'] = len(person['name'])

# Affichez le tableau mis à jour
for person in populations:
    print(person)


'''
Etape 2
Ajoutez un champ rate, puis respectivement attribuer pour chaque personne, des valeurs aléatoires comprises entre 1 et 100.

'''
# Ajouter un champ rate à chaque entrée du tableau
for i in populations:
    i['rate'] = randint(1, 100)

# Afficher le tableau
for i in populations:
    print (i)

'''
Etape 3
Déterminez les 4 personnes qui ont les meilleurs valeurs de rate.

'''
# Créer un tableau ordonné
tab_order = sorted(populations,key=lambda person: person['rate'], reverse=True)

# Sélectionnez les 4 premières personnes avec les meilleures valeurs de rate
best_rate = tab_order[:4]

# Affichez les 4 personnes avec les meilleures valeurs de rate
for person in best_rate:
    print(f"{person['name']} a une valeur de rate de {person['rate']}.")


