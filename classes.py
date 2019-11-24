from ball import Ball
red_ball = Ball(10, "red", 2)
blue_ball = Ball(12, "blue", 5)
print(red_ball.radius) # 10
print(red_ball.color) # red
print(red_ball.weight) # 2

print(blue_ball.radius) # 12
print(blue_ball.color) # blue
print(blue_ball.weight) # 5

from ball import Football
bears = Football(22, "brown", 13)
packers = Football(22, "green", 13)
print(bears.color)
print(bears.pressure)
bears.inflate(2)
print(bears.pressure)

from ball import PatriotsBall
patriots = PatriotsBall(22, "brown", 13)
print(patriots.pressure)
patriots.inflate(2)
print(patriots.pressure)
