#!/usr/bin/env python3

"""
Data Container
Python 3.9+
Author: niftycode
Modified by: -
Date created: February 19th, 2022
Date modified: -
"""

from dataclasses import dataclass


@dataclass
class MessageData:
    """This dataclass is the store for the data:
    user id, text, date, service and account (caller id).
    """

    user_id: str
    text: str
    date: str
    phone_number: str
    service: str
    account: str
    is_from_me: int
    groupchat_id: str
    row_id: int

    def __str__(self):
        """String representation

        :return: the representation of this object
        """
        return (
            f"row id:\t\t{self.row_id}\n"
            f"user id:\t\t{self.user_id}\n"
            f"date and time:\t\t{self.date}\n"
            f"phone number:\t\t{self.phone_number}\n"
            f"service:\t\t{self.service}\n"
            f"caller id:\t\t{self.account}\n"
            f"direction:\t\t{'sent' if self.is_from_me else 'received'}\n"
            f"groupchat_id:\t\t{self.groupchat_id}"
            f"message: \n"
            # f"is_from_me:\t\t{self.is_from_me}\n"
            f"\n"
            f"text:\n"
            f"=====\n"
            f"{self.text}\n"
            f"\n"
            f"----------------------------------------------------------------\n"
        )
