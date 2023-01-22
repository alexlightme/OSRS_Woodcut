import cProfile
import pstats
from pstats import SortKey



cProfile.run('start_RL_livefeed_v3(False)', 'stats')

p = pstats.Stats('stats')
p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(20)


