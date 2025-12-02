from question import moves
moves = moves.splitlines()
position = 50
star1 = 0
star2 = 0
# Since 0-99 keeps looping and the total elements are 100, current position + steps % 100 will give the next position.
# You can calculate how many times you pass 0 by checking how many times you cross the (100 - current position) and current position for R and L respectively.
for i in moves:
    steps = int(i[1:])
    if i[0] == "R":
        f0 = (100 - position) % 100
        if f0 == 0:
            f0 = 100
        passes = 1 + (steps - f0)//100 if f0 <= steps else 0
        position = (position + steps) % 100
    if i[0] == "L":
        f0 = position % 100
        if f0 == 0:
            f0 = 100
        passes = 1 + (steps - f0)//100 if f0 <= steps else 0
        position = (position - steps) % 100
    star2 += passes
    if position == 0:
        star1 += 1
print(star1, star2)