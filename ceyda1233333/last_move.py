def lastMoveEnd(wonPlayer): # Oyunu Sonlandıran Fonksiyon
    lastQuery = input('\n\nPlayer ' + wonPlayer + ' won the game.\nWould you like to play again(Y/N)?: ')
    lastQuery = str(lastQuery).upper()
        
    if lastQuery == 'Y':
        return lastMovePlay()
        
    elif lastQuery == 'N':
        print('Byee..')

def lastMovePlay():        
    player1 = input('Enter a capital letter to represent player 1 (except O): ') # Player1 için isim sorgusu
    player1 = str(player1).upper()

    player2 = input('Enter a capital letter to represent player 2 (except O): ') # Player 2 için isim sorgusu
    player2 = str(player2).upper()
    
    if player1 == player2 or player1 == 'O' or player2 == 'O': # oyuncuların isimlerinin birbiriyle aynı olmasını ve O karakterini içermemesini sağlayan if döngüsü.
        print('Player names cannot be the same and cannot contain the letter O!')
        return lastMovePlay() ## işlem true ise başa sarıyor.
    
    else: # ilk if sorgusundan geçti
        def movement(rows, column): # 3
            def fieldOutput(rows, column, playerLoc, player, rock):
                # ------Field Çıktısı------
                print('', end="    ")
                for f in range(len(column)):
                    print(column[f], end="   ")
                for f2 in range(len(column)):
                    print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                    print(f2 + 1, end=" | ")
                    for f3 in range(len(column)):
                        print(rows['row' + str(f2 + 1)][f3], end=" | ")
                    print(f2 + 1, end="")
                print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                print('', end="    ")
                for f in range(len(column)):
                    print(column[f], end="   ")
                
                if rock == 'big':
                    if player == player1:
                        return movementPlayer(player2)
                    
                    elif player == player2:
                        return movementPlayer(player1)
                    
                elif rock == 'small':
                    return movementControl(rows, column, playerLoc, player, rock)
            
            def movementControl(rows, column, playerLoc, player, rock):
                    locs = ['N','S','E','W','NE','NW','SE','SW']
                    
                    fullness = 0
                    #Row Kontrolü
                    if (playerLoc[2] - 1) == 0 or rows['row' + str(playerLoc[2] - 1)][playerLoc[3]] != " ":
                        locs.remove('N')
                        fullness += 1
                        
                    if (playerLoc[2] + 1) > len(rows) or rows['row' + str(playerLoc[2] + 1)][playerLoc[3]] != " ":
                        locs.remove('S')
                        fullness += 1
                    
                    #Column Kontrolü
                    if(playerLoc[3] + 1) == len(column) or rows[playerLoc[0]][playerLoc[3] + 1] != " ":
                        locs.remove('E')
                        fullness += 1
                        
                    if(playerLoc[3] - 1) < 0 or rows[playerLoc[0]][playerLoc[3] - 1] != " ":
                        locs.remove('W')
                        fullness += 1
                    
                    #Köşelerin Kontrolleri
                    if(playerLoc[2] - 1) == 0 or (playerLoc[3] + 1) == len(column) or rows['row' + str(playerLoc[2] - 1)][playerLoc[3] + 1] != " ":
                        locs.remove('NE')                    
                        fullness += 1
                    
                    if(playerLoc[2] - 1) == 0 or (playerLoc[3] - 1) < 0 or rows['row' + str(playerLoc[2] - 1)][playerLoc[3] - 1] != " ":
                        locs.remove('NW')
                        fullness += 1
                    
                    if(playerLoc[2] + 1) > len(rows) or (playerLoc[3] + 1) == len(column) or rows['row' + str(playerLoc[2] + 1)][playerLoc[3] + 1] != " ":
                        locs.remove('SE')
                        fullness += 1
                    
                    if(playerLoc[2] + 1) > len(rows) or (playerLoc[3] - 1) < 0 or rows['row' + str(playerLoc[2] + 1)][playerLoc[3] - 1] != " ":
                        locs.remove('SW')
                        fullness += 1
                    
                    if fullness == 8:
                        if player == player1:
                            return lastMoveEnd(player2) # bitirme fonksiyonu
                        
                        elif player == player2:
                            return lastMoveEnd(player1) # bitirme fonksiyonu
                    
                    else:
                        if rock == 'big':
                            newLocation = input('\n\nPlayer ' + player + ' please enter the direction you want to move your own big stone'+  str(locs) + ': ')
                            newLocation = str(newLocation).upper()
                            
                            for nl in range(len(locs)): # Hareket komutu fonksiyonu
                                if locs[nl] == newLocation:
                                    if newLocation == 'S':
                                        rows[playerLoc[0]][playerLoc[3]] = ' '
                                        playerLoc[2] += 1
                                        playerLoc[0] = 'row' + str(playerLoc[2])
                                        rows[playerLoc[0]][playerLoc[3]] = player
                                        
                                        # Field Çıktısını Çağırıyorum
                                        return fieldOutput(rows, column, playerLoc, player, 'small')
                                        
                                    elif newLocation == 'E':
                                        rows[playerLoc[0]][playerLoc[3]] = ' '
                                        playerLoc[3] += 1
                                        playerLoc[1] = column[playerLoc[3]]
                                        rows[playerLoc[0]][playerLoc[3]] = player
                                            
                                        # Field Çıktısını Çağırıyorum
                                        return fieldOutput(rows, column, playerLoc, player , 'small')
                                    
                                    elif newLocation == 'W':
                                        rows[playerLoc[0]][playerLoc[3]] = ' '
                                        playerLoc[3] -= 1
                                        playerLoc[1] = column[playerLoc[3]]
                                        rows[playerLoc[0]][playerLoc[3]] = player 
                                        
                                        # Field Çıktısını Çağırıyorum
                                        return fieldOutput(rows, column, playerLoc, player, 'small')
                                    
                                    elif newLocation == 'SE':
                                        rows[playerLoc[0]][playerLoc[3]] = ' '
                                        playerLoc[2] += 1
                                        playerLoc[0] = 'row' + str(playerLoc[2])
                                        playerLoc[3] += 1
                                        playerLoc[1] = column[playerLoc[3]]
                                        rows[playerLoc[0]][playerLoc[3]] = player 
                                        
                                        # Field Çıktısını Çağırıyorum
                                        return fieldOutput(rows, column, playerLoc, player, 'small')
                                    
                                    elif newLocation == 'SW':
                                        rows[playerLoc[0]][playerLoc[3]] = ' '
                                        playerLoc[2] += 1
                                        playerLoc[0] = 'row' + str(playerLoc[2])
                                        playerLoc[3] -= 1
                                        playerLoc[1] = column[playerLoc[3]]
                                        rows[playerLoc[0]][playerLoc[3]] = player 
                                        
                                        # Field Çıktısını Çağırıyorum
                                        return fieldOutput(rows, column, playerLoc, player, 'small')
                                    
                                    elif newLocation == 'N':
                                        rows[playerLoc[0]][playerLoc[3]] = ' '
                                        playerLoc[2] -= 1
                                        playerLoc[0] = 'row' + str(playerLoc[2])
                                        rows[playerLoc[0]][playerLoc[3]] = player 
                                        
                                        # Field Çıktısını Çağırıyorum
                                        return fieldOutput(rows, column, playerLoc, player, 'small')
                                    
                                    elif newLocation == 'NE':
                                        rows[playerLoc[0]][playerLoc[3]] = ' '
                                        playerLoc[2] -= 1
                                        playerLoc[0] = 'row' + str(playerLoc[2])
                                        playerLoc[3] += 1
                                        playerLoc[1] = column[playerLoc[3]]
                                        rows[playerLoc[0]][playerLoc[3]] = player 
                                        
                                        # Field Çıktısını Çağırıyorum
                                        return fieldOutput(rows, column, playerLoc, player, 'small')
                                    
                                    elif newLocation == 'NW':
                                        rows[playerLoc[0]][playerLoc[3]] = ' '
                                        playerLoc[2] -= 1
                                        playerLoc[0] = 'row' + str(playerLoc[2])
                                        playerLoc[3] -= 1
                                        playerLoc[1] = column[playerLoc[3]]
                                        rows[playerLoc[0]][playerLoc[3]] = player 
                                        
                                        # Field Çıktısını Çağırıyorum
                                        return fieldOutput(rows, column, playerLoc, player, 'small')
                                    
                            else:
                                print('\nInvalid Value..')
                                return movementPlayer(player)
                                
                        elif rock == 'small':
                                smallRock = input('\n\nPlayer ' + player + ', please enter the location where you want to place a small stone (like 1A):')
                                smallRock = str(smallRock).upper()
                                
                                rowRockLoc = smallRock[0]
                                columnRockLoc = smallRock[1]
                                
                                for c in range(len(column)):
                                    if column[c] == columnRockLoc:
                                        columnRockLoc = c
                                        
                                        if rows['row' + str(rowRockLoc)][c] == " ":
                                            rows['row' + str(rowRockLoc)][c] = 'O'
                                            return fieldOutput(rows, column, playerLoc, player, 'big')
                                        
                                        elif rowRockLoc > len(rows) or rowRockLoc < 1:
                                            movementControl(rows, column, playerLoc, player, 'small')

                                        else:
                                            movementControl(rows, column, playerLoc, player, 'small')
                                    else:
                                        movementControl(rows, column, playerLoc, player, 'small')
                        
            def movementPlayer(startPlayer): # 2
                for x in range(1,len(rows) + 1):
                    for y in range(len(rows)):
                        if rows['row'+str(x)][y] == startPlayer:
                            startPlayerLoc = []
                            startPlayerLoc.append('row'+str(x))
                            startPlayerLoc.append(column[y])
                            startPlayerLoc.append(x)
                            startPlayerLoc.append(y)
            
                            return movementControl(rows, column, startPlayerLoc, startPlayer, 'big')
                        
            return movementPlayer(player1)
                
        def playingFieldQuery(): # 1 Oyun Alanı Sorgusu
            playingField = input('Enter the row/column number of the playing field (3, 5, 7): ')
            playingField = str(playingField) ## Hata Kontrolde sorun olmaması için string olarak kayıt ediyorum
        
            if playingField != '3' and playingField != '5' and playingField != '7':
                print('Just 3, 5, 7') ## Oyuncu oyun alanını 3 5 7 dışında bir değer girerse uyarıp oyun alanı sorugusunu yeniden başlatıyor.
                return playingFieldQuery()
            
            elif playingField == '3':
                    column = ['A','B','C'] # sütun
                    rows = { # sıra
                    "row1": [' ',' ',' '],
                    "row2": [' ',' ',' '],
                    "row3": [' ',' ',' ']
                    }
                    
                    a = len(rows) / 2  # Merkezini bulup int`e çeviriyorum ki 1.5 u 1 olarak alsın
                    a = int(a)
                    rows['row'+ str(1)][a] = player1 # Oyuncular gerekli yerlere oturtuldu
                    rows['row'+ str(len(rows))][a] = player2
                    
                    # ------Field Çıktısı------
                    print('', end="    ")
                    for f in range(len(column)):
                        print(column[f], end="   ")
                    for f2 in range(len(column)):
                        print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                        print(f2 + 1, end=" | ")
                        for f3 in range(len(column)):
                            print(rows['row' + str(f2 + 1)][f3], end=" | ")
                        print(f2 + 1, end="")
                    print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                    print('', end="    ")
                    for f in range(len(column)):
                        print(column[f], end="   ")
                        
                    return movement(rows, column)
                
            elif playingField == '5':
                    column = ['A','B','C','D','E']
                    rows = {
                    "row1": [' ',' ',' ',' ',' '],
                    "row2": [' ',' ',' ',' ',' '],
                    "row3": [' ',' ',' ',' ',' '],
                    "row4": [' ',' ',' ',' ',' '],
                    "row5": [' ',' ',' ',' ',' ']
                    }
                    
                    a = len(rows) / 2  # Merkezini bulup int`e çeviriyorum ki 1.5 u 1 olarak alsın
                    a = int(a)
                    rows['row'+ str(1)][a] = player1 # Oyuncular gerekli yerlere oturtuldu
                    rows['row'+ str(len(rows))][a] = player2

                    # ------Field Çıktısı------
                    print('', end="    ")
                    for f in range(len(column)):
                        print(column[f], end="   ")
                    for f2 in range(len(column)):
                        print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                        print(f2 + 1, end=" | ")
                        for f3 in range(len(column)):
                            print(rows['row' + str(f2 + 1)][f3], end=" | ")
                        print(f2 + 1, end="")
                    print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                    print('', end="    ")
                    for f in range(len(column)):
                        print(column[f], end="   ")
                        
                    return movement(rows, column)
                
            elif playingField == '7':
                column = ['A','B','C','D','E','F','G']
                rows = {
                    "row1": [' ',' ',' ',' ',' ',' ',' '],
                    "row2": [' ',' ',' ',' ',' ',' ',' '],
                    "row3": [' ',' ',' ',' ',' ',' ',' '],
                    "row4": [' ',' ',' ',' ',' ',' ',' '],
                    "row5": [' ',' ',' ',' ',' ',' ',' '],
                    "row6": [' ',' ',' ',' ',' ',' ',' '],
                    "row7": [' ',' ',' ',' ',' ',' ',' ']
                }
                
                a = len(rows) / 2  # Merkezini bulup int`e çeviriyorum ki 1.5 u 1 olarak alsın
                a = int(a)
                rows['row'+ str(1)][a] = player1 # Oyuncular gerekli yerlere oturtuldu
                rows['row'+ str(len(rows))][a] = player2
                
                # ------Field Çıktısı------
                print('', end="    ")
                for f in range(len(column)):
                    print(column[f], end="   ")
                for f2 in range(len(column)):
                    print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                    print(f2 + 1, end=" | ")
                    for f3 in range(len(column)):
                        print(rows['row' + str(f2 + 1)][f3], end=" | ")
                    print(f2 + 1, end="")
                print('\n  ','-' * int(float(len(column)) * 3.9)) # Çizgi adedini ayarlıyor
                print('', end="    ")
                for f in range(len(column)):
                    print(column[f], end="   ")
                        
                return movement(rows, column)
            
        playingFieldQuery()
lastMovePlay()