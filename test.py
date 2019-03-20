from bunny import bunny
import time


def simulate_step():
    time.sleep(0.3)


steps = range(1, 2000)
for step in bunny(steps):
    simulate_step()
