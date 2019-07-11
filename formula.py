pokeballs = {
    'pokeball':1,
    'ultraball':2,
    'masterball':255
}


def calculate(maxHP, currentHP, caughtPokemon, captureRate, ballBonus, primaryType, secondaryType, statusAilment, rotomPow, turnNum, isBeast):
    
    catch_rate = (3 * int(maxHP) - 2 * int(currentHP))
    
    catch_rate *= int(captureRate)
    
    if ballBonus in pokeballs:
        catch_rate *= pokeballs[ballBonus]
    
    
    
    catch_rate /= (3 * int(maxHP))
    
    breakout_chance = (catch_rate / 255)**(0.75 / 4)
    
    crit_mod = 0
    
    if caughtPokemon > 600:
        crit_mod = 2.5
    elif caughtPokemon > 450:
        crit_mod = 2
    elif caughtPokemon > 300:
        crit_mod = 1.5
    elif caughtPokemon > 150:
        crit_mod = 1
    elif caughtPokemon > 30:
        crit_mod = 0.5
    else:
        crit_mod = 0
    
    critical_chance = (catch_rate * crit_mod/6) / 256
    
    return str(100 * ((critical_chance * breakout_chance) + (1 - critical_chance) * breakout_chance**4)) + "%"