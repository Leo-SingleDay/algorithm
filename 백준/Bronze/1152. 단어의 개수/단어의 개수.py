string = input("")
words = string.split(" ")
words = [w for w in words if w != ""] # 공백이 아닌 경우에만 words에 넣음 # 리스트 조건제시법
print(len(words))