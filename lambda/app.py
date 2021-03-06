import logging

from boto3 import client

logger = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)


def lambda_handler(event: dict, context) -> dict:
    """
    :param event: input data, usually a dict, but can also be list, str, int, float, or NoneType type.
    :param context: object providing info about invocation, function, and execution environment
    :return: dict with TranslatedText, SourceLanguageCode, TargetLanguageCode
    """
    logging.info(str(event))
    text = event.get('text', 'no input text provided')
    translate = client(service_name='translate', region_name='us-west-2', use_ssl=True)
    return translate.translate_text(Text=text, SourceLanguageCode='en', TargetLanguageCode='de')
