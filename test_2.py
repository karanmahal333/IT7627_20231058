from bowling_game_for_student import BowlingGame

game = BowlingGame()
for _ in range(12):  # 12 strikes
    game.roll(10)

print("Test 2 - Perfect Game")
print("Expected: 300")
print("Actual:", game.score())
