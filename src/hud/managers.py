

# class OrderManager():

#     def create_order(self, number=None, **extra_fields):
#         # Creates and save a new user
#         if not number:
#             raise ValueError('Users must provide a number for an order to be created!')

#         order = self.model(number=self.number, **extra_fields)
#         order.save(using=self._db)

#         return order
