# Spencer Burton
# 9/23/20
# String Formatting Example

value1 = "123456789101112"
value2 = "3.13571985"
example = str.format("Formatted string {0:10.0} {1:4.4} {2:^50} {4:>50} {5:50}", value1, value2, "test", 42, 8, 9.10)
# print(example)

print(str.format("Example 'd': {0:15d}", 1500000))
print(str.format("Example ',': {0:15,}", 1500000))
print(str.format("Example 'e': {0:15e}", 3.14159584918545))
print(str.format("Example 'f': {0:15f}", 3.14159))
print(str.format("Example 'g': {0:15g}", 3.14159))
print(str.format("Example '%': {0:15%}", 0.75))
