from distutils.command.sdist import sdist
import numpy as np
from itertools import product
import random
import math
sudoku = []

def verification(sudoku, n):
    sudoku = np.array(sudoku).reshape((n*n,n*n))
    sudoku_transposed = np.array(sudoku)
    sudoku_transposed = sudoku_transposed.transpose()
    for i in range(n*n):
        if len(sudoku[i]) != len(set(sudoku[i])) or len(sudoku_transposed[i]) != len(set(sudoku_transposed[i])):
            return False
    for x,y in product((0,n,n*2),(0,n,n*2)):
      numeros = sudoku[y:y+n, x:x+n]
      if len(numeros.flatten()) != len(set(numeros.flatten())):
        return False
    return True



def possible(y,x,numero):
  global sudoku
  m = len(sudoku)
  n = int(math.sqrt(m))
  for i in range(m):
    try:
      if int(sudoku[y,i]) == numero:
          return False
    except:
      continue
  for i in range(m):
      try:
        if int(sudoku[i,x]) == numero:
            return False
      except:
        continue
      
  xcero = (x//n)*n
  ycero = (y//n)*n
  for i in range(0,n):
        for j in range(0,n):
              try:
                if int(sudoku[ycero+i,xcero+j]) == numero:
                      return False
              except:
                continue
  return True



#solved = False
def solver():
  global sudoku
  m = len(sudoku)
  f = len(str(m))
  s = f*"-"
  for y in range(m):
    for x in range(m):
      if sudoku[y,x] == s:
        for a in range(1,m+1):
          if possible(y,x,a):
            sudoku[y,x] = a
            solver()
            global solved
  #          if(solved == True):
     #           return sudoku
            sudoku[y,x] = "-"
        return
  #solved = True
  print(sudoku)
  


solved = False
cont = 0
def issolutionunique():
  global solved
  global cont
  global sudoku
  m = len(sudoku)
  f = len(str(m))
  for y in range(m):
    for x in range(m):
      if sudoku[y,x] == f*"-":
        for a in range(1,m+1):
          if possible(y,x,a):
            sudoku[y,x] = a
            issolutionunique()
            sudoku[y,x] = "-"
        return
  cont +=1

def generator(n):
    global sudoku
    f = len(str(n*n))
    c = f*"-"
    sudoku =  np.full((n*n,n*n),c)
    for i in range(n*n):
        a = random.randint(0,n*n-1)
        b = random.randint(0,n*n-1)
        while not (possible(a,b,i+1)):
            a = random.randint(0,n*n-1)
            b = random.randint(0,n*n-1)
        sudoku[a,b] = str(i+1)
    print(sudoku)
    #return generated
    solver()
    print(sudoku)
    toString(eraser(n))
  #solver()
  #toString(eraser(n))
  #solver()
  #toString(eraser(n))
#generator(3)

  
def eraser(n):
  global sudoku
  global cont
  sudoku1 = np.copy(sudoku)
  m = n*n
  f = len(str(m))
  c = f*"-"
  a = random.randint(0,n*n-1)
  b = random.randint(0,n*n-1)
  sudoku1[a,b] = c
  sudoku = np.copy(sudoku1)
  issolutionunique()
  while cont <= 1:
    sfinal = np.copy(sudoku1)
    a = random.randint(0,n*n-1)
    b = random.randint(0,n*n-1)
    sudoku1[a,b] = c
    sudoku = np.copy(sudoku1)
    cont = 0
    issolutionunique()
  return sfinal



def toString(sudokufinal):
  st = ""
  for i in range(len(sudokufinal)):
    for j in range(len(sudokufinal)):
      st = st + str(sudokufinal[i,j])
    print(st)
    st = ""


def main():
  global sudoku
  print("¡Bienvenido al solucionador de Sudokus! :)")
  print("----------------------------------------------")
  while True:
    print("¿Qué desea hacer?")
    print("1. Verificar si un Sudoku está bueno.")
    print("2. Solucionar un Sudoku.")
    print("3. Generar un Sudoku.")
    print("4. Salir")
    o = int(input())
    if o == 1:
      n = int(input("Especifique el tamaño de su Sudoku: "))
      m = n*n
      f = len(str(m))
      print("Ingrese su Sudoku:")
      for j in range(m):
        fila = str(input())
        chunks = [fila[i:i+f] for i in range(0, len(fila), f)]
        sudoku = sudoku + [chunks]
      sudoku = np.array(sudoku)
      if verification(sudoku,n) == True:
        print("¡Su Sudoku está bueno!")
      else: print("Su Sudoku está malo... :(")
      sudoku = []
    if o == 2:
      n = int(input("Especifique el tamaño de su Sudoku: "))
      m = n*n
      f = len(str(m))
      sud = []
      print("Ingrese su Sudoku:")
      for j in range(m):
        fila = str(input())
        chunks = [fila[i:i+f] for i in range(0, len(fila), f)]
        sud = sud + [chunks]
      sudoku = np.array(sud)
      print("¡Aquí está su solución!")
      toString(solver())
      sudoku = []
    if o == 3:
      n = int(input("Ingrese el tamaño del Sudoku que desea generar: "))
      print("¡Su Sudoku ha sido generado de manera exitosa!")
      generator(n)
      sudoku= []
    if o == 4:
      print("¡Vuelva pronto!")
    
main()

