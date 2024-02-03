contatos = {
  "felipe@email.com": {"nome": 'Felipe', 'telefone': '9999-1122'}
}
resultado = contatos.pop('felipe@email.com') #remove->{'nome': 'Felipe', 'telefone': '9999-1122'}
print(resultado)

resultado = contato.pop('felipe@email.com', 'nao encontrou') #{}->nao encontrou
print(resultado)