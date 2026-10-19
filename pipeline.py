"""
Data Processing Pipeline - CLI Template --> secondary update post final submission deadline

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --config config/config.yaml --verbose
"""

import argparse
import logging
import sys
from pathlib import Path
from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)

logger = logging.getLogger(__name__)





def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Analyse a data file")
    
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to input relevant file"
    )
    parser.add_argument(
        "--config", "-c",
        required=True,
        help="Accepts path to yaml config file")
    parser.add_argument(
        "--output", "-o",
        default="results.csv",
        help="Output file path"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print detailed infomation"
    )

    return parser.parse_args()
        









def main():
    """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    try:
        validate_input(args.input)
        logger.debug(f"Argument Parsed: Input= {args.input}\nOutput= {args.output}")
    except FileNotFoundError:
        sys.exit(1)
    
    try:
        logger.debug(f"Argument Parsed: Config File Validation -- {args.config}")
        validate_input(args.config)
    except FileNotFoundError:
        sys.exit(1)

    try:
        logger.debug(f"Argument Parsed: Input={args.input}\nOutput={args.output}")
        loaded_data = load_data(args.input)
        logger.info(f"Data loaded from {args.input}")
        loaded_config = load_data(args.config)
        logger.info(f"Config file loaded from {args.config}")
    except ValueError:
        sys.exit(1)

    required_columns = loaded_config["validation"]["required_columns"]
    numeric_columns = loaded_config["validation"]["numeric_columns"]
    DATAFRAME_COPY = loaded_data.copy

    try:
        validated_df = validate_dataframe(loaded_data, required_columns, numeric_columns)
        logger.info(f"""Validated frame contains {validated_df.shape[0]},
        {(loaded_data.shape[0] - validated_df.shape[0])} rows removed from {loaded_data.shape[0]} original rows""")
    except ValueError:
        sys.exit(1)

    try:
        processed = process_data(validated_df, loaded_config)
    except ValueError:
        sys.exit(1)
    
    print(create_cleaning_report(validated_df, processed))
    logger.info(f"""processed data from {args.input} 
    input using {args.config} configuration settings""")
    save_data(processed, args.output)
    logger.info(f"saved processed data to {args.output}")
        




        


if __name__ == "__main__":
    main()