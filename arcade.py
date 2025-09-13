name = "Fred"
passes = 2
tokens = 10
price = 5.50
tokensPerGame = 2

totalTokens = passes * tokens
totalCost = passes * price
games = totalTokens // tokensPerGame

print("RECEIPT")
print("Name", name)
print("Passes", passes)
print("Tokens", totalTokens)
print(f"Total ${totalCost:.2f}")
print("Games", games)