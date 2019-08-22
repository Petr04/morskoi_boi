from player import Player
from result import Result

p1 = Player()
p2 = Player()

p1.generate()
p2.generate()

order = (p1, p2)
end = False

while True:
	for i in range(2):

		out = order[i].attack(order[1-i])

		print(out)

		if out == Result.WIN:
			winner = i
			end = True
			break

	if end:
		break

print('Победил {}'.format(('p1', 'p2')[winner]))