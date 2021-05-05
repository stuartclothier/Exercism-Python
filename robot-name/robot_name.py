class Robot:
    
    def __init__(self):
        import string
        import random
        self.name = f"{''.join(random.choices(string.ascii_uppercase, k = 2))}{''.join(random.choices(string.digits,k=3))}"
        
    def reset
print(Robot().name)