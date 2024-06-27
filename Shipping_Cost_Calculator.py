# Shipping Cost Calculator

## Input package weight and shipping rate 
weight = float(input("Enter the package weight i kilograms: "))
rate = float(input("Enter the shiping rate per kilograms: "))

## Calculate shipping cost 
Shipping_cost = weight * rate 

## Display the results 
print(f"Shipping Cost: {shipping_cost} USD")
