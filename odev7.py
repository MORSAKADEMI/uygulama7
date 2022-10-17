'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
players = {
    '1': {"name": "Ronaldo","year of birthday": "1985","nationality": "Portugal","current team": "Manchester United","history": "Juventus, Real Madrid"},
    '2': {"name": "Messi","year of birthday": "1987","nationality": "Argentina","current team": "PSG","history": "Barcelona, Argentina"}
}
# 2- id' e göre arama yapınız.
id = input("id: ")
print(players[id])
# 3- id' e göre bilgi kayıt siliniz.
del players[id]
print(players)