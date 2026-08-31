def tower_builder(n):
    tower = []
    for i in range(n):
        tower.append((n-i-1) * " " + ((i * 2)+1) * "*" + (n-i-1) * " ")
    
    return tower