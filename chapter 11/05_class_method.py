class employee:
    a  = 1

    @classmethod
    def show (cls):
        print(f"The class arrtibute is {cls.a}")


o = employee()

o.a = 3

o.show()