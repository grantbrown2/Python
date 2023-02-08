class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print("---Display Info Method---")
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    def enroll(self):
        print("---Enroll Method---")
        if self.is_rewards_member:
            print("You are already a member!")
            return False
        self.is_rewards_member = True
        print(self.is_rewards_member)
        self.gold_card_points = 200
        print(self.gold_card_points)
    def spend_points(self, amount):
        print("===Point Spending Method===")
        if self.gold_card_points < amount:
            print("You do not have enough points!")
            return
        self.gold_card_points -= amount


grant = User("Grant", "Brown", "gbrownzzzz58@gmail.com", "21")
grant.display_info()
grant.enroll()

bob = User("Bob", "Jackson", "testemail@gmail.com", "52")
bob.is_rewards_member = True
bob.gold_card_points = 300
bob.display_info()
bob.enroll()
bob.spend_points(50)
bob.display_info()

john = User("John", "Green", "anotheremail@gmail.com", "32")
john.display_info()
john.enroll()
john.spend_points(280)
john.display_info()


