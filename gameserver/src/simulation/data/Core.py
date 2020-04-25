from src.simulation.data._Building import Building


class Core(Building):
    
    __hp = 15
    
    def getHP(self):
        return self.__hp
    
    def dealDamage(self, dmg: int):
        self.__hp -= dmg
    
    def getTeam(self):
        return self.DEFENDING
