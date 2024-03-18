from contextlib import closing

"""Demonstrate raiding a refrigerator."""

class RefrigeratorRaider:
    """Raid a refrigerator."""

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print("Taking {}".format(food))

    def close(self):
        print("Close fridge door.")

def raid(food):
    r = RefrigeratorRaider()
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        r.close()


raid("bacon")
raid("deep fried pizza")
