#!/usr/bin/env python
# coding: utf-8

import random

#choosing the pointer
def inputPlayerLetter():
    letter = " "
    while letter not in ['X','O']:
        letter = input("Choose your pointer: ").upper()
    if letter == "X":
            letter = ['X','O']
    else:
            letter = ['O','X']
    return letter

#board is a string of pointers
def drawBoard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'user'

def playAgain():
    a = input("Do you want to play again?(y/n):").lower()
    if a == "y":
        return True 
    else:
        return False

def makeMove(board,move,letter):
    board[move] = letter

def isWinner(board,le):
    return ((board[1] == le and board[2] == le and board[3] == le) or
            (board[4] == le and board[5] == le and board[6] == le) or 
            (board[7] == le and board[8] == le and board[9] == le) or
            (board[1] == le and board[4] == le and board[7] == le) or
            (board[2] == le and board[5] == le and board[8] == le) or
            (board[3] == le and board[6] == le and board[9] == le) or
            (board[1] == le and board[5] == le and board[9] == le) or
            (board[3] == le and board[5] == le and board[7] == le))

def getBoardCopy(board):
    dupeboard=[]
    for i in board:
        dupeboard.append(i)
    return dupeboard

def isSpaceFree(board,move):
    return board[move] == " "

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        move = int(input("Whats your next move??(1/9)"))
    return move

def chooseRandomMoveFromList(board,moveslist):
    possiblemoves = []
    for i in moveslist:
        if isSpaceFree(board,i):
            possiblemoves.append(i)
    if len(possiblemoves) == 0:
        return None
    else:
        return possiblemoves

def getComputerMove(board,computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter= 'X'
    for i in range(1,10):
        if isSpaceFree(board,i):
            copy = getBoardCopy(board)
            if isWinner(copy,computerLetter):
                makeMove(copy,i,computerLetter)
                return i
    
    for i in range(1,10):
        if isSpaceFree(board,i):
            copy = getBoardCopy(board)
            if isWinner(copy,playerLetter):
                makeMove(copy,i,playerLetter)
                return i
    move = chooseRandomMove(board,[1,3,7,9]) #copy
    if move!= None:
        return move
    
    if isSpaceFree(board,5):
        return 5
    
    return chooseRandomMove(board,[2,4,6,8])

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
        else:
            return True
        
print("WELCOME HEHHE AAO AAO")
while True:
    theBoard = [' ']*10
    plt,clt = inputPlayerLetter()
    turn = whoGoesFirst()
    print("it's"+turn+ "turn")
    gameIsPlaying = True
    
    
    while gameIsPlaying:
        
        if turn == 'user':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,move,plt)
            
            
            if isWinner(theBoard,plt):
                drawBoard(theBoard)
                print("hehehjeet gaya")
                gameIsPlaying = False
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print("tieaya")
                gameIsPlaying = False
            else:
                turn = 'computer'
        else:
            move = getComputerMove(theBoard,clt)
            makeMove(theBoard,move,clt)
            
            if isWinner(theBoard,clt):
                drawBoard(theBoard)
                print("haar gaya")
                gameIsPlaying = False
            
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print("tieaya")
                gameIsPlaying = False        
        
    if not playAgain():
        break
  

