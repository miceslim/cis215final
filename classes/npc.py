import classes.items as items


class NonPlayableCharacter:
    """NPC class will raise a NotImplementedError if the
       NPC has not been previously created.

       NPC class returns the name of the SupportingCharacter.

       NPC class will be called on two separate tiles: the
       HiLineVendingMachineTile and the AlienTraderTile. Currently, there are two instances
       of this class: AlienTrader and HiLineVendingMachine.

       The AlienTrader only accepts and returns Monopoly Money as payment, however
       the AlienTrader does make trades with the player if the player has
       something the AlienTrader wants for their inventory. While the AlienTrader
       only accepts Monopoly Money as payment, it is stored as the variable
       creditTotal in the AlienTrader class. The variable creditTotal will increase
       and the AlienTrader's inventory will decrease as the game continues.

       The HiLineVendingMachine accepts Monopoly Money, Chuck E CHeese Tokens, or
       Visa Gift Cards as payments for purchases of an item in the vending machine's
       inventory. The HiLineVendingMachine does not make trades for the items
       in its inventory. While the HiLineVendingMachine accepts Monopoly Money,
       Chuck E Cheese Tokens, and Visa Gift Cards as payment, all three are stored
       as the variable creditTotal in the HiLineVendingMachine class. The variable
       creditTotal will increase and the HiLineVendingMachine's inventory will decrease
       as the game continues.


        -Treasure"""

    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.BottleOfRum()
                         items.randomweapon
                         items.randomconsume]

class AlienTrader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Alien Trader"
        self.CreditTotal = 250
        self.inventory = [items.DayOldFrenchBaguette(),
                          items.DayOldFrenchBaguette(),
                          items.RumAndCoke(),
                          items.FourPackOfRedBull()
                         items.randomconsume
                         items.randomweapon]


class HiLineVendingMachine(NonPlayableCharacter):
    def __init__(self):
        self.name = "HiLine Vending Machine"
        self.CreditTotal = 740
        self.inventory = [items.DayOldFrenchBaguette(),
                          items.DayOldFrenchBaguette(),
                          items.DayOldFrenchBaguette(),
                          items.randomconsume,
                          items.RumAndCoke(),
                          items.RumAndCoke(),
                          items.randomitem,
                          items.FourPackOfRedBull(),
                          items.FourPackOfRedBull(),
                          items.randomconsume,
                          items.BottleOfAspirin(),
                          items.randomconsume]

