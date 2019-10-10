'''
Exemplo:
POST data = {"question": [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}
Response = {"solution":[3 ,3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]}
Função =   solution([2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]) == [3, 3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]]
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def lambda_function(request):
    #data = {"question": [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}

    data = request.data

    result_lista = []
    dic = {}
    lista = []

    # Contabiliza os elementos
    for chave in data["question"]:
        if chave not in dic:
            dic[chave] = 1
        else:
            dic[chave] += 1
    
    # Monta a tupla para ordenar
    for chave in dic:
        lista.append((chave,dic[chave]))
    
    # Ordena a lista pela quantidade de vezes que o número aparece 
    lista.sort(key=lambda x: x[1], reverse=True)

    # Monta a lista para o resultado
    for tupla in lista:
        for count in range(tupla[1]):
            result_lista.append(tupla[0])

    #response = {"solution":[3 ,3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]}

    return Response({"solution": result_lista})
