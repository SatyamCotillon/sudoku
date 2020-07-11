import math


def ens_vide(n):
  s = []
  for i in range(n):
    s.append(0)
    
  return s


def recherche(g, l, m):
  cpt = 0
  res = -1
  ok = False
  n = len(g)
  while cpt < n and not ok:
    if g[l][cpt] == m:
      res = cpt
      ok = True
    cpt += 1
    
  return res


def ens_vide2(n):
  s = []
  for i in range(n):
    s.append(False)
    
  return s


def grille_pleine(g):
  rep = True
  n = len(g)
  for i in range(n):
    for j in range(n):
      if g[i][j] == 0:
        rep = False
    
  return rep


def val_possible(g):
  n = len(g)
  t = []
  v = []
  for i in range(n):
    v.append(ens_vide(n))
  for l in range(n):
    for c in range(n):
      t = ens_vide(n)
      if g[l][c] == 0:
        for lt in range(n):
          ct = c
          if g[lt][ct] != 0:
            t[g[lt][ct] - 1] = 1
        for ct in range(n):
          lt = l
          if g[lt][ct] != 0:
            t[g[lt][ct] - 1] = 1
        for ltb in range(int(l / math.sqrt(n)) * int(math.sqrt(n)), int(l / math.sqrt(n)) * int(math.sqrt(n)) + int(math.sqrt(n)) - 1):
          for ctb in range(int(c / math.sqrt(n)) * int(math.sqrt(n)), int(c / math.sqrt(n)) * int(math.sqrt(n)) + int(math.sqrt(n)) - 1):
            if g[ltb][ctb] != 0:
              t[g[ltb][ctb] - 1] = 1
        for a in range(n):
          if t[a] == 0:
            t[a] = 1
          else:
            t[a] = 0
      v[l][c] = t
    
  return v


def somme_val_possible(g):
  n = len(g)
  a = val_possible(g)
  rep = []
  for b in range(n):
    rep.append(ens_vide(n))
  for cpt1 in range(n):
    for cpt2 in range(n):
      for cpt3 in range(n):
        rep[cpt1][cpt2] += a[cpt1][cpt2][cpt3]
  
  return rep


def recherche2(g, l, c, ar):
  i = 0
  ok = False
  rep = -1
  n = len(g)
  while not ok and i < n:
    if g[l][c][i] == ar:
      rep = i
      ok = True
    i += 1
    
  return rep


def affecte_val_possible(g):
  n = len(g)
  ok1 = False
  while not ok1:
    a = val_possible(g)
    b = somme_val_possible(g)
    l = 0
    cpt = False
    while l < n:
      c = recherche(b, l, 1)
      if c != - 1:
        cpt = True
        d = recherche2(a, l, c, 1)
        g[l][c] = d + 1
      l += 1
    if cpt == False:
      ok1 = True
  for l in range(n):
    for c in range(n):
      a = val_possible(g)
      d = recherche2(a, l, c, 1)
      if d != -1:
        g[l][c] = d + 1

  return g


def lok(g, l):
  n = len(g)
  s = ens_vide2(n)
  c = 0
  ok = True
  while ok == True and c < n:
    if g[l][c] != 0:
      if s[g[l][c] - 1] == True:
        ok = False
      else:
        s[g[l][c] - 1] = True
    c += 1
    
  return ok


def cok(g, c):
  n = len(g)
  s = ens_vide2(n)
  l = 0
  ok = True
  while ok == True and l <= n - 1:
    if g[l][c] != 0:
      if s[g[l][c] - 1] == True:
        ok = False
      else:
        s[g[l][c] - 1] = True
    l += 1
    
  return ok


def bok(g, mdl, mdc):
  n = len(g)
  s = ens_vide2(n)
  ok = True
  l = mdl
  while ok == True and l < mdl + int(math.sqrt(n)):
    c = mdc
    while ok == True and c < mdc + int(math.sqrt(n)):
      if g[l][c] != 0:
        if s[g[l][c] - 1] == True:
          ok = False
        else:
          s[g[l][c] - 1] = True
      c += 1
    l += 1
    
  return ok


def gok(g):
  n = len(g)
  ok = True
  l = 0
  c = 0
  while ok and l < n:
    ok = lok(g, l)
    l += 1
  while ok and c < n:
    ok = cok(g, c)
    c += 1
  l = 0
  while ok and l < n:
    c = 0
    while ok and c < n:
      ok = bok(g, l ,c)
      c += int(math.sqrt(n))
    l += int(math.sqrt(n))
    
  return ok


def recherche_non_valideL(g, l):
  n = len(g)
  r = ens_vide(n)
  for c in range(n):
    if g[l][c] != 0:
      r[g[l][c] - 1] += 1
    
  return r


def recherche_non_valideC(g, c):
  n = len(g)
  r = ens_vide(n)
  for l in range(n):
    if g[l][c] != 0:
      r[g[l][c] - 1] += 1
    
  return r


def recherche_non_valideB(g, mdl, mdc):
  n = len(g)
  r = ens_vide(n)
  for l in range(mdl, int(mdl + math.sqrt(n))):
    for c in range(mdc, int(mdc + math.sqrt(n))):
      if g[l][c] != 0:
        r[g[l][c] - 1] += 1
    
  return r


def supprime_ligne(g, l, a):
  n = len(g)
  for c in range(n):
    if g[l][c] == a:
      g[l][c] = 0
    
  return g


def supprime_colonne(g, c, a):
  n = len(g)
  for l in range(n):
    if g[l][c] == a:
      g[l][c] = 0
    
  return g


def supprime_bloc(g, mdl, mdc, a):
  n = len(g)
  for l in range(mdl, mdl + int(math.sqrt(n))):
    for c in range(mdc, mdc + int(math.sqrt(n))):
      if g[l][c] == a:
        g[l][c] = 0
    
  return g


def retire_val_non_valide(g):
  n = len(g)
  for l in range(n):
    r = recherche_non_valideL(g, l)
    for pr in range(n):
      if r[pr] > 1:
        g = supprime_ligne(g, l, pr + 1)
  for c in range(n):
    r = recherche_non_valideC(g, c)
    for pr in range(n):
      if r[pr] > 1:
        g = supprime_colonne(g, c, pr + 1)
  for l in range(0, n, int(math.sqrt(n))):
    for c in range(0, n, int(math.sqrt(n))):
      r = recherche_non_valideB(g, l, c)
      for pr in range(n):
        if r[pr] > 1:
          g = supprime_bloc(g, l, c, pr + 1)
    
  return g


def remplir_sudoku(g):
  go = gok(g)
  gp = grille_pleine(g)
  while not go or not gp:
    g = affecte_val_possible(g)
    go = gok(g)
    gp = grille_pleine(g)
    if not go:
      g = retire_val_non_valide(g)
  
  return g


def grille_pleine2(g):
  rep = True
  n = len(g)
  for i in range(n):
    for j in range(n):
      if g[i][j] == -1:
        rep = False
  
  return rep


def ens_vide3(n):
  s = []
  for i in range(n):
    s.append(-1)
  
  return s


def remplir_grille():
  rep1 = False
  g = []
  nbl = int(input("combien de lignes y a t'il dans votre grille ?\n"))
  nbc = int(input("combien de collones y a t'il dans votre grille ?\n"))
  if nbl != nbc:
    return rep1
  else:
    for i in range(nbl):
      g.append(ens_vide3(nbl))
    gp = False
    while not gp:
      ok1 = False
      cpt = 0
      while not ok1 and cpt < nbl:
        a = recherche(g, cpt, -1)
        if a != -1:
          ok1 = True
          g[cpt][a] = " X"
        cpt += 1
      form = ""
      for i in range(nbl):
        form += "{" + str(i) + ":3}"
      for i in g:
        print(form.format(*i))
      case = int(input("quelle est la valeur de la case avec une croix ?\n"))
      g[cpt-1][a] = case
      gp = grille_pleine2(g)
  
  return g


def sudoku():
  g = False
  while g == False:
    g = remplir_grille()
  g = remplir_sudoku(g)
  n = len(g)
  form = ""
  for i in range(n):
    form += "{" + str(i) + ":3}"
  for i in g:
    print(form.format(*i))
  
  return g


print(sudoku())

