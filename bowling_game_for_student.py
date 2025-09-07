"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""

class BowlingGame:
    """
    A class to simulate a 10-pin bowling game.

    Methods
    -------
    roll(pins):
        Records a roll in the game.
    score():
        Returns the total score of the game.
    """

    def __init__(self):
        """
        Initialize a new bowling game with 10 frames.
        Each frame has up to 2 rolls, except the 10th which may have 3.
        """
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """
        Record a roll in the game.

        Args:
            pins (int): Number of pins knocked down in this roll.
        """
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        """
        Work out the total score for the game.

        Returns:
            int: The final score after all rolls are added.
        """
        score = 0
        frame_index = 0

        for frame in range(10):
            if self._is_strike(frame_index):
                # Strike
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return score

    def _is_strike(self, frame_index):
        """
        Check if the roll at frame_index is a strike.

        Args:
            frame_index (int): The roll index to check.

        Returns:
            bool: True if strike, False otherwise.
        """
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """
        Check if the two rolls at frame_index form a spare.

        Args:
            frame_index (int): The roll index to check.

        Returns:
            bool: True if spare, False otherwise.
        """
        return frame_index + 1 < len(self.rolls) and \
               self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _strike_bonus(self, frame_index):
        """
        Calculate the bonus after a strike.

        Args:
            frame_index (int): Index of the strike roll.

        Returns:
            int: Bonus points from the next two rolls.
        """
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """
        Calculate the bonus after a spare.

        Args:
            frame_index (int): Index of the first roll of the spare.

        Returns:
            int: Bonus points from the next roll.
        """
        return self.rolls[frame_index + 2]
