from stdlib import *

def main (lines):
    xmax = {
            "red" : 12,
            "green" : 13,
            "blue" : 14}
    poss_id = []
    for l in lines:
        if not l: continue
        ids, game = l.split(":")
        ids = int(ids.split(" ")[-1])
        app = True

        for game in game.split(";"):
            game = game.split(" ")[1:]
            vals = ints(game[::2])
            names = game[1::2]


            for n,v in zip(names,vals):
                if v > xmax[n.strip(" ,")]:
                    app = False
        if app:
            poss_id.append(ids)

    return sum(poss_id)

if __name__ == "__main__":
    lines = open("in.txt").read().splitlines()
    print(main(lines))
