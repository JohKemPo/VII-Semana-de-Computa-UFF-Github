def main():
    #teste
    contats = []
    while 1:
        menu = int(input("1 para adicionar contatos \n 2 para buscar entre seus contatos \n 3 para deletar um contatos \n 4 para mostrar sua lista de contatos\n"))
        if menu == 1:
            contats = addcont(contats)
            print("sua nova lista de contatos ", contats)
        elif menu ==2:
            busccont(contats)
        elif menu == 3:
            contdeletado, cas = delcont(contats)
            del contats[contdeletado - 1]
            print(f'contatos de numero {contdeletado} deletado, o numero era {cas}')
            print(f'sua nova lista de contatos \n {contats}')
        elif menu == 4:
            print('sua lista de contatos e', contats)
        else:
            exit()
def busccont(contatos):
    print('sua lista atual de contatos \n', contatos)
    busca = input()
    print('Contato de numero', contatos.index(busca) + 1)
    
def delcont(contatos):
    print('sua lista atual de contatos \n', contatos)
    deletado = input()
    return contatos.index(deletado) + 1, contatos[contatos.index(deletado)]
def addcont(contatos):
    contatos.append(input('insira um contato para adicionar'))
    if input('quer adicionar mais algum contato? \n S para sim\n').upper() == 'S':
        addcont(contatos)
    return contatos
main()    
