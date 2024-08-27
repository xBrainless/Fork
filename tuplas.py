# função para acessar segundo item da tupla
# def segundo(tupla):
#     return tupla[1]

# tupla = [(558147, 951642), (712350, 244295), (573823, 26964), (405252, 787604), (718654, 867660), (531580, 78830), (973139, 710331), (892292, 646016), (422760, 694913), (154753, 539704), (887061, 324831), (438508, 667179), (237467, 295633), (489705, 725316), (328311, 644622), (591120, 994303)]
# tupla.sort(key=segundo, reverse=True)
# print(tupla)

# converter tupla em dicionario
# dicionario = dict((x, y) for x, y in tuple)
# ou
# usando dictionary comprehension
# dicionario = {tuple_1[i] : tuple_2[i] for i, _ in enumerate(tuple_2)}

# converter tupla em lista
# lista = list(tupla)
# ou
# lista = [i for i in tupla]


# EXERCICIO 1

# meta = 10000
# vendas = [
#     ('João', 15000),
#     ('Julia', 27000),
#     ('Marcus', 9900),
#     ('Maria', 3750),
#     ('Ana', 10300),
#     ('Alon', 7870),
# ]

# for nome, numeros in vendas: #podemos nomear o conteudo das tuplas
#     if numeros >= meta:
#         print('{} bateu a meta'.format(nome))

##Testando fork
