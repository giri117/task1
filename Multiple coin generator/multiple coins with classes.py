#here we use inheritance concept. Means here child class will use parent function
#we use dictonaries
#we use Super function to get acces for the parent class

import random #this is solely used in fliping concept

class Coin:#here we define and construct all the general things a coin has and needs
    def __init__(self,rare=False,clean=True,heads=True,**kwarg):
        for key,value in kwarg.items():
          setattr(self,key,value)
        self.head=heads
        self.is_rare=rare
        if self.is_rare:
             self.value=self.original_value*2
        else:
             self.value=self.original_value
        self.is_clean=clean
        if self.is_clean:
             self.color=self.original_color
        else:
             self.color=self.rusted_color
    
    def flip(self):
        head_options= [True,False]
        choice= random.choice(head_options)
        self.head= choice
    def __del__(self):
        print('coin is spent')

    def rust(self):
        self.color=self.rusty_color
    def clean(self):
        self.color=self.original_color
    def __str__(self):#this constructor can change the form of output printing into our wish. 
        if self.original_value>=1:
            return '£{} coin'.format(int(self.original_value))
        else:
            return '{}p coin'.format(int(self.original_value*100))

class One_paisa(Coin):
    def __init__(self):
        info={
            'original_value':0.01,
            'original_color':'bronze',
            'rusty_color':'violet',
            'mass':1
            }
        super().__init__(**info)

class Two_paisa(Coin):
    def __init__(self):
        info={
            'original_value':0.02,
            'original_color':'orange',
            'rusty_color':'red',
            'mass':2
            }
        super().__init__(**info)

class Two_Rupee(Coin):
    def __init__(self):
        info={
            'original_value':2,
            'original_color':'silver',
            'rusty_color':'violet',
            'mass':10
            }
        super().__init__(**info)

class Five_Rupee(Coin):
    def __init__(self):
        info={
            'original_value':5,
            'original_color':'Lite gold',
            'rusty_color':'lite yellow',
            'mass':25
            }
        super().__init__(**info)

class Fifty_Rupee(Coin):
    def __init__(self):
        info={
            'original_value':50,
            'original_color':'gold',
            'rusty_color':'yellow',
            'mass':30
            }
        super().__init__(**info)
class Hundred_Rupee(Coin):
    def __init__(self):
        info={
            'original_value':100,
            'original_color':'Diamond',
            #'clean_color':'anything',
            'rusty_color':None,
            'mass':10
            }
        super().__init__(**info)
        def rust(self):
            self.color=self.original_color
        def clean(self):
            self.color=self.original_color

        

class Rupee(Coin):#here we inherited the class coin.
    def __init__(self):
        info={
            'original_value':1.00,
            'original_color':'silver',
            'rusty_color':'copper',
            'mass':10
            }
        super().__init__(**info)#here we are unpacking data and this will be packed into the class coin through **kwargs            
            

coins=[One_paisa(), Two_paisa(), Two_Rupee(), Five_Rupee(), Fifty_Rupee(), Hundred_Rupee(), Rupee()]#here we have to keep "()" after evry class otherwise it can't be opened. then the values inside were hided and we get error as there are no such values in that particular class

for coin in coins:
    arguments=[coin,coin.value,coin.color,coin.mass]
    strings='{}-value:{}, color{}, mass g{}'.format(*arguments)#here we are packing arguments into format. so we have to use "*" definetly other wise we will get errors
    print(strings)
        
    
    
    
        
