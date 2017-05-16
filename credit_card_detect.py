''' MY credit card validator'''

class Credit_card():

    card_digits = 0

    def __init__(self, ccnum):
        self.card_number = ccnum


    def number_of_digits(self):
        '''Total number of digits'''
        return len(self.card_number)


    def mod10_algo(self):
        cclist = self.card_number
        print(cclist)
        i, s, number, digit_sum = self.card_digits -2, 0, 0, 0
        while i != -1:
            if i%2 == 0:
                number = int(cclist[i]) * 2
            else:
                number = int(cclist[i])
            print(number)
            if number >= 10:
                number, reminder = divmod(number, 10)
                number += reminder
                print('Numero sommato ' + str(number))
            digit_sum += number
            print('Somma: ' + str(digit_sum))
            i -= 1
        digit_sum = digit_sum * 9
        # print('digit_sum ' + str(digit_sum)) # Debug 
        if str(digit_sum)[-1] == cclist[self.card_digits -1]:
            print('This card is valid')
            print()
            print(self.card_number)
        else:
            print(str(digit_sum)[-1])
            print('This isn\'t a valid card number')

first = Credit_card('38520000023237')
first.card_digits = first.number_of_digits()
first.mod10_algo()
