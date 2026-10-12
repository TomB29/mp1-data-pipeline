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
from data_loaders import load_data
from data_processor import process_data, create_cleaning_report

logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt='%H:%M:%S'
        )
    logging.basicConfig(
        level=logging.info,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt='%H:%M:%S'
        )
    logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt='%H:%M:%S'
    )



def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Analyse a data file")
    args = parser.parse_args()
    parser.add_argument(
        "--input", "i",
        required=True,
        help="Path to input relevant file"
        )
    parser.add_argument(
        "--config", "-c",
        required=True,
        help="Accepts path to yaml config file")
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




def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    if not Path(filepath).is_file():
        logger.ERROR(f"Could not locate file requested in argument: {filepath.name}")
        raise FileNotFoundError(f"Input file not found: {filepath.name}")
    else:
        logger.info(f"Input file validated: {filepath}")
        return True



def main():
    parse_arguments()
    """Main pipeline function."""
    # TODO: implement
    try:
        logger.DEBUG(f"Argument Parsed: Input= {args.input}\nOutput= {args.output}")
        validate_input(args.input)
    except FileNotFoundError:
        sys.exit(1)

    try:
        logger.DEBUG(f"Argument Parsed: Input={args.input}\nOutput={args.output}")
        load_data(args.input)
        logger.info(f"Data loaded from {args.input}")
    except ValueError:
        sys.exit(1)

        


if __name__ == "__main__":
    main()