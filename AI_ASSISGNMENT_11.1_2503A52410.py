from collections import deque


class OrderQueue:
    """Manage e-commerce orders using a FIFO queue."""

    def __init__(self):
        """Initialize an empty order queue."""
        self.orders = deque()

    def add_order(self, order_id, customer_name):
        """Add a new order to the rear of the queue."""
        self.orders.append((order_id, customer_name))

    def process_order(self):
        """Remove and process the oldest order."""
        if not self.orders:
            return None

        return self.orders.popleft()

    def display_orders(self):
        """Display all pending orders."""
        if not self.orders:
            print("No pending orders.")
            return

        print("Pending Orders:")
        for order_id, customer in self.orders:
            print(f"Order ID: {order_id}, Customer: {customer}")


# Example usage
order_queue = OrderQueue()

# Add orders
order_queue.add_order(101, "Rahul")
order_queue.add_order(102, "Priya")
order_queue.add_order(103, "Arjun")

# Display pending orders
order_queue.display_orders()

# Process orders
print("\nProcessing:", order_queue.process_order())
print("Processing:", order_queue.process_order())

# Display remaining orders
print("\nRemaining Orders:")
order_queue.display_orders()