anser = [25, 39, 100, 1, 5]

while True:
    print("終了するときは\"q\"を入力してください")
    s = input("当たるかな？:")

    if s == "q":
        break

    try:
        i = int(s)
    except ValueError:
        print("数字を入力するか、\"q\"を入力してください")
        continue

    if i in anser:
        print("ありました！正解です。おめでとうございます。")
    else:
        print("残念！あきらめないで。")
