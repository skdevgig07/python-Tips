class Oi:
  
p = Oi()

[x for x in vars(Oi).items() if '_' not in x[0]]

[x for x in vars(p).items()]
