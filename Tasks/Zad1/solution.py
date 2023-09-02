# Dawid Justyna
# ALgorytm działą w ten sposób że tworze tablice F[X,Y] która sprawdz najtanszy koszt dojechania do punktu X na mapie i majac tam paliwa Y:
# zakładam ze na planete moge dojechac z maksymalnie takim bakiem jakie było maksimum baku - odległość od ostatniej planety ( za to odpowiada iteracja j)
# pozniej sprawdzam każda możlwość to znaczy jak najbardziej opłaca sie dojechac z poprzednij planety czy
# np chce na planete X dojechac z planety X-1 nie tankująć wogole na stacji X-1 czy może zatabkować jakaś częśc i za to odpowiada petla z iteracja k
# (k - ile paliwa miałem na X-1 j ile chce mieć na X tmp - odległość dlatego na X-1 musze tankować (tmp+j)-k
# Na końcu sprawdzam jescze teleportacje, i jeśli się bardziej opłaca niż najniższy obecny koszt dojechania do punktu którego prowadzi teleprotacja to nadpisuje
# koszt optymalny. Na poczatku sprawdzam warunek brzegowy czyli F[0] tam uznaje ze jeśli chce na F[0] mieć X litrów paliwa to cene biorę też z F[0] ( jest tu pewna
# nieścisłość jednak nie wpływa na rezultat bo nawet jeśli bym miał  A = B to i tak zwróciłbym F[0][0], bo jeśli mozna dojechać na jakas stacje majac X paliwa na koncu
# to mozna tez tam dojechac majac na koncu 0 paliwa i to po niższym koszcie.
# Złożoność: O(n*E^2)

def planets( D, C, T, E ):
    n = len(D)
    F = [[float('inf') for _ in range(E+1)] for _ in range(n)]
    for i in range(E+1):
        F[0][i] = C[0]*i
    if T[0][0] != 0:
        aim, cost = T[0]
        F[aim][0] = F[0][0] + cost

    for i in range(1,n):
        tmp = D[i]-D[i-1]
        for j in range(E - tmp+1):
            for k in range(E+1):
                if j - k + tmp >=0:
                    F[i][j] = min(F[i][j], F[i-1][k] + C[i-1]*(j- k+ tmp))
        if T[i][0] > i:
            aim , cost = T[i]
            F[aim][0] = min(F[i][0] +cost, F[aim][0])
    return F[-1][0]
