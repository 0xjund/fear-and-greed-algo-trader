from env.fork_setup import seed_fork_tokens
from moccasin.config import get_active_network

active_network = get_active_network()

if active_network.forked_network():
    seed_fork_tokens(active_network)

# Fix
# run_bot()
