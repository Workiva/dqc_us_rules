# Copyright (c) 2015, Workiva Inc.  All rights reserved
# Copyright (c) 2015, XBRL US Inc.  All rights reserved
import json
import os.path

_LOADED_MESSAGES = None


def _load_messages(filename=None):
    """
    Loads the messages from the filename passed in.  If nothing is passed in, it defaults to the message_info.json
    """
    global _LOADED_MESSAGES
    if not filename:
        directory, _ = os.path.split(__file__)
        filename = os.path.join(directory, 'message_info.json')
    with open(filename, 'r') as f:
        _LOADED_MESSAGES = json.load(f)


def get_message(primary_number, secondary_number='default'):
    """
    Gets the message for a primary number and a secondary number for a message categorization.  If the rule
    doesn't have the secondary number in existence, it grabs the default value for the primary categorization.

    @param primary_number: The primary number for the rule.  Should be a string.
    @param: The secondary number for the rule.  Should be a string.
    @return: The message text, or None if the primary number does not exist
    """
    global _LOADED_MESSAGES
    if not _LOADED_MESSAGES:
        _load_messages()
    if primary_number not in _LOADED_MESSAGES:
        return '(Message code not found)'
    return _LOADED_MESSAGES[primary_number].get(secondary_number, _LOADED_MESSAGES[primary_number]['default'])
