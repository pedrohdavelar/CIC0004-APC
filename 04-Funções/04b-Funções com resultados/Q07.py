def calcula_distancia(x,y,xc,yc):
    dx = x - xc
    dy = y - yc
    
    if dx < 0:
        dx *= -1
    if dy < 0:
        dy *= -1
    return dx+dy