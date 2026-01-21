# Trade Parameters
BUY_THRESHOLD = 25 # Fear
SELL_THRESHOLD = 70 # Greed

# Position Sizes
TRADE_PERCENT = 0.15
MAX_POSITION = 0.50

# Safety
MIN_USDC_BALANCE = 20 * 10**6
MIN_BALANCE_ETH = 0.01

# Max Gas Price
MAX_GAS_PRICE_GWEI = 5 #L2 gas pricing

# Risk Management
MIN_TRADE_INTERVAL = 864000 * 3 # 3 day trade interval

# Bot settings
DRY_RUN = True
CHECK_INTERVAL = 86400 # Daily-seconds 

# WBTC decimals
WBTC_DECIMALS = 8
MIN_WBTC = 0.0001
# Avoid dust issues
MIN_WBTC_POSITION = 10_000

# WBTC forked test whale
WBTC_WHALE = "0x2f5e87C9312fa29aed5c179E456625D79015299c"

# USDC forked test whale
USDC_WHALE = "0xEe7aE85f2Fe2239E27D9c1E23fFFe168D63b4055"
