input_param = input("特徴を入力してください。:")

my_dictionary = {
    "shinchou": "166.4",
    "taizyu": "75?",
    "favorite color": "red",
    "favorite musician": [
        "Mr.Children",
        "BOOWY",
        "GLAY",
        "B'z"
    ]
}

if input_param in my_dictionary:
    value = my_dictionary[input_param]
    print(value)
else:
    print("そのような特徴は登録されていません。")
