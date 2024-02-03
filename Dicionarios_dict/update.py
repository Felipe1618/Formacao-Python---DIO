contato = {
  "felipe@email.com": {"nome": 'Felipe', 'telefone': '9999-1122'}
}
contato.update({'felipe@email.com': {'nome': 'feh'}})
print(contato) #{'felipe@email.com': {'nome': 'feh'}}

contato.update({'carlos@email.com': {'nome': 'Carlos', 'telefone': '88888-4455'}})
print(contato)