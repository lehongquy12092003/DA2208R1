import random # phải “nhập khẩu” chương trình random trước
the_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: ")) # bạn đoán mò 1 số từ 1 đến 10
while guess != the_number: # trong khi số bạn cho còn khác với số của máy cho thì cứ tiếp tục vòng lặp while
    if guess > the_number:
        print(guess, "was too high. Try again.") # không phải, số bạn cho lớn quá
    if guess < the_number:
        print(guess, "was too low. Try again.") # không phải, số bạn cho thấp quá
    guess = int(input("Guess again: ")) # Đóan lại đi !
print(guess, "was the number! You win!") # Đúng rồi bạn thắng
