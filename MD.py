import random

# Updated economic indicators
GDP_initial = 27000  # U.S. GDP in Q4 2024, in billion dollars
initial_debt = 36000  # Hypothetical national debt in billion dollars

# Policy parameters
threshold = 0.6  # Productivity threshold for Maxwell's Demon
interest_rate = 0.03  # 3% interest on debt
gov_subsidy_per_tx = 0.01  # Subsidy cost per accepted transaction, in billion dollars
waste_cost_per_tx = 0.005  # Cost per rejected transaction, in billion dollars
num_transactions = 1000000  # Number of transactions to simulate

# Generate transactions with random productivity scores between 0 and 1
transactions = [{'id': i, 'productivity': random.random()} for i in range(num_transactions)]

def maxwells_demon_with_debt(transactions, threshold, GDP, debt, interest_rate, gov_subsidy_per_tx, waste_cost_per_tx):
	productive_sector = []
	unproductive_sector = []

	for tx in transactions:
		if tx['productivity'] > threshold:
			productive_sector.append(tx)
			debt += gov_subsidy_per_tx  # Government subsidizes productive transactions
		else:
			unproductive_sector.append(tx)
			debt += waste_cost_per_tx  # Cost to manage unproductive transactions

	# Calculate GDP contributions
	gdp_contribution = sum(tx['productivity'] for tx in productive_sector)
	GDP += gdp_contribution

	# Calculate economic entropy (waste)
	entropy = sum(1 - tx['productivity'] for tx in unproductive_sector)

	# Apply interest on total debt
	debt += debt * interest_rate

	return {
		'GDP': GDP,
		'Entropy': entropy,
		'Debt': debt,
		'Accepted Transactions': len(productive_sector),
		'Rejected Transactions': len(unproductive_sector)
	}

# Run the simulation
results = maxwells_demon_with_debt(
	transactions,
	threshold,
	GDP_initial,
	initial_debt,
	interest_rate,
	gov_subsidy_per_tx,
	waste_cost_per_tx
)

# Display results
print(f"Simulated GDP: ${results['GDP']:.2f} billion")
print(f"Economic Entropy (waste): {results['Entropy']:.2f}")
print(f"Total Debt: ${results['Debt']:.2f} billion")
print(f"Accepted Transactions: {results['Accepted Transactions']}")
print(f"Rejected Transactions: {results['Rejected Transactions']}")
