def  binariodec(binario1):
  decimal = 0
  for i in binario1:
    decimal = decimal * 2 + int(i)
  return decimal

Nbinario = int(input("Digite um numero binario a ser convertido em decimal: ")
resultado = binariodec(Nbinario)
print(f"O valor decimal de {Nbinario} é {resultado})
