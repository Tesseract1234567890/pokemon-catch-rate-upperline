import formula

maxHP = input("What is the maximum HP of the Pokemon you are trying to capture?")
currentHP = input("What is the current HP of the Pokemon you are trying to capture?")
caughtPokemon = input("How many Pokemon species have you captured?")
captureRate = input("What is the intrinsic catch rate (go to Bulbapedia if you don't know what this is) of the Pokemon you are trying to capture?")
ballBonus = input("What type of ball are you trying to use to catch the Pokemon? (Use proper spacing!)")
primaryType = input("What is the first type of your Pokemon?")
secondaryType = input("What is the second type, if any, of you Pokemon?")
statusAilment = input("Does the Pokemon have a status ailment? (If no, leave blank)")
rotomPow = input("What is the level of Rotom Power you are using, if any?")
turnNum = input("What is the turn number of the battle you are in when trying to catch the Pokemon?")
isBeast = input("Is your Pokemon a Beast? (Yes or No)")

print (formula.calculate(maxHP, currentHP, caughtPokemon, captureRate, ballBonus, primaryType, secondaryType, statusAilment, rotomPow, turnNum, isBeast))