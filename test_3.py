from bowling_game_for_student import BowlingGame

game = BowlingGame()
for _ in range(21):  # 21 rolls of 5 = all spares
    game.roll(5)

print("Test 3 - All Spares")
print("Expected: 150")
print("Actual:", game.score())
