class Portfolio:

    def __init__(self, assets):
        # assets is a list of stock tickers
        self.assets = assets

    def __str__(self):
        return str(self.assets)

    def __getitem__(self, key):
        # Single Indexing (1-based: tech_portfolio[1] -> first asset)
        if isinstance(key, int):
            if key <= 0:
                raise IndexError(
                    "1-based indexing required (indices start at 1)"
                )
            return self.assets[key - 1]

        # Slicing (1-based: tech_portfolio[1:3] -> assets 1 and 2)
        elif isinstance(key, slice):
            start = (key.start - 1) if key.start is not None else None
            stop = (key.stop - 1) if key.stop is not None else None
            return self.assets[start : stop : key.step]

        else:
            raise TypeError("Index must be an integer or a slice")

    def __len__(self):
        return len(self.assets)


# Instantiating the object
tech_portfolio = Portfolio(['AAPL', 'NVDA', 'GOOGL', 'MSFT', 'AMZN'])

# Personalized 1-based indexing
print(tech_portfolio[1])  # Output: AAPL

# Slicing (1st to 3rd element non-inclusive -> elements 1 & 2)
print(tech_portfolio[1:3])  # Output: ['AAPL', 'NVDA']

# Iteration (Manual loop with 1-based indexing)
for i in range(1, len(tech_portfolio) + 1):
    print(f"Holding: {tech_portfolio[i]}")

#  Membership Testing
print('NVDA' in tech_portfolio.assets)  # Output: True