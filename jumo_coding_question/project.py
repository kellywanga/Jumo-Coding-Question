import logging.config
import sys

from jumo_coding_question.configurations import Config
from jumo_coding_question.configurations.logging_config import (
    get_logging_configuration
)
from jumo_coding_question.Utils import file_actions, data_actions


def run(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

    config_instance = Config()
    logging.config.dictConfig(get_logging_configuration(config_instance))

    file_contents = file_actions.CSVFileRead.readfile(
        config_instance.INPUTS_DIRECTORY + "Loans.csv"
    )

    if file_contents == None:
        logging.debug("Could not read file!")
        quit()

    data_items = data_actions.CreateDictFromCSVData.CSVDataToDict(
        file_contents
    )
    logging.debug(data_items)
    print(data_items)


if __name__ == "__main__":
    run()
