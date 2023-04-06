import parse


if __name__ == "__main__":
    word = input("Введите любое название предмета для поиска в стиме: ")
    dt = parse.Parse(word)
    dt.get_req()
    info = dt.get_data()
    print(info)