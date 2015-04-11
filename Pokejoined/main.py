result = []
def buildList(l, c):
    global result

    if len(c)==1:
        print(c[0], result)
        
    if len(c):
        last = c[-1]
        nl = [buildList([n for n in l if n!=name], c + [name]) for name in l if last[-1] == name[0]]
        if len(nl) == 0 and len(c) > len(result):
            result = c[:]
        return nl
    else:
        for name in l:
            buildList([n for n in l if n!=name], [name])
        return result

f = open('input.txt')
l = f.readline().split(' ')
f.close()

print(buildList(l, []))

# ['machamp', 'petilil', 'landorus', 'scrafty', 'yamask', 'kricketune', 'emboar', 'registeel', 'loudred', 'darmanitan', 'nosepass', 'simisear', 'relicanth', 'heatmor', 'rufflet', 'trapinch', 'haxorus', 'seaking', 'girafarig', 'gabite', 'exeggcute', 'emolga', 'audino']

