# your improved User class goes here
# ## Requirements
# 1. Add a method to your `User` class that allows for creating a new user post.
# 2. Add any necessary instance properties to make step 1 work.  What data structure should you use?
# 3. Add a class variable that stores the posts from every user.  What data structure should you use?
# 4. Make sure that the the information stays in sync!

# ## Bonus
# Add a method that allows for deleting a post.  Again, make sure that your information stays in sync.

class User:

    post_hist = {}
    def __init__(self,name,email_address,license_num):
        self.name = name
        self.email_address = email_address
        self.license_num = license_num
    
    def __str__(self):
        return f"{self.name} has email {self.email_address} and license # {self.license_num}."

    @property
    def post(self):
        return User.post_hist

    @post.setter
    def post(self, message):
        if self.name not in User.post_hist.keys():
            User.post_hist[self.name] = [message]
        else:
            User.post_hist[self.name].append(message)

    def remove_post(self, post_text):
        for i,item in enumerate(User.post_hist[self.name]):
            if post_text == item:
                User.post_hist[self.name].pop(i)

    
alice = User('alice', 'alice@email.com', 'asdlfkjaslkdfjsldf')
alice.post = 'hi'
alice.post = 'another'
alice.post = 'three'
print(alice.post)
alice.remove_post('hi')
print(alice.post)

talulah = User('talulah', 'talulah@email.com', 'asdlfkjaslkdfjsldf')
talulah.post = 'meep'
talulah.post = 'morp'
talulah.post = 'veracity'
print(talulah.post)


