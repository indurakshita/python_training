import random 
class Cards:
    
    def __init__(self):
        self.shapes = ["Hearts","Diamonds","Clubs","Spades"]
        self.numbers = ["2","3","4","5","6","7","8","9","10","jack","Queen","king","ace"]
        self.cards = [f"{shape} - {number}" for shape in self.shapes for number in self.numbers]
        self.new_cards = None
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards
    
    def get_card(self):
        
            self.new_cards = random.choices(self.cards,k=2)
            for card in self.new_cards:
                self.cards.remove(card)
            return self.new_cards
        
    @property
    def len_card(self):
        return len(self.cards)
    
    def color(self,cards):
        colors = {
            "Hearts": "\033[91m",  
            "Diamonds": "\033[91m",  
            "jack": "\033[91m",  
            "Queen": "\033[91m", 
            "ace": "\033[91m",  
        }

        for card1 in cards:
           
             shape,number = card1.split("-")
             
             color_shape = colors.get(shape,"") + shape
             color_number = colors.get(number,'') + number
             print(f'{color_shape},{color_number}')

card = Cards()
card.shuffle()
card.get_card()
card.len_card
color_card = card.new_cards
card.color(color_card)

# -----------------------------------------------------------------------------------------------------------

# Using decorators for colors

# import random

# class Cards:

#     def dec_color(func):
#         def wrapper(self, cards):
#             colors = {
#                 "Hearts": "\033[91m",  
#                 "Diamonds": "\033[91m",  
#                 "jack": "\033[91m",  
#                 "Queen": "\033[91m", 
#                 "Clubs": "\033[91m",
#                 "Spades": "\033[91m",
#                 "ace": "\033[91m",  
#             }
            
            
            
#             for card1 in cards:
#                 shape, number = card1.split("-")
#                 color_shape = colors.get(shape, "\033[0;34m") + shape
#                 color_number = colors.get(number, "\033[0;37m") + number
#                 result = print(f"{color_shape} - {color_number}\033[0m")
        
#         return wrapper


#     def __init__(self):
#         self.shapes = ["Hearts", "Diamonds", "Clubs", "Spades"]
#         self.numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "Queen", "king", "ace"]
#         self.cards = [f"{shape} - {number}" for shape in self.shapes for number in self.numbers]
#         self.new_cards = None
    
#     def shuffle(self):
#         random.shuffle(self.cards)
#         return self.cards
    
#     @dec_color()
#     def get_card(self):
#         self.new_cards = random.choices(self.cards, k=1)
#         for card in self.new_cards:
#             self.cards.remove(card)
#         return self.new_cards
    
#     @property
#     def len_card(self):
#         return len(self.cards)
    
 
    
# card = Cards()
# card.shuffle()
# final = card.get_card()


