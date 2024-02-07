a = input() 
b = input() 
c = input()

vertebrado = {
  "ave": {"carnivoro": "aguia", "onivoro": "pombo"}, #vírgula no final de cada dicionário para separação entre outro dicionário.
  "mamifero": {"onivoro": "homem", "herbivoro": "vaca"}
}

invertebrado = {
  "inseto": {"hematofago": "pulga", "onivoro": "lagarta"},
  "alinideo": {"hematofago": "sanguessuga", "onivoro": "minhoca"},
}

if a == "vertebrado":
  if b == "ave":
    if c == "carnivoro":
      animal = vertebrado["ave"]["carnivoro"] #aguia
      print(animal)
    else:
      animal = vertebrado["ave"]["onivoro"] #pombo
      print(animal)
  else:
    if c == "onivoro":
      animal = vertebrado["mamifero"]["onivoro"] #homem
      print(animal)
    else:
      animal = vertebrado["mamifero"]["herbivoro"] #vaca
      print()      
else:
  if b == "inseto":
    if c == "hematofago":
      animal = invertebrado["inseto"]["hematofago"] #pulga
      print(animal)
    else:
      animal = invertebrado["inseto"]["onivoro"] #lagarta
      print(animal)
  else:
    if c == "hematofago":
      animal = invertebrado["alinideao"]["hematofago"] #sanguessuga
      print(animal)
    else:
      animal = invertebrado["alinideo"]["onivoro"] #minhoca
      print(animal)