animals = ['leão', 'tigre', 'girafa', 'elefante', 'crocodilo', 'gato', 'cachorro', 'papagaio', 'pomba' , 'coruja', 'gavião', 'peixe-boi', 'baleia', 'tubarão', 'polvo', 'caranguejo', 'formiga', 'abelha', 'borboleta' , 'aranha']

animals.sort()

for animals in animals:
    print(animals)

with open('animals.csv','w') as f:
    for animal in animals:
        f.write("%s\n" % animal)