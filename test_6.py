from bowling_game_for_student import BowlingGame

game = BowlingGame()

# First 9 frames: all gutter (0,0)
for _ in range(18):
    game.roll(0)

# 10th frame: strike + two bonus rolls (10, 10)
game.roll(10)
game.roll(10)
game.roll(10)

print("Test 6 - Strike in Final Frame")
print("Expected: 30")
print("Actual:", game.score())
