import asyncio

from src.util.Logger import logger
from src.exceptions.PlayerKickedException import PlayerKickedException
from src.player.Messages import Messages
from src.player.Player import Player
from src.game.Phase1 import Phase1


class Game:

    def __init__(self, ID: int):
        self.__ID = ID
    
    async def start(self, player1: Player, player2: Player):
        if not await Messages.askIfReady(player1):
            await player1.disconnect()
            raise PlayerKickedException(player1, "Not ready for battle")
        if not await Messages.askIfReady(player2):
            await player2.disconnect()
            raise PlayerKickedException(player2, "Not ready for battle")
        p1 = Phase1(player1, player2)
        logger.debug("Game #{}: phase 1 begins.".format(self.__ID))
        await p1.start()