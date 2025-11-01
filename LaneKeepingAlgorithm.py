"""Wrapper script kept for compatibility; calls into package implementation.

Usage:
    python LaneKeepingAlgorithm.py [--use-gpio]

By default GPIO is disabled so you can run this on a development machine.
"""

import argparse
from autonomous_lane_assist_system import lanekeeping


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-gpio", action="store_true", help="Enable RPi.GPIO control (requires running on a Pi)")
    args = parser.parse_args()
    lanekeeping.run_camera_loop(use_gpio=args.use_gpio)


if __name__ == "__main__":
    main()
GPIO.setup(in1,GPIO.OUT)

GPIO.setup(in2,GPIO.OUT)
