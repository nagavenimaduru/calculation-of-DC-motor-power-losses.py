# DC Motor Power Loss Calculator

print("===== DC Motor Power Loss Calculator =====")

# Input values
input_power = float(input("Enter input power of motor (W): "))
output_power = float(input("Enter output power of motor (W): "))

# Calculate power loss
power_loss = input_power - output_power

# Calculate efficiency
efficiency = (output_power / input_power) * 100

print("\n===== Results =====")
print(f"Input Power  : {input_power:.2f} W")
print(f"Output Power : {output_power:.2f} W")
print(f"Power Loss   : {power_loss:.2f} W")
print(f"Efficiency   : {efficiency:.2f} %")
