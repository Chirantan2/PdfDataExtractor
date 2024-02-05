import re

def fetch_cin(text: str):
    """fetch CIN number

    Args:
        text (str): text to be searched

    Returns:
        _type_: matches
    """
    return re.findall(r'[UL]\d{5}\D{2}\d{4}\D{3}\d{6}', text), len(re.findall(r'[UL]\d{5}\D{2}\d{4}\D{3}\d{6}', text))

def fetch_email(text: str):
    """fetch email

    Args:
        text (str): text to be searched

    Returns:
        _type_: matches
    """
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)

def fetch_phone(text: str):
    """fetch landline phone numbers

    Args:
        text (str): text to be searched

    Returns:
        _type_: matches
    """
    return re.findall(r'\+?[6-9]?[6-8]?\d{11}', text)

def fetch_pan(text: str):
    """fetch PAN

    Args:
        text (str): text to be searched

    Returns:
        _type_: matches
    """
    return re.findall(r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}', text)


def fetch_websites(text: str):
    """fetch websites 

    Args:
        text (str): text to be searched

    Returns:
        _type_: matches
    """
    return re.findall(r'[w]{3}[.][\D]*[.][\w]{3}', text)

def fetch_dates(text: str):
    """fetch dates

    Args:
        text (str): text to be searched

    Returns:
        _type_: matches
    """
    return re.findall(r'\d{2}[/]\d{2}[/]\d{4}',text)

