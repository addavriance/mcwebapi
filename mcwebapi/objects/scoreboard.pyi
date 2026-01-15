"""Type stubs for Scoreboard API module.

This module provides type hints for Scoreboard operations that correspond to
the ScoreboardApiModule.java backend methods.

Note: Scoreboard module methods don't require an identifier, as they operate
on the global server scoreboard.
"""

from typing import Any, Dict, List, Optional
from ..core.client import MinecraftClient
from ..core.promise import Promise

class Scoreboard:
    """Represents the Minecraft scoreboard system.

    Args:
        client: The MinecraftClient instance
    """

    def __init__(self, client: MinecraftClient) -> None: ...

    # ===== OBJECTIVES =====

    def createObjective(
        self, name: str, criteriaId: str, displayName: str
    ) -> Promise[bool]:
        """Create scoreboard objective.

        Args:
            name: Objective internal name
            criteriaId: Criteria type (e.g., "dummy", "health", "deathCount")
            displayName: Display name shown to players

        Returns:
            True if created successfully
        """
        ...

    def removeObjective(self, name: str) -> Promise[bool]:
        """Remove objective by name.

        Args:
            name: Objective name

        Returns:
            True if removed successfully
        """
        ...

    def getObjectives(self) -> Promise[List[Dict[str, Any]]]:
        """Get all objectives.

        Returns:
            List of objectives with keys:
                - name (str): Objective name
                - displayName (str): Display name
                - criteria (str): Criteria type
                - renderType (str): Render type ("INTEGER", "HEARTS")
        """
        ...

    def getObjective(self, name: str) -> Promise[Dict[str, Any]]:
        """Get objective by name.

        Args:
            name: Objective name

        Returns:
            Objective info or None if not found
        """
        ...

    def setDisplaySlot(self, slot: str, objectiveName: str) -> Promise[bool]:
        """Set objective to display slot.

        Args:
            slot: Display slot ("LIST", "SIDEBAR", "BELOW_NAME")
            objectiveName: Objective name or None to clear slot

        Returns:
            True if successful
        """
        ...

    def getDisplaySlots(self) -> Promise[Dict[str, Optional[str]]]:
        """Get all display slots and their objectives.

        Returns:
            Dictionary mapping slot names to objective names
        """
        ...

    # ===== TEAMS =====

    def createTeam(self, name: str) -> Promise[bool]:
        """Create team.

        Args:
            name: Team name

        Returns:
            True if created successfully
        """
        ...

    def removeTeam(self, name: str) -> Promise[bool]:
        """Remove team by name.

        Args:
            name: Team name

        Returns:
            True if removed successfully
        """
        ...

    def getTeams(self) -> Promise[List[Dict[str, Any]]]:
        """Get all teams.

        Returns:
            List of teams with keys:
                - name (str): Team name
                - displayName (str): Display name
                - color (str): Team color
                - prefix (str): Name prefix
                - suffix (str): Name suffix
                - friendlyFire (bool): Friendly fire enabled
                - seeFriendlyInvisibles (bool): See friendly invisibles
                - players (List[str]): List of player names
        """
        ...

    def getTeam(self, name: str) -> Promise[Dict[str, Any]]:
        """Get team by name.

        Args:
            name: Team name

        Returns:
            Team info or None if not found
        """
        ...

    def addPlayerToTeam(self, teamName: str, playerName: str) -> Promise[bool]:
        """Add player to team.

        Args:
            teamName: Team name
            playerName: Player name

        Returns:
            True if successful
        """
        ...

    def removePlayerFromTeam(self, playerName: str) -> Promise[bool]:
        """Remove player from their team.

        Args:
            playerName: Player name

        Returns:
            True if successful
        """
        ...

    def setTeamDisplayName(self, teamName: str, displayName: str) -> Promise[bool]:
        """Set team display name.

        Args:
            teamName: Team name
            displayName: Display name

        Returns:
            True if successful
        """
        ...

    def setTeamColor(self, teamName: str, colorName: str) -> Promise[bool]:
        """Set team color.

        Args:
            teamName: Team name
            colorName: Color name (e.g., "RED", "BLUE", "GREEN", "GOLD")

        Returns:
            True if successful
        """
        ...

    def setTeamPrefix(self, teamName: str, prefix: str) -> Promise[bool]:
        """Set team name prefix.

        Args:
            teamName: Team name
            prefix: Prefix text

        Returns:
            True if successful
        """
        ...

    def setTeamSuffix(self, teamName: str, suffix: str) -> Promise[bool]:
        """Set team name suffix.

        Args:
            teamName: Team name
            suffix: Suffix text

        Returns:
            True if successful
        """
        ...

    def setTeamFriendlyFire(self, teamName: str, enabled: bool) -> Promise[bool]:
        """Set team friendly fire.

        Args:
            teamName: Team name
            enabled: Whether friendly fire is enabled

        Returns:
            True if successful
        """
        ...

    def setTeamSeeFriendlyInvisibles(self, teamName: str, enabled: bool) -> Promise[bool]:
        """Set whether team members can see friendly invisibles.

        Args:
            teamName: Team name
            enabled: Whether to see friendly invisibles

        Returns:
            True if successful
        """
        ...

    # ===== SCORES =====

    def getScore(self, objectiveName: str, target: str) -> Promise[Optional[int]]:
        """Get score for target in objective.

        Args:
            objectiveName: Objective name
            target: Target name (player, entity, or fake player)

        Returns:
            Score value or None if not found
        """
        ...

    def setScore(self, objectiveName: str, target: str, value: int) -> Promise[bool]:
        """Set score for target in objective.

        Args:
            objectiveName: Objective name
            target: Target name
            value: Score value

        Returns:
            True if successful
        """
        ...

    def addScore(self, objectiveName: str, target: str, value: int) -> Promise[bool]:
        """Add to score for target in objective.

        Args:
            objectiveName: Objective name
            target: Target name
            value: Value to add (can be negative)

        Returns:
            True if successful
        """
        ...

    def resetScore(self, objectiveName: str, target: str) -> Promise[bool]:
        """Reset score for target in objective.

        Args:
            objectiveName: Objective name
            target: Target name

        Returns:
            True if successful
        """
        ...

    def resetAllScores(self, target: str) -> Promise[bool]:
        """Reset all scores for target across all objectives.

        Args:
            target: Target name

        Returns:
            True if successful
        """
        ...

    def getScores(self, target: str) -> Promise[Dict[str, int]]:
        """Get all scores for target.

        Args:
            target: Target name

        Returns:
            Dictionary mapping objective names to score values
        """
        ...

    def getObjectiveScores(self, objectiveName: str) -> Promise[Dict[str, int]]:
        """Get all scores in objective.

        Args:
            objectiveName: Objective name

        Returns:
            Dictionary mapping target names to score values
        """
        ...
