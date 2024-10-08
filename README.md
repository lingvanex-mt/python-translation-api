# Python Translation API
Discover the Power of Lingvanex Translator Service

Unlock the potential of your applications with Lingvanex Translator, a cutting-edge cloud-based neural machine translation service. Compatible with any operating system, free translation api Python Lingvanex enables the creation of intelligent, multi-lingual solutions for all supported languages. Whether you are looking for a python translation API, or need to translate text efficiently, Lingvanex offers a powerful solution for developers.

With Lingvanex, you can effortlessly translate both text and HTML pages, enhancing your global reach and communication capabilities. Our free translation API for Python allows you to start integrating translation functionality into your projects quickly and easily. Additionally, our python library for translation ensures smooth integration with minimal setup. You can also explore a specialized python language translation library, making it easy to build language tools.

Explore the capabilities of the [Lingvanex Cloud API](https://lingvanex.com/en/translationapi/) and learn more about our [Secure On-Premise Machine Translation](https://lingvanex.com/). This versatile tool provides developers with a **python library to translate text**, offering a robust way to handle translations in your application. For those seeking a free python translation API, Lingvanex offers solutions that meet all levels of demand.


# How to get the authentication key
Before using the API you need to create the [account](https://lingvanex.com/registration/) and then generate the API key at the bottom of the page. You must use this authorization key to authorize requests.


# Installation
You can install the library with PyPI using pip:

```
pip install lingvanex
```


# Requirements
* Python version >= 3.6
* Requests module version >= 2.0


# Getting the list of languages
To retrieve the list of languages, perform a GET request with the authentication key as follows:
```
import requests

url = "https://api-b2b.backenster.com/b1/api/v3/getLanguages?platform=api&code=en_GB"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
```

Options:
* `url`: https://api-b2b.backenster.com/b1/api/v3/getLanguages
* `platform`: api
* `Authorization`: The key must be obtained in advance
* `code`: the language code in the format “language code_code of the country”, which is used to display the names of the languages. The language code is represented only in lowercase letters, the country code only in uppercase letters (example en_GB, es_ES, ru_RU etc). If this option is not present, then English is used by default.


# Translate Python Text
This POST method translates text and HTML single string or arrays with the authentication key. Also it performs transliteration, language auto detection.

```
import requests

url = "https://api-b2b.backenster.com/b1/api/v3/translate"

payload = {
    "platform": "api",
    "from": "en_GB",
    "to": "de_DE",
    "data": "Some text",
    "translateMode": "html",
    "enableTransliteration": True
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

Options:
* `url`: https://api-b2b.backenster.com/b1/api/v3/translate
* `platform`: api
* `Authorization`: The key must be obtained in advance
* `from`: the language code in the format “language code_code of the country” from which the text is translated. The language code is represented only in lowercase letters, the country code only in uppercase letters (example en_GB, es_ES, ru_RU and etc.). If this parameter is not present, the auto-detect language mode is enabled.
* `to`: language code in the format “language code_code of the country” to which the text is translated (required)
* `data`: data for translation.
* `translateMode`: Describe the input text format. Possible value is "html" for translating and preserving html structure. If the value is not specified or is other than "html" then plain text is translating.
* `enableTransliteration`: If true response includes sourceTransliteration and targetTransliteration fields.


# Issues
If you are having problems using the library, please [contact](https://lingvanex.com/en/contact-us/) us.


