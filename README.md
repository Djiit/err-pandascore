# err-pandascore - Basic Pandascore API Err integration

[![Build Status](https://travis-ci.org/Djiit/err-pandascore.svg?branch=master)](https://travis-ci.org/Djiit/err-pandascore) [![Coverage Status](https://coveralls.io/repos/github/Djiit/err-pandascore/badge.svg?branch=master)](https://coveralls.io/github/Djiit/err-pandascore?branch=master)

Err-pandascore is a plugin for [Err](https://github.com/gbin/err) that allows you to interact with the [pandascore.co](http://pandascore.co) API. **It requires Python 3.6+**.

**Note: This is a very alpha release. This plugin is subject to major changes.**

## Features

* Basic player search/profile display.
* Support AUTOINSTALL_DEPS thanks to the `requirements.txt` file.

Have an idea ? Open an [issue](https://github.com/Djiit/err-pandascore/issues) or send me a [Pull Request](https://github.com/Djiit/err-pandascore/pulls).

## Usage

### Installation

As admin of an err chatbot, send the following command over XMPP:

```
!repos install https://github.com/Djiit/err-pandascore.git
```

### Commands

Use `!help Pandascore` to see the available commands and their explanation.

## Configuration

Send configuration commands through chat message to this plugins as in :

```
!plugin config Pandascore {'PANDASCORE_API_KEY': 'your_api_key_here'}
```
