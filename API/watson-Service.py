# #you will need the following library 
#!pip install ibm_watson wget

from ibm_watson import SpeechToTextV1 
from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

url_lt=''
apikey_lt=''
url_s2t = ""
iam_apikey_s2t = ""

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
print(s2t)

version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')

translation=translation_response.get_result()
spanish_translation =translation['translations'][0]['translation']
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
translation_eng=translation_new['translations'][0]['translation']
French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()
French_translation['translations'][0]['translation']