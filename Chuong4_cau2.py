from random import randrange

while True:
    somay = randrange(1, 101)
    solandoan = 0
    win = False
    print("\nMáy đã chọn 1 số từ 1 đến 100. Bạn có 7 lần đoán!")

    while solandoan < 7:
        solandoan += 1
        songuoi = int(input(f"Lần đoán {solandoan}: "))
        if songuoi == somay:
            print("🎉 Chúc mừng bạn đoán đúng! Số máy là:", somay)
            win = True
            break
        elif songuoi < somay:
            print("Số bạn đoán nhỏ hơn số máy.")
        else:
            print("Số bạn đoán lớn hơn số máy.")

    if not win:
        print("❌ GAME OVER! Số máy là:", somay)

    hoi = input("Bạn có muốn chơi lại không? (c/k): ").lower()
    if hoi == "k":
        break

print("Cảm ơn bạn đã chơi game!")