def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

if __name__ == "__main__":
    notas = [7.5, 8.0, 9.5, 6.0]
    media = calcular_media(notas)
    print(f"A média é: {media}")
