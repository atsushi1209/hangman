def string_float(string):
    return float(string)

try:
    print(string_float("test"))    
except ValueError:
        print("数値を入力してください")
        
