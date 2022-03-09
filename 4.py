if __name__ == "__main__":
    path = input("Enter a path to file: ")
    with open(path, "r", encoding="utf-8") as f:
        a = f.readlines()

    list_to_delete = []
    for i in a:
        if i.startswith("#"):
            list_to_delete.append(i)

    for i in list_to_delete:
        a.remove(i)

    with open("file.py", "w", encoding="utf-8") as f:
        for i in a:
            f.write(i)