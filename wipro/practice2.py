import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    return a / b


divide(10, 2)
import re

pattern = r'\d+'
string = "Order 123, Invoice 456, Receipt 789."


for match in re.finditer(pattern, string):
    print("Match:", match.group(), "at position", match.span())
# Output:
# Match: 123 at position (6, 9)
# Match: 456 at position (18, 21)
# Match: 789 at position (30, 33)
