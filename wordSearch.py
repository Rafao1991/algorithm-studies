class MySolution:
    board = None
    board_size_x = None
    board_size_y = None
    
    def wordSearch(self, board, word):
        # validate word
        if len(word) == 0:
            return False
        
        # validate board
        if board and len(board) > 0 and len(board[0]) > 0:
            self.board = board
            self.board_size_x = len(self.board)
            self.board_size_y = len(self.board[0])
        
        # navigate through the board
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # is word first position?
                if self.board[x][y] == word[0]:
                    # set current position
                    current_pos = (x, y)
                    # star the magic to find the whole word in the board
                    if self.deep_first_search(current_pos, [current_pos], word, 0):
                        return True
        return False
    
    def deep_first_search(self, current_pos, visited_paths, word, word_index):
        # reach final position?
        if word_index == len(word) - 1:
            return True
        
        # get current x and y
        x, y = current_pos
        
        # set possible moves
        moves = [
            (x+1,y),
            (x, y+1),
            (x-1, y),
            (x, y-1)
        ]
        
        # set new index to validate
        new_index = word_index + 1
        
        # navigate through possible moves
        for move_x, move_y in moves:
            # is this move valid?
            if move_x >= 0 and move_x < self.board_size_x and move_y >= 0 and move_y < self.board_size_y:
                # is this char expected?
                if word[new_index] == self.board[move_x][move_y]:
                    # set the new valid move
                    new_move = (move_x, move_y)
                    # validate if the move was not visited before
                    if new_move not in visited_paths:
                        # call recursive to the new move
                        # adding the new move to visited positions
                        # and setting the new index as the current one
                        if self.deep_first_search(new_move, visited_paths + [new_move], word, new_index):
                            return True
        return False
    
test_board = [
    ['A','B','C','E'],  
    ['S','F','C','S'],    
    ['A','D','E','E']
]
mySolution = MySolution()
print('Given "ABCCED" return true -> ' + str(mySolution.wordSearch(test_board, 'ABCCED')))
print('Given "SEE" return true -> ' + str(mySolution.wordSearch(test_board, 'SEE')))
print('Given "ABCB" return false -> ' + str(mySolution.wordSearch(test_board, 'ABCB')))
print('Given "" return false -> ' + str(mySolution.wordSearch(test_board, '')))
print('Given "ABCESCFSADEE" return true -> ' + str(mySolution.wordSearch(test_board, 'ABCESCFSADEE')))