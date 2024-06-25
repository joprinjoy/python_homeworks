import unittest
from hangman import guess,start,game_room,select_word,word_mask,show_the_progress,hangman,show_hangman,retry
from unittest.mock import patch

class TestStart(unittest.TestCase):
    @patch('hangman.game_room',return_value = None)
    @patch('hangman.input',return_value = 'start')
    def test_start_start(self,mock_input,mock_game_room):
        result = start()
        self.assertEqual(result, True)

    @patch('hangman.input',return_value = 'no')
    def test_start_else(self,mock_input):
        result = start()
        self.assertEqual(result, False)

    @patch('hangman.input',return_value = '')
    def test_start_blank(self,mock_input):
        result = start()
        self.assertEqual(result, False)



class TestGameRoom(unittest.TestCase):

    #mocking all the functions with some values
    @patch('hangman.filtered_words_from_file',return_value = ['hello','testes'])
    @patch('hangman.select_word',return_value = 'hello')
    @patch('hangman.sleep',return_value = None  )
    @patch('hangman.guess',return_value = True)
    @patch('hangman.retry')
    def test_game_room_true(self,mock_sleep,mock_select_word,mock_filtered_word_from_file,mock_guess,mock_retry):
        # used to get the printed statements as argument 
        with patch('builtins.print') as mock_print:
            game_room()
             
        #checking whether the check string present in the argument
        self.assertIn('Congratulations',mock_print.call_args.args[0])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        mock_retry.assert_called_once() 
    
    @patch('hangman.filtered_words_from_file',return_value = ['hello','testes'])
    @patch('hangman.select_word',return_value = 'hello')
    @patch('hangman.sleep',return_value = None  )
    @patch('hangman.guess',return_value = False)
    @patch('hangman.retry')
    def test_game_room_false(self,mock_filtered_words_from_file,mock_select_word,mock_sleep,mock_guess,mock_retry):
        with patch('builtins.print') as mock_print:
            game_room()

        self.assertIn('killed',mock_print.call_args.args[0])   
        mock_retry.assert_called_once()                                                                                                                                                                                                                                                                                                                                                                   


    @patch('hangman.filtered_words_from_file',return_value = ['hello','testes'])
    @patch('hangman.select_word',return_value = 'hello')
    @patch('hangman.sleep',return_value = None  )
    @patch('hangman.guess',return_value = '')
    @patch('hangman.retry')
    @patch('hangman.game_room')
    def test_game_room_false(self,mock_filtered_words_from_file,mock_select_word,mock_sleep,mock_guess,mock_retry,mock_game_room):
        game_room()
        #make sure game_roo function is called when receiving any other value than true or false
        mock_game_room.assert_called_once()

class TestWordMask(unittest.TestCase):
    def test_word_mask_first(self):
        word_from_file = 'hello'
        expected_output = {1:'-',2:'-',3:'-',4:'-',5:'-'}
        result =word_mask(word_from_file)
        self.assertEqual(result, expected_output)

    def test_word_mask_second(self):
        word_from_file = 'tested'
        expected_output = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-'}
        result =word_mask(word_from_file)
        self.assertEqual(result, expected_output)

    
        


    
class TestSelectword(unittest.TestCase):
    
    @patch('hangman.random.choice') 
    def test_select_word(self,mock_random_choice):
        filtered_words = ['hii','hey','hello','test','super','honeybee','brocode']
        mock_random_choice.return_value = 'hello'      
        result = select_word(filtered_words)
        self.assertEqual(result, 'hello')

    @patch('hangman.random.choice') 
    def test_select_word_second(self,mock_random_choice):
        filtered_words = ['h1i','hey','hello','test','super','honeybee','brocode']
        mock_random_choice.return_value = 'h1i'      
        result = select_word(filtered_words)
        self.assertEqual(result, 'h1i')


class TestShowTheProgress(unittest.TestCase):

    def test_show_progress_first(self):
        gameword = 'hello'
        player_input = 'h'
        expected_output = 'h----'
        result = show_the_progress(gameword,player_input)
        self.assertEqual(result, expected_output )

    # def test_show_progress_second(self):
    #     gameword = 'hello'
    #     player_input = 'e'
    #     expected_output = 'he---'
    #     result = show_the_progress(gameword,player_input)
    #     self.assertEqual(result, expected_output )

    # def test_show_progress_third(self):
    #     gameword = 'hello'
    #     player_input = 'l'
    #     expected_output = 'hell-'
    #     result = show_the_progress(gameword,player_input)
    #     self.assertEqual(result, expected_output )

    # def test_show_progress_fourth(self):
    #     gameword = 'hello'
    #     player_input = 'o'
    #     expected_output = 'hello'
    #     result = show_the_progress(gameword,player_input)
    #     self.assertEqual(result, expected_output )

class TestShowHangman(unittest.TestCase):
    @patch('hangman.print_hangman')
    def  test_show_hangman0(self,mock_print_hangman):
        show_hangman(0)
        mock_print_hangman.assert_called_once_with(hangman[0])

    @patch('hangman.print_hangman')
    def test_show_hangman1(self,mock_print_hangman):
        show_hangman(1)
        mock_print_hangman.assert_called_once_with(hangman[7])

    @patch('hangman.print_hangman')
    def test_show_hangman2(self,mock_print_hangman):
        show_hangman(2)
        mock_print_hangman.assert_called_once_with(hangman[6])

    @patch('hangman.print_hangman')
    def test_show_hangman3(self,mock_print_hangman):
        show_hangman(3)
        mock_print_hangman.assert_called_once_with(hangman[5])
    @patch('hangman.print_hangman')
    def test_show_hangman4(self,mock_print_hangman):
        show_hangman(4)
        mock_print_hangman.assert_called_once_with(hangman[4])

    @patch('hangman.print_hangman')
    def test_show_hangman5(self,mock_print_hangman):
        show_hangman(5)
        mock_print_hangman.assert_called_once_with(hangman[3])

    @patch('hangman.print_hangman')
    def test_show_hangman6(self,mock_print_hangman):
        show_hangman(6)
        mock_print_hangman.assert_called_once_with(hangman[2])

    @patch('hangman.print_hangman')
    def test_show_hangman6(self,mock_print_hangman):
        show_hangman(7)
        mock_print_hangman.assert_called_once_with(hangman[1])    

class TestRetry(unittest.TestCase):
    @patch('hangman.input')
    @patch('hangman.game_room')
    def test_retry_Y(self,mock_game_room,mock_input):
        # mock_retry.return_value = False
        mock_input.return_value = 'Y'
        # mock_quit.return_value = True
        mock_game_room.return_value = None
        retry()
        #make sure game_room function called 
        mock_game_room.assert_called_once()


    @patch('hangman.input')
    @patch('hangman.game_room')    
    def test_retry_case_check(self,mock_game_room,mock_input):
        mock_input.return_value = 'y'
        mock_game_room.return_value = None
        retry()
        mock_game_room.assert_called_once()

    @patch('hangman.input')
    @patch('hangman.quit')
    def test_retry_N(self,mock_quit,mock_input):
        mock_input.return_value = 'N'
        mock_quit.return_value = None
        retry()
        mock_quit.assert_called_once()

    @patch('hangman.input')
    @patch('hangman.retry')
    def test_retry_other(self,mock_input,mock_retry):
        mock_input.return_value = 'q'
        mock_retry.return_value = None
        retry()
        mock_retry.assert_called_once()

    @patch('hangman.input')
    @patch('hangman.retry')
    def test_retry_empty(self,mock_input,mock_retry):
        mock_input.return_value = ''
        mock_retry.return_value = None
        retry()
        mock_retry.assert_called_once()



class TestGuess(unittest.TestCase):
    @patch('hangman.input')
    @patch('hangman.show_hangman')
    @patch('hangman.sleep',return_value = None)
    @patch('hangman.retry',return_value=None)
    def test_guess_True(self,mock_show_hangman,mock_sleep,mock_retry,mock_input):
        game_word = 'hello'     
        mock_input.side_effect = ['h', 'e', 'l', 'l','o'] 
        result = guess(game_word)
        self.assertEqual(result, True)

    @patch('hangman.input')
    @patch('hangman.show_hangman')
    @patch('hangman.sleep',return_value = None)
    @patch('hangman.retry',return_value=None)
    def test_guess_false(self,mock_show_hangman,mock_sleep,mock_retry,mock_input):
        game_word = 'abpe'     
        mock_input.side_effect = ['a', 'b', 'c', 'd','e','f','g','h','i','u'] 
        result = guess(game_word)
        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()