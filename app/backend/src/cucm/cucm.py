import os
import json

from src.ciscoaxl import axl




cucm = "10.10.20.1"
username = "administrator"
password = "ciscopsdt"
version = "12.5"


def auth():
    ucm = axl(
        username=username, 
        password=password, cucm=cucm, 
        cucm_version=version
        )
    return ucm
ucm = auth()


