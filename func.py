# -*- coding: utf-8 -*-
def func(a, b, x, y):
    return [(yk, xk) for xk in range(a, x+1) for yk in range(b, y+1)]

def print_move_pos(nx, ny):
    ret = []
    a = func(0, 0, ny, nx)
    num = 1
    for i in a:
        data = {}
        data['pos'] = i
        data['move'] = [{'pos': ()},{'pos': ()},{'pos': ()},{'pos': ()}] #上右下左
        x = i[0]
        y = i[1]
        for j in range(4):
            if j == 0:
                if (y - 1) >= 0:
                    data['move'][0]['pos'] = (x, y-1)
                    data['move'][0]['filename'] = str(num)
                    num +=1
            if j == 1:
                if (x + 1) <= nx:
                    data['move'][1]['pos'] = (x+1, y)
                    data['move'][1]['filename'] = str(num)
                    num += 1
            if j == 2:
                if (y + 1) <= ny:
                    data['move'][2]['pos'] = (x, y+1)
                    data['move'][2]['filename'] = str(num)
                    num += 1
            if j == 3:
                if (x - 1) >= 0:
                    data['move'][3]['pos'] = (x-1, y)
                    data['move'][3]['filename'] = str(num)
                    num += 1
        ret.append(data)
    return ret

def print_gif_path(x1,y1,x2,y2):
    data = print_move_pos(7,5)
    num = 1
    for i in data:
        if x1 == i['pos'][0] and y1 == i['pos'][1]:
            for j in i['move']:
                if j['pos']:
                    if j['pos'][0] == x2 and j['pos'][1] == y2:
                        return j['filename']
