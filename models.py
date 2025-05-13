import pickle
import os

class User:
    def __init__(self, user_id, username, password, email, phone):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.orders = []

    def login(self, password):
        return self.password == password

class Admin(User):
    def __init__(self, user_id, username, password, email, phone):
        super().__init__(user_id, username, password, email, phone)

class Ticket:
    def __init__(self, ticket_id, ticket_type, price, validity, features, quantity):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.price = price
        self.original_price = price
        self.validity_period = validity
        self.features = features
        self.available_quantity = quantity

    def isAvailable(self):
        return self.available_quantity > 0

class Order:
    def __init__(self, order_id, user_id, ticket_list, order_date):
        self.order_id = order_id
        self.user_id = user_id
        self.ticket_list = ticket_list
        self.order_date = order_date
        self.total_price = 0.0

    def calculateTotal(self, ticket_dict):
        self.total_price = sum(ticket_dict[tid].price for tid in self.ticket_list)

class Discount:
    def __init__(self):
        self.available = False

class SystemManager:
    def __init__(self):
        self.users = self.load_data("users.pkl")
        self.tickets = self.load_data("tickets.pkl")
        self.orders = self.load_data("orders.pkl")
        self.discount = self.load_discount("discount.pkl")

        default_tickets = {
            "T1": Ticket("T1", "Single Race", 300, "2025-11-01", "Main Stand", 100)
        }
        if not isinstance(self.tickets, dict):
            self.tickets = {}

        for tid, ticket in default_tickets.items():
            if tid not in self.tickets:
                self.tickets[tid] = ticket

        self.save_all()

    def load_data(self, filename):
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                return pickle.load(f)
        return {}

    def load_discount(self, filename):
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                return pickle.load(f)
        return Discount()

    def save_all(self):
        with open("users.pkl", "wb") as f: pickle.dump(self.users, f)
        with open("tickets.pkl", "wb") as f: pickle.dump(self.tickets, f)
        with open("orders.pkl", "wb") as f: pickle.dump(self.orders, f)
        with open("discount.pkl", "wb") as f: pickle.dump(self.discount, f)
