from random import *
import numpy as np
import matplotlib.pyplot as plt

def X() -> np.ndarray:
    return np.linspace(0, 0.5, 100)

def BLOCK_TIME() -> int:
    return 600

def BLOCK_REWARD() -> float:
    return 6.25

def simulation_selfish_mining(n, q, gamma) -> (float, int):
    reward = 0
    time = 0
    i = 0
    while i < n:
        i += 1
        stop = False
        block = 0
        while not stop:
            while random() < q:  # l'attaquant mine un block
                block += 1
                time += BLOCK_TIME()
            if block >= 2:  # l'attaquant écrase la blockchain officielle
                block -= 2
                reward += 2 * BLOCK_REWARD()
            elif block == 1 and random() > q:  # l'attaquant perd
                block = 0
                if random() < gamma:  # il tente de diffuser son block aux grace a sa connectivité
                    reward += BLOCK_REWARD()
            elif block == 0:  # l'attaquant est en retard
                time += BLOCK_TIME()
            stop = block == 0
    return reward, time

def goodCycles():
    while True:
        amount = input("What is the number of attacks you will make ? ")
        try:
            val = int(amount)
            if val >= 0 and val <= 100001:
                break
            else:
                print("Amount must be between 0 and 10000, try again")
        except ValueError:
            print("Amount must be a number, try again")
    return val

def main():
    cycles = goodCycles()
    connectivity = float(20)/100
    # Practical dishonest yield
    x, y = X(), []
    for q in x:
        R, T = simulation_selfish_mining(cycles, q, connectivity)
        y.append(R / T*100)
    # Theoretical honest yield
    x1, y1 = X(), []
    for q in x:
        y1.append(q * BLOCK_REWARD() / BLOCK_TIME()*100)

    bascule = 0
    i = 0
    while bascule==0 and i<len(x):
        m = max(y[i], y1[i])
        if m == y[i]:
            bascule = m
        i += 1
    txt="For {} cycles tipping point is {}%".format(cycles, round(bascule*100, 2))
    plt.plot(x, y, label="Practical dishonest yield")
    plt.plot(x1, y1, label="Theoretical honest yield")
    plt.legend(loc='upper left')
    plt.figtext(0.35, 0.7, txt, ha="center")
    plt.xlabel('q')
    plt.ylabel('R')
    plt.title("Simulation selfish mining")
    plt.grid()
    plt.show()
main()