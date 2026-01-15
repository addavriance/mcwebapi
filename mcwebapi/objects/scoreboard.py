from typing import List, Dict, Optional

from .base import SocketInstance
from ..core.client import MinecraftClient
from ..types import ObjectiveInfo, TeamInfo


class Scoreboard(SocketInstance):
    """Scoreboard object for scoreboard management."""

    def __init__(self, client: MinecraftClient):
        super().__init__("scoreboard", client)

    # Objectives
    async def createObjective(self, name: str, criteria_id: str, display_name: str) -> bool:
        """Create scoreboard objective."""
        return await super().__getattr__("createObjective")(name, criteria_id, display_name)

    async def removeObjective(self, name: str) -> bool:
        """Remove scoreboard objective."""
        return await super().__getattr__("removeObjective")(name)

    async def getObjectives(self) -> List[ObjectiveInfo]:
        """Get all objectives."""
        data = await super().__getattr__("getObjectives")()
        return [ObjectiveInfo(**obj) for obj in data]

    async def getObjective(self, name: str) -> ObjectiveInfo:
        """Get objective information."""
        data = await super().__getattr__("getObjective")(name)
        return ObjectiveInfo(**data)

    async def setDisplaySlot(self, slot: str, objective_name: Optional[str]) -> bool:
        """Set objective display slot."""
        return await super().__getattr__("setDisplaySlot")(slot, objective_name)

    async def getDisplaySlots(self) -> Dict[str, Optional[str]]:
        """Get all display slots."""
        return await super().__getattr__("getDisplaySlots")()

    # Teams
    async def createTeam(self, name: str) -> bool:
        """Create team."""
        return await super().__getattr__("createTeam")(name)

    async def removeTeam(self, name: str) -> bool:
        """Remove team."""
        return await super().__getattr__("removeTeam")(name)

    async def getTeams(self) -> List[TeamInfo]:
        """Get all teams."""
        data = await super().__getattr__("getTeams")()
        return [TeamInfo(**team) for team in data]

    async def getTeam(self, name: str) -> TeamInfo:
        """Get team information."""
        data = await super().__getattr__("getTeam")(name)
        return TeamInfo(**data)

    async def addPlayerToTeam(self, team_name: str, player_name: str) -> bool:
        """Add player to team."""
        return await super().__getattr__("addPlayerToTeam")(team_name, player_name)

    async def removePlayerFromTeam(self, player_name: str) -> bool:
        """Remove player from team."""
        return await super().__getattr__("removePlayerFromTeam")(player_name)

    async def setTeamDisplayName(self, team_name: str, display_name: str) -> bool:
        """Set team display name."""
        return await super().__getattr__("setTeamDisplayName")(team_name, display_name)

    async def setTeamColor(self, team_name: str, color: str) -> bool:
        """Set team color."""
        return await super().__getattr__("setTeamColor")(team_name, color)

    async def setTeamPrefix(self, team_name: str, prefix: str) -> bool:
        """Set team prefix."""
        return await super().__getattr__("setTeamPrefix")(team_name, prefix)

    async def setTeamSuffix(self, team_name: str, suffix: str) -> bool:
        """Set team suffix."""
        return await super().__getattr__("setTeamSuffix")(team_name, suffix)

    async def setTeamFriendlyFire(self, team_name: str, enabled: bool) -> bool:
        """Set team allow or disallow friendly fire."""
        return await super().__getattr__("setTeamFriendlyFire")(team_name, enabled)

    async def setTeamSeeFriendlyInvisibles(self, team_name: str, enabled: bool) -> bool:
        """Set team allow or disallow friendly fire."""
        return await super().__getattr__("setTeamSeeFriendlyInvisibles")(team_name, enabled)

    # Scores
    async def getScore(self, objective_name: str, target: str) -> Optional[int]:
        """Get score value."""
        return await super().__getattr__("getScore")(objective_name, target)

    async def setScore(self, objective_name: str, target: str, value: int) -> bool:
        """Set score value."""
        return await super().__getattr__("setScore")(objective_name, target, value)

    async def addScore(self, objective_name: str, target: str, value: int) -> bool:
        """Add to score value."""
        return await super().__getattr__("addScore")(objective_name, target, value)

    async def resetScore(self, objective_name: str, target: str) -> bool:
        """Reset score for objective."""
        return await super().__getattr__("resetScore")(objective_name, target)

    async def resetAllScores(self, target: str) -> bool:
        """Reset all scores for target."""
        return await super().__getattr__("resetAllScores")(target)

    async def getScores(self, target: str) -> Dict[str, int]:
        """Get all scores for target."""
        return await super().__getattr__("getScores")(target)

    async def getObjectiveScores(self, objective_name: str) -> Dict[str, int]:
        """Get all scores for objective."""
        return await super().__getattr__("getObjectiveScores")(objective_name)
