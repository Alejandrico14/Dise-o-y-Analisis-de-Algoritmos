texto = open('quijote.txt',  'r'  ,  encoding="utf8")

print("Coincidencias de El quijote de algúnas palabras owo")

A = texto.read()
resultados = []
def string_match_brute(A,P):
    count = 0
    for i in range(len(A) - len(P) + 1):
        for j in range(len(P)):
            if P[j] == A[i+j]:
                pass
            else:
                break
        if j+1 == len(P) and A[i+j] == P[j]:
            count = count + 1
            resultados.append(i)

    print(f" {P} tuvimos alrededor de {count} coincidencias y se encuentran en... {resultados}")
    resultados.clear()

#Se va a trabajar con ... Hidalfo, molino, merced (sé que es hidalgo, pero no está demás buscarlo mal e.e)

patron = ["molino", "hidalgo", "merced"]
for i in patron:
    string_match_brute(A,i)

