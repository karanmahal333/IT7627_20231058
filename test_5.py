from bowling_game_for_student import BowlingGame

game = BowlingGame()

# First 9 frames: all gutter (0,0)
for _ in range(18):
    game.roll(0)

# 10th frame: spare (9,1) and a bonus roll of 5
game.roll(9)
game.roll(1)
game.roll(5)

print("Test 5 - Spare in Final Frame")
print("Expected: 15")
print("Actual:", game.score())
