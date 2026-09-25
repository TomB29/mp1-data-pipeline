"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path


logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%H:%M:%S'v
        )
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%H:%M:%S'v
        )
    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%H:%M:%S'v
    )



def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Analyse a data file")
    parser.add_argument(
        "--input", "i",
        required=True,
        help="Path to input relevant file"
        )
    parser.add_argument(
        "--output", "o",
        default="results.csv",
        help="Output file path"
        )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print detailed infomation"
        )
    #parser.add_argument(
        #"--format", "-f"
        #
        #)



def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    if not Path(filepath).is_file():
        logger.error("Input file not found: %s", filepath.name)
    else:
        logger.info("Input file validated: %s", filepath)
        return True



def main():
    """Main pipeline function."""
    pass  # TODO: implement
    #direction = Path(
    if validate_input(p):
        parse_arguments(p)


if __name__ == "__main__":
    main()