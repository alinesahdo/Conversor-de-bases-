def num_para_decimal(num, base_original = 10): # função que converte um valor de qualquer base para a decimal
    resultado = 0
    expoente = len(str(num))  # vai contar os elementos do valor dado, a partir do 0 

    if base_original == 1:
        return len(num)
    if base_original == 1: # converte da base 1 para decimal
        return len(num)
    for digito in str(num):
        if digito.isdigit(): # verifica se todos os valores são numéricos
             digito = int(digito)
             resultado += digito * (base_original **(expoente - 1)) # fórmula geral para achar o valor na base decimal
             expoente -= 1
        else:
            resultado += (ord(digito) - 55) * (base_original **(expoente - 1)) 
            # se não for numérico, converte para o número correspondente de acordo com a tabela ASCII, apenas subtraindo 55
            expoente -= 1

    return resultado

def decimal_para_qualquer(numero_decimal, base_final = 10): # função que converte da base decimal para qualquer outra base
    resultado = []
    divisao = int(numero_decimal)
    
    if base_final == 1: # converte da base decimal para base 1
        return '|' * numero_decimal
    while divisao >= 1:
        resto = divisao % base_final # dividir o numero em base decimal pela base desejada até que o quociente seja maior ou igual a 1
        if resto > 9:
            resto = chr(resto + 55)
             # se o resto for maior que 9, siginifica que não é valor numérico, então, pela tabela ASCII, converte para o valor correspondente
        divisao = divisao//base_final
        resultado += [str(resto)]
    return ''.join(resultado[::-1]) # inverte a lista e tira os elementos dela

def verifica(valor, base): # função que verifica se o valor digitado está dentro da base original
    letras = []
    if base > 10:
        num = list(range(0, 10))
        for valores in range(10, base):
            letras.append(chr(55 + valores)) # vai listar todas as letras que existem na base digitada
    else:
        num = list(range(0, base))
        for elemento in valor:
            if elemento in letras:
                continue
            elif int(elemento) in num:
                continue
            else:
                return False
        return True
            
numero = input('Insira um valor: ').upper()
baseOriginal = int((input('Insira a base desse valor: ')) or 10)
baseDestino = int((input('Insira a base de destino: ')) or 10)
num_decimal = num_para_decimal(numero,baseOriginal)


if (((baseOriginal > 36) or (baseOriginal < 1)) or ((baseDestino > 36) or (baseDestino < 1))): 
    # o usuário deve digitar apenas as bases válidas
    print('Base inválida.')
elif not verifica(numero, baseOriginal):
    print(numero)
    print(f'Erro: o valor inserido não existe na base {baseOriginal}')
elif baseDestino == 10:
    print(f'Valor na base 10: {decimal_para_qualquer(num_decimal,baseDestino)}')
else:
    print(f'Valor na base {baseDestino}: {decimal_para_qualquer(num_decimal, baseDestino)}\nValor na base 10: {num_para_decimal(numero, baseOriginal)}')

  












