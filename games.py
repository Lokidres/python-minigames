import random
import time
import os
import sys
import string

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main_menu():
    while True:
        clear_screen()
        print_slow("╔══════════════════════════╗")
        print_slow("║       Mini Oyunlar       ║")
        print_slow("╠══════════════════════════╣")
        print_slow("║ 1. Rus Ruleti            ║")
        print_slow("║ 2. Taş Kağıt Makas       ║")
        print_slow("║ 3. Sayı Tahmin           ║")
        print_slow("║ 4. Adam Asmaca           ║")
        print_slow("║ 5. Zar Oyunu             ║")
        print_slow("║ 6. Kelime Bulmaca        ║")
        print_slow("║ 7. XOX                   ║")
        print_slow("║ 8. Çıkış                 ║")
        print_slow("╚══════════════════════════╝")
        
        try:
            choice = input("\nSeçiminiz (1-8): ")
            if choice == "1":
                russian_roulette()
            elif choice == "2":
                rock_paper_scissors()
            elif choice == "3":
                number_guess()
            elif choice == "4":
                hangman()
            elif choice == "5":
                dice_game()
            elif choice == "6":
                word_puzzle()
            elif choice == "7":
                tic_tac_toe()
            elif choice == "8":
                print_slow("Oyundan çıkılıyor...")
                sys.exit()
            else:
                print_slow("Geçersiz seçim! Tekrar deneyin.")
                time.sleep(1)
        except Exception as e:
            print_slow(f"Bir hata oluştu: {e}")
            time.sleep(1)

def russian_roulette():
    clear_screen()
    print_slow("═══ Rus Ruleti ═══")
    print_slow("Şarjörde 6 yuva var ve bir mermi...")
    bullet_position = random.randint(1, 6)
    current_position = 1
    
    while True:
        print_slow(f"\nŞarjör Pozisyonu: {current_position}/6")
        print_slow("\nTetiği çekmek için ENTER'a basın (q ile çıkış)")
        
        choice = input().lower()
        if choice == 'q':
            break
        
        print_slow("*click*", 0.3)
        time.sleep(0.5)
        
        if current_position == bullet_position:
            print_slow("\n💥 BANG! Öldün! 💀", 0.1)
            time.sleep(2)
            break
        else:
            print_slow("\nŞanslısın, hayattasın! 😅")
            current_position += 1
            if current_position > 6:
                current_position = 1

def rock_paper_scissors():
    choices = ["taş", "kağıt", "makas"]
    scores = {"oyuncu": 0, "bilgisayar": 0}
    clear_screen()
    print_slow("═══ Taş Kağıt Makas ═══")
    
    while True:
        print_slow(f"\nSkor - Siz: {scores['oyuncu']} Bilgisayar: {scores['bilgisayar']}")
        print_slow("\nSeçenekler: taş, kağıt, makas (q ile çıkış)")
        player_choice = input("\nSeçiminiz: ").lower()
        
        if player_choice == 'q':
            break
            
        if player_choice not in choices:
            print_slow("Geçersiz seçim!")
            continue
            
        computer_choice = random.choice(choices)
        print_slow(f"\nSizin seçiminiz: {player_choice}")
        print_slow(f"Bilgisayarın seçimi: {computer_choice}")
        
        if player_choice == computer_choice:
            print_slow("\nBerabere! 🤝")
        elif ((player_choice == "taş" and computer_choice == "makas") or
              (player_choice == "kağıt" and computer_choice == "taş") or
              (player_choice == "makas" and computer_choice == "kağıt")):
            print_slow("\nKazandınız! 🎉")
            scores["oyuncu"] += 1
        else:
            print_slow("\nKaybettiniz! 😢")
            scores["bilgisayar"] += 1
        
        time.sleep(1)

def number_guess():
    clear_screen()
    print_slow("═══ Sayı Tahmin Oyunu ═══")
    print_slow("1-100 arası bir sayı tuttum...")
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            print_slow(f"\nKalan hakkınız: {max_attempts - attempts}")
            guess = input("\nTahmininiz (q ile çıkış): ")
            if guess.lower() == 'q':
                break
                
            guess = int(guess)
            attempts += 1
            
            if guess < 1 or guess > 100:
                print_slow("1-100 arası bir sayı girin!")
                continue
                
            if guess == target:
                print_slow(f"\nTebrikler! {attempts} denemede buldunuz! 🎉")
                time.sleep(2)
                break
            elif guess < target:
                print_slow("Daha yüksek bir sayı deneyin! ⬆️")
            else:
                print_slow("Daha düşük bir sayı deneyin! ⬇️")
                
        except ValueError:
            print_slow("Geçerli bir sayı girin!")
    else:
        print_slow(f"\nHakkınız bitti! Sayı {target} idi. 😢")
        time.sleep(2)

def hangman():
    words = ["python", "programlama", "bilgisayar", "yazılım", "geliştirici", 
             "internet", "algoritma", "veritabanı", "terminal", "oyun"]
    clear_screen()
    print_slow("═══ Adam Asmaca ═══")
    
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6
    
    hangman_pics = ['''
      +---+
          |
          |
          |
         ===''', '''
      +---+
      O   |
          |
          |
         ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\  |
     / \  |
         ===''']
    
    while wrong_guesses < max_wrong:
        clear_screen()
        print(hangman_pics[wrong_guesses])
        
        word_display = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print_slow(f"\nKelime: {word_display}")
        print_slow(f"Tahmin edilen harfler: {', '.join(sorted(guessed_letters))}")
        
        if '_' not in word_display:
            print_slow("\nTebrikler! Kelimeyi buldunuz! 🎉")
            time.sleep(2)
            break
            
        guess = input("\nBir harf tahmin edin (q ile çıkış): ").lower()
        
        if guess == 'q':
            break
            
        if len(guess) != 1 or not guess.isalpha():
            print_slow("Lütfen tek bir harf girin!")
            continue
            
        if guess in guessed_letters:
            print_slow("Bu harfi zaten tahmin ettiniz!")
            continue
            
        guessed_letters.add(guess)
        
        if guess not in word:
            wrong_guesses += 1
            print_slow("Yanlış tahmin! ❌")
            if wrong_guesses == max_wrong:
                clear_screen()
                print(hangman_pics[wrong_guesses])
                print_slow(f"\nKaybettiniz! Kelime '{word}' idi. 😢")
                time.sleep(2)
        else:
            print_slow("Doğru tahmin! ✅")
        
        time.sleep(1)

def dice_game():
    clear_screen()
    print_slow("═══ Zar Oyunu ═══")
    print_slow("En yüksek puanı toplamaya çalışın!")
    
    player_score = 0
    computer_score = 0
    target_score = 50
    
    while True:
        print_slow(f"\nSkor - Siz: {player_score} Bilgisayar: {computer_score}")
        choice = input("\nZar atmak için ENTER (q ile çıkış): ")
        
        if choice.lower() == 'q':
            break
            
        player_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        
        print_slow(f"\nSizin zarınız: {player_roll} 🎲")
        time.sleep(0.5)
        print_slow(f"Bilgisayarın zarı: {computer_roll} 🎲")
        
        player_score += player_roll
        computer_score += computer_roll
        
        if player_score >= target_score or computer_score >= target_score:
            print_slow("\n=== Oyun Bitti! ===")
            if player_score > computer_score:
                print_slow("\nTebrikler! Kazandınız! 🎉")
            elif computer_score > player_score:
                print_slow("\nBilgisayar kazandı! 😢")
            else:
                print_slow("\nBerabere! 🤝")
            time.sleep(2)
            break
        
        time.sleep(1)

def word_puzzle():
    words = ["python", "java", "javascript", "html", "css", "ruby", "php", "swift", "kotlin", "rust"]
    clear_screen()
    print_slow("═══ Kelime Bulmaca ═══")
    
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    attempts = 0
    max_attempts = 5
    
    print_slow(f"\nKarışık harfler: {scrambled}")
    
    while attempts < max_attempts:
        print_slow(f"\nKalan hakkınız: {max_attempts - attempts}")
        guess = input("\nKelimeyi tahmin edin (q ile çıkış): ").lower()
        
        if guess == 'q':
            break
            
        attempts += 1
        
        if guess == word:
            print_slow("\nTebrikler! Doğru tahmin! 🎉")
            time.sleep(2)
            break
        else:
            print_slow("Yanlış tahmin! ❌")
            if attempts == max_attempts:
                print_slow(f"\nHakkınız bitti! Kelime '{word}' idi. 😢")
                time.sleep(2)

def tic_tac_toe():
    def print_board(board):
        clear_screen()
        print_slow("═══ XOX Oyunu ═══")
        print("\n")
        for i in range(3):
            print(f" {board[i*3]} │ {board[i*3+1]} │ {board[i*3+2]} ")
            if i < 2:
                print("───┼───┼───")
    
    def check_winner(board):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Yatay
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Dikey
            [0, 4, 8], [2, 4, 6]  # Çapraz
        ]
        
        for combo in win_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
                return board[combo[0]]
        return None
    
    board = [" "] * 9
    player = "X"
    computer = "O"
    
    while True:
        print_board(board)
        
        if " " not in board:
            print_slow("\nBerabere! 🤝")
            time.sleep(2)
            break
            
        if player == "X":
            try:
                move = int(input("\nHamleni gir (1-9, q ile çıkış): "))
                if move == "q":
                    break
                move -= 1
                
                if move < 0 or move > 8:
                    print_slow("Geçersiz hamle! 1-9 arası bir sayı girin.")
                    continue
                    
                if board[move] != " ":
                    print_slow("Bu kare dolu! Başka bir kare seçin.")
                    continue
                    
                board[move] = player
            except ValueError:
                print_slow("Geçersiz giriş!")
                continue
        else:
            available_moves = [i for i, x in enumerate(board) if x == " "]
            move = random.choice(available_moves)
            board[move] = computer
            print_slow("\nBilgisayar hamlesini yapıyor...")
            time.sleep(1)
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == player:
                print_slow("\nTebrikler! Kazandınız! 🎉")
            else:
                print_slow("\nBilgisayar kazandı! 😢")
            time.sleep(2)
            break
            
        player, computer = computer, player

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print_slow("\nOyundan çıkılıyor...")
        sys.exit()