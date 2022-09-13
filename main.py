import random

'''game logicten dewam edilecek '''

print('WELCOME TO THE TIC TAC TOE')
game_design = '1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9'
print(game_design)


class TicTacToe:
    def __init__(self):
        self.type_char = ''
        self.number = ''
        self.score_x = 0
        self.score_o = 0
        self.human = True
        self.location_list = [1,2,3,4,5,6,7,8,9];


    def game_logic(self, character, num, game_mode):
        global game_design

        updated_design = game_design.replace(f'{num}', f'{character}')
        splitted_design = updated_design.split()
        for i in splitted_design:
            if i == '|' or i == '---------':
                splitted_design.remove(i)
        if character == 'X':
            if num == 1:
                if (splitted_design[1] == 'O' and splitted_design[2] == 'X'):
                    self.score_x += 1

                if (splitted_design[3] == 'O' and splitted_design[6] == 'X'):
                    self.score_x += 1

                if (splitted_design[4] == 'O' and splitted_design[8] == 'X'):
                    self.score_x += 1


            if num == 3:
                if (splitted_design[0] == 'X' and splitted_design[1] == 'O'):
                    self.score_x += 1

                if (splitted_design[4] == 'O' and splitted_design[6] == 'X'):
                    self.score_x += 1

                if (splitted_design[5] == 'O' and splitted_design[8] == 'X'):
                    self.score_x += 1


            if num == 7:
                if (splitted_design[0] == 'X' and splitted_design[3] == 'O'):
                    self.score_x += 1

                if (splitted_design[4] == 'O' and splitted_design[2] == 'X'):
                    self.score_x += 1

                if (splitted_design[7] == 'O' and splitted_design[8] == 'X'):
                    self.score_x += 1

            if num == 9:
                if (splitted_design[0] == 'X' and splitted_design[4] == 'O'):
                    self.score_x += 1


            if num == 2:
                if (splitted_design[4] == 'O' and splitted_design[7] == 'X'):
                    self.score_x += 1

            if num == 4:
                if (splitted_design[4] == 'O' and splitted_design[5] == 'X'):
                    self.score_x += 1


            if num == 6:
                if (splitted_design[4] == 'O' and splitted_design[3] == 'X'):
                    self.score_x += 1


            if num == 8:
                if (splitted_design[4] == 'O' and splitted_design[1] == 'X'):
                    self.score_x += 1

            self.type_char = 'O'

        elif character == 'O':
            if num == 2:
                if (splitted_design[0] == 'X' and splitted_design[2] == 'X'):
                    self.score_o += 1
            if num == 4:
                if (splitted_design[0] == 'X' and splitted_design[6] == 'X'):
                    self.score_o += 1

            if num == 6:
                if (splitted_design[2] == 'X' and splitted_design[8] == 'X'):
                    self.score_o += 1
            if num == 8:
                if (splitted_design[6] == 'X' and splitted_design[8] == 'X'):
                    self.score_o += 1
            if num == 5:
                if (splitted_design[0] == 'X' and splitted_design[8] == 'X'):
                    self.score_o += 1
                if (splitted_design[2] == 'X' and splitted_design[6] == 'X'):
                    self.score_o += 1

                if (splitted_design[1] == 'X' and splitted_design[7] == 'X'):
                    self.score_o += 1

                if (splitted_design[3] == 'X' and splitted_design[5] == 'X'):
                    self.score_o += 1

            self.type_char = 'X'
        else:
            print('Yanlış karakter girdiniz.')

        if game_mode == 2:
            self.human = False

        game_design = updated_design
        print(updated_design)

    def control_design(self):
        for i in range(1, 10):
            if str(i) in game_design:
                return True

        return False

    def run(self):

        game_type = int(input('One vs One (1) or One vs Computer (2). Determine your choice: '))
        self.type_char = input('Which character do you wanna play? (X/O): ')

        while self.control_design():
            if game_type == 1 or self.human:
                self.number = int(input(f'Player "{self.type_char}" select a number,what you want to place the character: '))
                if(self.number in self.location_list):
                    self.game_logic(self.type_char, self.number, game_type)
                    self.location_list.remove(self.number)
                else:
                    print("It is already filled, Can you try again")
            elif game_type == 2:
                self.number = random.choice(self.location_list)
                self.location_list.remove(self.number)
                print(f'Computer "{self.type_char}" selected location {self.number}')
                self.game_logic(self.type_char, self.number, game_type)
                self.human = True
            else:
                print('Üzgünüz belirttiğiniz oyun modu yoktur.')

        if self.score_x > self.score_o:
            print(f'X player has {self.score_x} point, O player has {self.score_o} point. So X player won!! ')
        elif self.score_o > self.score_x:
            print(f'O player has {self.score_o} point, X player has {self.score_x} point. So O player won!! ')
        else:
            print(f'X player has {self.score_x} point, O player has {self.score_o} point. So draw!! ')

if __name__ == '__main__':
    game = TicTacToe()
    game.run()



