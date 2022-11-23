#-----------------Made by HaxTwoWater-----------------

import random


#Initialization of some of variables
money = 100
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
cards = []

#------------------Introduction---------------

def introduction():
    
    print("-----------------------")
    print("First of all chose a language")
    print("FR (Français) or EN (english)")
    print("-----------------------")
    langAsking = input()
    if langAsking == "FR" or langAsking == "fr" or langAsking == "Fr" or langAsking == "fR":
        frIntro()
    elif langAsking == "EN" or langAsking == "en" or langAsking == "En" or langAsking == "eN":
        enGame()
    elif langAsking == "money" or langAsking == "Money" or langAsking == "Monnaie" or langAsking == "monnaie":
        print("Calm the game didn't start")
    else:
        print("Wrong value type FR or EN to chose your language please")
        introduction()

#-------------------FR Part-------------------

def frIntro():

    cls()
    print("-----------------------")
    print("Bienvenue sur notre jeu de BlackJack \nentierement fait en python !")
    rulesAsking = input("Voulez vous voir les règles ? Oui ou Non")
    if rulesAsking == "Oui":
        frRules()
    elif rulesAsking == "Non":
        frGame()
    elif rulesAsking == "monnaie":
        print("Doucement la game a pas encore commencer")
        frIntro()
    else:
        print("Mauvaise valeur veuillez taper Oui ou Non s'il vous plaît")
        frIntro()

def frRules():

    cls()
    print("Alors, comment marche le blackjack ?")
    print("------------------------------------")
    print("Valeurs des cartes :")
    print(" - Les cartes numérotés de 2 à 10 valent leur chiffre en points (exemple le 8 vaut 8 simple non ?)")
    print(" - L'as vaut soit 11 soit 1 dépend en fonction du nombre de point deja en votre possession (on y reviendra)")
    print(" - Toutes les figures valent 10")
    print("------------------------------------")
    print("Le blackjack se joue avec 1 à 8 jeux de cartes de 52 cartes dans notre cas vous pourrez choisir")
    print("Et la mise minimum (du notre en tout cas) est de 20 et le maximum 10.000 (bonne chance :p)")
    print("------------------------------------")
    print("Déroulement de la partie")
    print("La partie commence le croupier vous donnent une carte puis s'en donne une face caché puis vous en donne une deuxième et s'en donne une deuxième face découverte")
    print("Le but s'approcher au plus proche d'un total de point de 21 (si vous avez 21 vous gagnez instantanément) sans pour autant le dépasser sinon vous perdez instantanément")
    print("Après le tirage vous pouvez demander autant de carte que vous le voulez du moment que vous dépasser pas 21")
    print("Si jamais vous avez une paire vous pouvez split pour doubler votre mise et ainsi avoir deux mains en spérant le double")
    print("Vous pouvez aussi lors de votre premier tirage, demander de doubler donc doubler votre mise et faire qu'un seul tirage")
    print("------------------------------------")
    print("Cas particulier vous comme le croupier pouvez directement avoir le nombre 21 lors de la distribution \n on appel ca un blackjack et donc vous gagnez ou perdez instantanément \ndans le cas ou vous gagnez, vous gagnez 2,5x votre mise au lieu de 2")
    print('De plus vous pouvez taper a tout moment "monnaie" pour savoir combien de monnaie vous avez.')
    checkAsking = input("Avez-vous bien compris les règles ? Oui ou Non")

    if checkAsking == "Oui" or checkAsking == "oui":
        frGame()
    elif checkAsking == "Non" or checkAsking == "non":
        frRules()
    elif checkAsking == "monnaie" or checkAsking == "Monnaie":
        print("Vous avez acutellement " + money + "€ !")
        frGame()
    else:
        print("Mauvaise valeur veuillez taper soit oui soit non ")

def frGame():

    choice = 0


#------------------EN Part---------------------

def enIntro():

    cls()
    print("-----------------------")
    print("Welcome to our BlackJack game \nentirely made in python !")
    rulesAsking = input("Wanna see the rules ? Yes or No")
    if rulesAsking == "Yes" or rulesAsking == "yes":
        enRules()
    elif rulesAsking == "No" or rulesAsking == "no":
        enGame()
    elif rulesAsking == "money" or rulesAsking == "Money":
        print("Calm the game didn't start")
        enIntro()
    else:
        print("Wrong value type Yes or No please")
        enIntro()

def enRules():

    cls()
    print("So, how does the blackjack work ?")
    print("------------------------------------")
    print("Value of cards :")
    print(" - Cards between 2 and 10 are valued to their own numbers")
    print(" - The Ace is 11 or 1 depends on the total of your points when you get it")
    print(" - Then all the figures are valued at 10")
    print("------------------------------------")
    print("We are playing BlackJack from 1 to 8 pack of cards of 52 cards each (for our game you'll chose the number of packs")
    print("And the minimum bet (for our game) is 20 and the max 10.000")
    print("------------------------------------")
    print("Course of the game")
    print("The game will start and the croupier will give 1 card to you, then a card to him wich you will don't see, then another to you an finally one for him wich you'll can see")
    print("The goal is to get as close as possible to 21 or get 21 and win instantly but if you bust and get over 21 you'll lose intantly")
    print("After the initial drawing you can ask as many as you want cards if you don't get over 21 ")
    print("If you get a pair you can split and then double your bet and split your cards to get to hands")
    print("And for the first asking for a cards you can double your bet but you can ask only for 1 card")
    print("------------------------------------")
    print("Exception if you or the croupier get 21 points during the initial drawing \nwe call that a BlackJack \nin that case you'll win instantly not 2x but 2.5x or lose instantly if it's the croupier who got it")
    print('In addition you can type at any moment "money" to know your balance.')
    checkAsking = input("Did you understand the rules ? Yes or No")

    if checkAsking == "Yes" or checkAsking == "yes":
        enGame()
    elif checkAsking == "No" or checkAsking == "no":
        enRules()
    elif checkAsking == "money" or checkAsking == "Money":
        print("You have actually " + money + "$ !")
        enGame()
    else:
        print("Wrong value type Yes or No please")

def enPlayAgain(againOrPlay): #Again = true, play = false
    
    if againOrPlay == True:
        again = input("Do you want to play again ? (Yes/No)")
        if again == "Yes" or again == "yes":
            print("")
    elif againOrPlay == False:
        nbPacks = input("How many packs you want to use ? (1 to 8)")
        enGame(nbPacks)

def enGame(nbPacks):

    print("lorem")


#--------------Draw Function------------------

def draw(nbPacks):



#-----------------Made by HaxTwoWater-----------------