from bowling_game_for_student import BowlingGame

game = BowlingGame()
rolls = [3,4,2,5,1,6,4,2,8,1,7,1,5,3,2,3,4,3,2,6]
for r in rolls:
    game.roll(r)

print("Test 4 - Regular Game")
print("Expected: 72")
print("Actual:", game.score())
