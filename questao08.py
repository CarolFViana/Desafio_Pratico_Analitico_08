# 8. Um sistema precisa verificar se uma senha atende a uma regra básica de
# segurança. Crie uma função que receba uma senha e retorne:
#  True se a senha possuir pelo menos 8 caracteres;
#  False caso contrário.
# Desafio: modifique a função para exigir também que a senha contenha pelo menos
# um número.

def verificar_senha(senha):
    tem_tamanho = len(senha) >= 8
    tem_numero = any(caractere.isdigit() for caractere in senha)

    return tem_tamanho and tem_numero


senha = input("Digite uma senha: ")

if verificar_senha(senha):
    print("Senha válida")
else:
    print("Senha inválida")