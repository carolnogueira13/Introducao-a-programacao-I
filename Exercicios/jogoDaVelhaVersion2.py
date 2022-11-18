
def imprime_tabuleiro():
    for i in range(3):
        print(f"{matriz[i][0]:3}|{matriz[i][1]:3}| {matriz[i][2]:3}")
        if i < 2:
            print("---*---*---")

matriz = [[" "]*3, [" "]*3, [" "]*3 ]

imprime_tabuleiro()