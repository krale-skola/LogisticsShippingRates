# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilgrams: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"The shipping cost is: {shipping_cost} USD")
