def std_weight(height, gender):
    height *= 0.01
    if gender == "남자":
        weight = round((height ** 2) * 22,2)
    elif gender == "여자":
        weight = round((height ** 2) * 21, 2)
    return f"키 {height*100}cm {gender}의 표준 체중은 {weight}kg입니다."

print(std_weight(175, "남자"))