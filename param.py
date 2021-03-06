import argparse

parser = argparse.ArgumentParser(description='parameters')


# -- Basic --
parser.add_argument('--seed', type=int, default=42,
                    help='random seed (default: 42)')
parser.add_argument('--eps', type=float, default=1e-6,
                    help='epsilon (default: 1e-6)')
parser.add_argument('--logging_level', type=str, default='info',
                    help='logging level (default: info)')
parser.add_argument('--log_to', type=str, default='print',
                    help='logging destination, "print" or a filepath (default: print)')
parser.add_argument('--output_folder', type=str, default='./output/',
                    help='Output folder')


# -- BBA --
parser.add_argument('--bba_reservoir', type=float, default=5,
                    help='BBA - Reservoir (default: 5)')
parser.add_argument('--bba_cushion', type=float, default=10,
                    help='BBA - Cushion (default: 10)')


# -- MPC --
parser.add_argument('--mpc_lookback', type=int, default=5,
                    help='MPC - Throughput lookback (default: 5)')
parser.add_argument('--mpc_lookahead', type=int, default=5,
                    help='MPC - Throughput lookahead (default: 5)')

config = parser.parse_args()
