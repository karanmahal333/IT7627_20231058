from bowling_game_for_student import BowlingGame

game = BowlingGame()
for _ in range(20):
   game.roll(0)

print("Test 1 - Gutter Game")
print("Expected: 0")
print("Actual:", game.score())
