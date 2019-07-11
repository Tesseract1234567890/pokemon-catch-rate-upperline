pokeballs = {
    'pokeball':1,
    'ultraball':2,
    'masterball':255
}


def calculate(maxHP, currentHP, captureRate, ballBonus, primaryType, secondaryType, statusAilment, rotomPow, turnNum, isBeast):
    
    catch_rate = (3 * maxHP - 2 * currentHP) * captureRate
    
    catch_rate *= captureRate
    
    if ballBonus in pokeballs:
        catch_rate *= pokeballs[ballBonus]
    
    