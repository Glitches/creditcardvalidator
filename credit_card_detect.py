''' MY credit card validator'''

class Credit_card(object):
    '''This class provides some method to generate and validate
    credit card
    '''


    def __init__(self):
        self.card_number = ''
        self.card_digits = 0


    def number_of_digits(self, ccnum):
        '''Total number of digits'''
        return len(ccnum)

    def which_issuer(self, ccnum):
        '''Verifies first digits and return which issuer is
        Visa: Card numbers start with a 4.
        MasterCard: Card numbers start with the numbers 51 through 55.
        Discover: Card numbers begin with 6011 or 65.
        American Express (Amex): Card numbers beginning with 34 or 37.

        input
        ccnum it's the credit card code number
        '''
        # print(ccnum)
        if int(ccnum[0]) == 4:
            print('Number %s it\'s a VISA card!' %(ccnum))
            print()
            print()
        elif  51 <= int(ccnum[0:2]) <= 55:
            print('Number %s it\'s a MASTERCARD card!' %(ccnum))
            print()
            print()
        elif int(ccnum[0]) == 3:
            print('Number %s it\'s an AMERICAN EXPRESS card!' %(ccnum))
            print()
            print()
        elif int(ccnum[0]) == 6:
            print('Number %s it\'s a DISCOVER card!' %(ccnum))
            print()
            print()

    def mod10_algo(self, ccnum):
        ''' Computes M10 algorithm on the input code

        input
        ccnum it's the credit card code number
        '''
        self.card_number = ccnum
        # print(self.card_number) # debug
        i, s, number, digit_sum = self.card_digits -2, 0, 0, 0
        while i != -1:
            if i%2 != 0:
                number = int(self.card_number[i]) * 2
            else:
                number = int(self.card_number[i])
            # print(number) # debug
            if number >= 10:
                number, reminder = divmod(number, 10)
                number += reminder
                # print('Numero sommato ' + str(number)) # debug
            digit_sum += number
            # print('Somma: ' + str(digit_sum)) # debug
            i -= 1
        digit_sum = digit_sum * 9
        # print('digit_sum ' + str(digit_sum)) # Debug
        if str(digit_sum)[-1] == self.card_number[self.card_digits -1]:
            print('Card number %s is valid!' %(self.card_number))
            print()
            print()
            return True
        else:
            print(str(digit_sum)[-1])
            print('This isn\'t a valid card number')
            print()
            print()


first = Credit_card()
print()
number = input('Type card number to verify: ')
print()
print()
first.card_digits = first.number_of_digits(number)
if first.mod10_algo(number) == True:
    first.which_issuer(number)
