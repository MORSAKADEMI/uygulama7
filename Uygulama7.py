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

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.  (sanırım liste değil dictionary olacaktı)
players = {
        "1":{"name":"Cristiano Ronaldo","yearOfBirth":"1985","nationality":"Portugal","current_team":"Portugal","history":"Juventus,Real Madrid,Portugal"},
        "2":{"name":"Lionel Messi","yearOfBirth":"1987","nationality":"Argentina","current_team":"Barcelona","history":"Barcelona,Argentina,Portugal"}
    }

# 2- id' e göre arama yapınız.(get ile de yapılabilir)
id = input("oyuncu id'si giriniz:")
if id in players:
    print(players[id])
else:
    print("böyle birisi bulunmamaktadır")

# 3- id' e göre bilgi kayıt siliniz.
silinecek_id = input("silmek istediğiniz bilginin id'sini giriniz:")
if silinecek_id in players:
    players.pop(silinecek_id)
else:
    print("bu bilgi mevcut değildir")