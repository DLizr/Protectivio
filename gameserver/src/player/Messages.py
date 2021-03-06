import asyncio

from websockets.exceptions import ConnectionClosedOK

from src.util.Logger import logger
from src.exceptions.PlayerKickedException import PlayerKickedException
from src.player.Player import Player


class Messages:

    @staticmethod
    async def askIfReady(player: Player) -> bool:
        """
        Ready = True, AFK = False.
        """
        player.clearMessages()
        await player.sendMessage("READY_CHECK")

        for _ in range(10):  # A player has 10 seconds to send the ready signal.
            msg = player.getMessageIfReceived()
            if msg == "READY":
                return True
            await player.ping()
            await asyncio.sleep(1)

        return False

    @staticmethod
    async def startPhase1(player: Player):

        player.clearMessages()
        await player.sendMessage("PHASE_1")

        for _ in range(5):
            msg = player.getMessageIfReceived()
            if msg == "OK":
                return
            await player.ping()
            await asyncio.sleep(1)

        logger.error("{} received a PHASE_1 signal but didn't respond!".format(player.getAddress()))
        await player.sendMessageSafe("KICKED:NO_RESPONSE")
        await player.disconnect()
        raise PlayerKickedException(player, "No response")

    @staticmethod
    async def startPhase2(player: Player):

        player.clearMessages()
        await player.sendMessage("PHASE_2")

        for _ in range(5):
            msg = player.getMessageIfReceived()
            if msg == "OK":
                return
            await player.ping()
            await asyncio.sleep(1)

        logger.error("{} received a PHASE_2 signal but didn't respond!".format(player.getAddress()))
        await player.sendMessageSafe("KICKED:NO_RESPONSE")
        await player.disconnect()
        raise PlayerKickedException(player, "No response")

    @staticmethod
    async def startPhase3(player: Player):

        player.clearMessages()
        await player.sendMessage("PHASE_3")

        for _ in range(5):
            msg = player.getMessageIfReceived()
            if msg == "OK":
                return
            await player.ping()
            await asyncio.sleep(1)

        logger.error("{} received a PHASE_3 signal but didn't respond!".format(player.getAddress()))
        await player.sendMessageSafe("KICKED:NO_RESPONSE")
        await player.disconnect()
        raise PlayerKickedException(player, "No response")

    @staticmethod
    async def getBase(player: Player):

        player.clearMessages()
        await player.sendMessage("GET_BASE")

        for _ in range(5):
            msg = player.getMessageIfReceived()
            if msg == "OK":
                return
            await player.ping()
            await asyncio.sleep(1)

        logger.error("{} received a GET_BASE signal but didn't respond!".format(player.getAddress()))
        await player.sendMessageSafe("KICKED:NO_RESPONSE")
        await player.disconnect()
        raise PlayerKickedException(player, "No response")

    @staticmethod
    async def sendBase(player: Player):

        player.clearMessages()
        await player.sendMessage("SEND_BASE")

        for _ in range(5):
            msg = player.getMessageIfReceived()
            if msg == "OK":
                return
            await player.ping()
            await asyncio.sleep(1)

        logger.error("{} received a SEND_BASE signal but didn't respond!".format(player.getAddress()))
        await player.sendMessageSafe("KICKED:NO_RESPONSE")
        await player.disconnect()
        raise PlayerKickedException(player, "No response")
