"""
This is translator module
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2020-08-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function translates the english text into french text
    """
    french_text = ''
    if english_text == '':
        return french_text
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    result = dict(json.loads(json.dumps(translation)))
    french_text = result['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    This function translates the french text into english text
    """
    english_text = ''
    if french_text == '':
        return english_text
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    result = dict(json.loads(json.dumps(translation)))
    english_text = result['translations'][0]['translation']
    return english_text
