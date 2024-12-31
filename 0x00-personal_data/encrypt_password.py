#!/usr/bin/env python3

import bcrypt


def hash_password(password):
    """returns a encrypted password"""
    salt = bcrypt.gensalt()
    hashd_pwd = bcrypt.hashpw(password.encode(), salt)
    return hashd_pwd