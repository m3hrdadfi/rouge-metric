<h1 align="center">Python ROUGE implementation 🦁</h1>

> FOR EVERY LANGUAGE

<br/><br/>


This is a wrapper version of Rouge by [Google](https://github.com/google-research/google-research/tree/master/rouge) 
implemented based on [HF metrics](https://huggingface.co/metrics/rouge) for every language.

## How to use

### Requirements

```bash
# requirement packages

pip install -r requirements.txt
git clone https://github.com/m3hrdadfi/rouge-metric .
```

### Load rouge wrapper

```python
from datasets import load_metric

metric = load_metric("./rouge")
```

### Calculate
You just need to enter your language code (ISO code) in the language argument.

```python
references = ["The quick brown fox jumps over the lazy dog"]
predictions = ["The quick black cat jumps over the lazy fox"]
result = metric.compute(predictions=predictions, references=references, language="en")
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: English, result: {result}")
```

**Output**
```text
Language: English, result: {'rouge1': 77.78, 'rouge2': 50.0, 'rougeL': 66.67, 'rougeLsum': 66.67}
```

---

```python
references = ["روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد"]
predictions = ["گربه سیاه سریع از روی روباه تنبل می‌پرد"]
result = metric.compute(predictions=predictions, references=references, language="fa")
result = {key: round(value.mid.fmeasure, 4) * 100 for key, value in result.items()}
print(f"Language: Persian, result: {result}")
```

**Output**
```text
Language: Persian, result: {'rouge1': 75.0, 'rouge2': 42.86, 'rougeL': 62.5, 'rougeLsum': 62.5}
```

## How to contribute
Currently, I'm filling the language requirements and probably would complete them shortly. 
But if you want to help me in this way, you're welcome.
You just need to provide the regex and best stemmer package for the language you want or even your native language in an issue or make a pull request as follows.

1. Fork the [repository](https://github.com/m3hrdadfi/rouge-metric) by clicking on the 'Fork' button on the repository's page. 
   This creates a copy of the code under your GitHub user account.
2. Clone your fork to your local disk, and add the base repository as a remote:
    ```bash
    git clone git@github.com:<your Github handle>/rouge-metric.git
    cd rouge-metric
    git remote add upstream https://github.com/m3hrdadfi/rouge-metric.git
    ```
3. Set up a development environment by running the following command in a virtual environment:
    ```bash
    conda create -n env python=3.8 --y
    conda activate env
    pip install -r requirements.txt 
    ```
4. Create a new branch to hold your development changes:
    ```bash
    git checkout -b a-descriptive-name-for-your-changes-languages
    ```
   
    **Do not work on the `master` branch.**
5. Develop the features/languages on your branch.
6. Once you're happy with your implementation, add your changes and make a commit to record your changes locally:
    ```bash
    git add -A
    git commit -m "YOUR MESSAGE"
    ```
    It is a good idea to sync your copy of the code with the original repository regularly. This way you can quickly account for changes:
    ```bash
    git fetch upstream
    git rebase upstream/main
    ```
   Push the changes to your account using:
    ```bash
    git push -u origin a-descriptive-name-for-your-changes-languages
    ```
7. Once you are satisfied, go the webpage of your fork on GitHub. Click on "Pull request" to send your to the project maintainers for review.

## License

[Apache License 2.0](LICENSE)

## Languages

|              Language Name             | Language Code | Status |
|:--------------------------------------:|:-------------:|:------:|
|                  Afar                  |       aa      |        |
|                Abkhazian               |       ab      |        |
|                 Avestan                |       ae      |        |
|                Afrikaans               |       af      |        |
|                  Akan                  |       ak      |        |
|                 Amharic                |       am      |        |
|                Aragonese               |       an      |        |
|                 Arabic                 |       ar      |        |
|                Assamese                |       as      |        |
|                 Avaric                 |       av      |        |
|                 Aymara                 |       ay      |        |
|               Azerbaijani              |       az      |        |
|                 Bashkir                |       ba      |        |
|               Belarusian               |       be      |        |
|                Bulgarian               |       bg      |        |
|            Bihari languages            |       bh      |        |
|                 Bislama                |       bi      |        |
|                 Bambara                |       bm      |        |
|                 Bengali                |       bn      |        |
|                 Tibetan                |       bo      |        |
|                 Breton                 |       br      |        |
|                 Bosnian                |       bs      |        |
|           Catalan; Valencian           |       ca      |        |
|                 Chechen                |       ce      |        |
|                Chamorro                |       ch      |        |
|                Corsican                |       co      |        |
|                  Cree                  |       cr      |        |
|                  Czech                 |       cs      |        |
| Church Slavic; Slavonic; Old Bulgarian |       cu      |        |
|                 Chuvash                |       cv      |        |
|                  Welsh                 |       cy      |        |
|                 Danish                 |       da      |        |
|                 German                 |       de      |        |
|       Divehi; Dhivehi; Maldivian       |       dv      |        |
|                Dzongkha                |       dz      |        |
|                   Ewe                  |       ee      |        |
|          Greek, Modern (1453-)         |       el      |        |
|                 English                |       en      |    ✅   |
|                Esperanto               |       eo      |        |
|           Spanish; Castilian           |       es      |        |
|                Estonian                |       et      |        |
|                 Basque                 |       eu      |        |
|                 Persian                |       fa      |    ✅   |
|                  Fulah                 |       ff      |        |
|                 Finnish                |       fi      |        |
|                 Fijian                 |       fj      |        |
|                 Faroese                |       fo      |        |
|                 French                 |       fr      |        |
|             Western Frisian            |       fy      |        |
|                  Irish                 |       ga      |    ✅   |
|         Gaelic; Scottish Gaelic        |       gd      |        |
|                Galician                |       gl      |        |
|                 Guarani                |       gn      |        |
|                Gujarati                |       gu      |        |
|                  Manx                  |       gv      |        |
|                  Hausa                 |       ha      |        |
|                 Hebrew                 |       he      |        |
|                  Hindi                 |       hi      |        |
|                Hiri Motu               |       ho      |        |
|                Croatian                |       hr      |        |
|         Haitian; Haitian Creole        |       ht      |        |
|                Hungarian               |       hu      |        |
|                Armenian                |       hy      |        |
|                 Herero                 |       hz      |        |
|               Interlingua              |       ia      |        |
|               Indonesian               |       id      |        |
|         Interlingue; Occidental        |       ie      |        |
|                  Igbo                  |       ig      |        |
|            Sichuan Yi; Nuosu           |       ii      |        |
|                 Inupiaq                |       ik      |        |
|                   Ido                  |       io      |        |
|                Icelandic               |       is      |        |
|                 Italian                |       it      |        |
|                Inuktitut               |       iu      |        |
|                Japanese                |       ja      |        |
|                Javanese                |       jv      |        |
|                Georgian                |       ka      |    ✅   |
|                  Kongo                 |       kg      |        |
|             Kikuyu; Gikuyu             |       ki      |        |
|           Kuanyama; Kwanyama           |       kj      |        |
|                 Kazakh                 |       kk      |        |
|        Kalaallisut; Greenlandic        |       kl      |        |
|              Central Khmer             |       km      |        |
|                 Kannada                |       kn      |        |
|                 Korean                 |       ko      |        |
|                 Kanuri                 |       kr      |        |
|                Kashmiri                |       ks      |        |
|                 Kurdish                |       ku      |        |
|                  Komi                  |       kv      |        |
|                 Cornish                |       kw      |        |
|             Kirghiz; Kyrgyz            |       ky      |        |
|                  Latin                 |       la      |        |
|      Luxembourgish; Letzeburgesch      |       lb      |        |
|                  Ganda                 |       lg      |        |
|    Limburgan; Limburger; Limburgish    |       li      |        |
|                 Lingala                |       ln      |        |
|                   Lao                  |       lo      |        |
|               Lithuanian               |       lt      |    ✅   |
|              Luba-Katanga              |       lu      |        |
|                 Latvian                |       lv      |        |
|                Malagasy                |       mg      |        |
|               Marshallese              |       mh      |        |
|                  Maori                 |       mi      |        |
|               Macedonian               |       mk      |        |
|                Malayalam               |       ml      |        |
|                Mongolian               |       mn      |        |
|                 Marathi                |       mr      |        |
|                  Malay                 |       ms      |        |
|                 Maltese                |       mt      |        |
|                 Burmese                |       my      |        |
|                  Nauru                 |       na      |        |
|            Norwegian Bokmål            |       nb      |        |
|      Ndebele, North; North Ndebele     |       nd      |        |
|                 Nepali                 |       ne      |        |
|                 Ndonga                 |       ng      |        |
|             Dutch; Flemish             |       nl      |        |
|            Norwegian Nynorsk           |       nn      |        |
|                Norwegian               |       no      |        |
|      Ndebele, South; South Ndebele     |       nr      |        |
|             Navajo; Navaho             |       nv      |        |
|         Chichewa; Chewa; Nyanja        |       ny      |        |
|           Occitan (post 1500)          |       oc      |        |
|                 Ojibwa                 |       oj      |        |
|                  Oromo                 |       om      |        |
|                  Oriya                 |       or      |        |
|            Ossetian; Ossetic           |       os      |        |
|            Panjabi; Punjabi            |       pa      |        |
|                  Pali                  |       pi      |        |
|                 Polish                 |       pl      |        |
|             Pushto; Pashto             |       ps      |        |
|               Portuguese               |       pt      |        |
|                 Quechua                |       qu      |        |
|                 Romansh                |       rm      |        |
|                  Rundi                 |       rn      |        |
|      Romanian; Moldavian; Moldovan     |       ro      |        |
|                 Russian                |       ru      |        |
|               Kinyarwanda              |       rw      |        |
|                Sanskrit                |       sa      |        |
|                Sardinian               |       sc      |        |
|                 Sindhi                 |       sd      |        |
|              Northern Sami             |       se      |        |
|                  Sango                 |       sg      |        |
|           Sinhala; Sinhalese           |       si      |        |
|                 Slovak                 |       sk      |        |
|                Slovenian               |       sl      |        |
|                 Samoan                 |       sm      |        |
|                  Shona                 |       sn      |        |
|                 Somali                 |       so      |        |
|                Albanian                |       sq      |        |
|                 Serbian                |       sr      |        |
|                  Swati                 |       ss      |        |
|             Sotho, Southern            |       st      |        |
|                Sundanese               |       su      |        |
|                 Swedish                |       sv      |        |
|                 Swahili                |       sw      |        |
|                  Tamil                 |       ta      |        |
|                 Telugu                 |       te      |        |
|                  Tajik                 |       tg      |        |
|                  Thai                  |       th      |        |
|                Tigrinya                |       ti      |        |
|                 Turkmen                |       tk      |        |
|                 Tagalog                |       tl      |        |
|                 Tswana                 |       tn      |        |
|          Tonga (Tonga Islands)         |       to      |        |
|                 Turkish                |       tr      |    ✅   |
|                 Tsonga                 |       ts      |        |
|                  Tatar                 |       tt      |        |
|                   Twi                  |       tw      |        |
|                Tahitian                |       ty      |        |
|             Uighur; Uyghur             |       ug      |        |
|                Ukrainian               |       uk      |        |
|                  Urdu                  |       ur      |        |
|                  Uzbek                 |       uz      |        |
|                  Venda                 |       ve      |        |
|               Vietnamese               |       vi      |        |
|                 Volapük                |       vo      |        |
|                 Walloon                |       wa      |        |
|                  Wolof                 |       wo      |        |
|                  Xhosa                 |       xh      |        |
|                 Yiddish                |       yi      |        |
|                 Yoruba                 |       yo      |        |
|             Zhuang; Chuang             |       za      |        |
|                 Chinese                |       zh      |        |
|                  Zulu                  |       zu      |        |