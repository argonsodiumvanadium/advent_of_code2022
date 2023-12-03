from stdlib import *

def main (lines):
    poss_id = []
    for l in lines:
        if not l: continue
        ids, game = l.split(":")
        ids = int(ids.split(" ")[-1])
        app = True

        xmax = {"red" : -1, "green" : -1, "blue" : -1}
        for game in game.split(";"):
            game = game.split(" ")[1:]
            vals = ints(game[::2])
            names = game[1::2]


            for n,v in zip(names,vals):
                key = n.strip(" ,")
                xmax[key] = v if xmax[key] < v else xmax[key]
        poss_id.append(xmax["red"]*xmax["green"]*xmax["blue"])

    return sum(poss_id)

if __name__ == "__main__":
    lines = open("in.txt").read().splitlines()
    print(main(lines))
