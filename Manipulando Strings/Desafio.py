#Minha versão
T = input(print("Escreva seu TWITTER: \n"))
#Chat GPT: A função input() já imprime uma mensagem para o usuário, portanto, não é necessário usar print() dentro de input(). O comando print("Escreva seu TWITTER: \n") será executado antes do input(), o que não é o comportamento desejado. Você pode simplesmente usar o input() para obter a entrada do usuário.

twitter = "MUTE" if len(T) > 140  else "TWITTER"

print(twitter)

#chat GPT - versão 1
print("Chat GPT".center(50, "-"))
def verificar_tuite(texto):
    if len(texto) <= 140:
        return "TWEET"
    else:
        return "MUTE"

# Exemplo de uso:
texto = input("Digite o texto: ")
resultado = verificar_tuite(texto)
print(resultado)

#chat GPT - versão analisada, corrigida e melhorada da minha primera versão
print("Chat GPT - Versão Revisada".center(50, "-"))
T = input("Escreva seu TWITTER: ")
while len(T) > 140:
    print("Seu tweet excede o limite de 140 caracteres. Tente novamente.")
    T = input("Escreva seu TWITTER: ")

TWEET = "TWEET"
print(TWEET)
