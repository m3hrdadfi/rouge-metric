# coding=utf-8
# Copyright 2021 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python2, python3
"""A library for tokenizing text."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import six

from . import languages


def tokenize(text, language, stemmer):
    """Tokenize input text into a list of tokens.

    This approach aims to replicate the approach taken by Chin-Yew Lin in
    the original ROUGE implementation.

    Args:
      text: A text blob to tokenize.
      language: Handling text language.
      stemmer: An optional stemmer.

    Returns:
      A list of string tokens extracted from input text.
    """

    regex = languages.languages.get(language, "a-z0-9")

    # Convert everything to lowercase.
    text = text.lower()

    # Replace any non-alpha-numeric characters with spaces.
    text = re.sub(r"[^" + regex + "]+", " ", six.ensure_str(text))

    tokens = re.split(r"\s+", text)
    if stemmer:
        # Only stem words more than 3 characters long.
        tokens = [stemmer.stem(x) if len(x) > 3 else x for x in tokens]

    # One final check to drop any empty or invalid tokens.
    tokens = [x for x in tokens if re.match(r"^[" + regex + "]+$", six.ensure_str(x))]

    return tokens
