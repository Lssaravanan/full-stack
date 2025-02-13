class A:
    def __init__(self):
        print("This is constructor")
    def sample(self):
        print("this is normal function")
    def __del__(self):
        print("bye...")
obj=A()
obj.sample()
