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
    
    breakout_chance = (catch_rate / 255)**0.75
    
    return str(breakout_chance * 100) + "%"