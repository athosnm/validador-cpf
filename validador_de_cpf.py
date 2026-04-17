while True:
    cpf = input('Digite o CPF para validação: ')
    cpf = cpf.replace('.', '').replace('-', '')

    if not cpf.isdigit() or len(cpf) != 11:
        print('CPF inválido! Digite apenas números com 11 dígitos.')
    else:
        nove_digitos = cpf[:9]
        contador_regressivo = 10
        resultado_dg1 = 0
        digito1 = 0
        
        for digito in nove_digitos:
            resultado_dg1 += int(digito) * contador_regressivo
            contador_regressivo -= 1
            
        digito1 = (resultado_dg1 * 10) % 11
        digito1 = digito1 if digito1 <= 9 else 0

        resultado_dg2 = 0
        contador_regressivo = 11

        for digito in nove_digitos:
            resultado_dg2 += int(digito) * contador_regressivo
            contador_regressivo -= 1
            
        resultado_dg2 = resultado_dg2 + (digito1 * 2)
        digito2 = (resultado_dg2 * 10) % 11
        digito2 = digito2 if digito2 <= 9 else 0

        valido = nove_digitos + str(digito1) + str(digito2)

        if valido == cpf:
            print('CPF válido!')
        else:
            print('CPF inválido!')









    
        
    

    
    
    