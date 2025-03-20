# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost , added 0.2
shipping_cost = weight * rate * 0.2

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

