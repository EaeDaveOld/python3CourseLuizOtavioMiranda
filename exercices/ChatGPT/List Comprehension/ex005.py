# 5 - Crie uma lista com as letras maiúsculas de uma string.
texto = 'asDczxAdsawqrVewqeqwIasesasdaD'
print(texto)

print()

letras_maiusculas = [letra for letra in texto if letra.isupper()]
print(letras_maiusculas)
