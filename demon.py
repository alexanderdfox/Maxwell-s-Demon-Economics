def demon_adjusted_tariff(partner_tariff_rate, us_import_value, us_export_value, epsilon=1e-9):
	"""
	Calculates the U.S. reciprocal tariff adjusted with a Maxwell's Demon-inspired entropy filter.
	
	Parameters:
		partner_tariff_rate (float): Partner's average tariff rate (e.g. 0.05 for 5%)
		us_import_value (float): U.S. import value from the partner
		us_export_value (float): U.S. export value to the partner
		epsilon (float): small number to prevent division by zero
	
	Returns:
		float: Adjusted reciprocal tariff
	"""
	trade_balance_ratio = us_export_value / (us_import_value + epsilon)  # Demon Efficiency Factor
	basic_tariff = (partner_tariff_rate / (partner_tariff_rate + 1)) * (us_import_value + us_export_value) - us_import_value
	demon_tariff = trade_balance_ratio * basic_tariff
	return demon_tariff


# Sample data for major trade partners
trade_partners = {
	"Canada": {
		"tariff_rate": 0.035,
		"us_imports": 350_000_000_000,
		"us_exports": 360_000_000_000
	},
	"European Union": {
		"tariff_rate": 0.05,
		"us_imports": 500_000_000_000,
		"us_exports": 450_000_000_000
	},
	"China": {
		"tariff_rate": 0.075,
		"us_imports": 450_000_000_000,
		"us_exports": 150_000_000_000
	},
	"Japan": {
		"tariff_rate": 0.025,
		"us_imports": 135_000_000_000,
		"us_exports": 75_000_000_000
	},
	"Mexico": {
		"tariff_rate": 0.04,
		"us_imports": 400_000_000_000,
		"us_exports": 300_000_000_000
	}
}

# Run calculation and print results
for country, data in trade_partners.items():
	adjusted = demon_adjusted_tariff(
		data["tariff_rate"],
		data["us_imports"],
		data["us_exports"]
	)
	print(f"{country} — Demon-Adjusted Tariff: ${adjusted:,.2f}")