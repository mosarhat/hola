# hola Bot

Discord Bot that uses OpenAI to chat with users in Spanish.

This bot utilizes ```discord.py``` a modern API wrapper for Discord.

## Installation

We want to install ```discord.py```. We will include voice support. 

The following is the command:

```bash
python3 -m pip install -U discord.py[voice]
```

According to ```discord.py``` and its [documentation](https://discordpy.readthedocs.io/en/stable/intro.html), sometimes libraries can pollute a systems installs. 

Simply put, sometimes, one version from a library is different from another persons library in their system. 

To download a virtual environment, we use the following:

```bash
py -m venv bot-env
```

We then have to activate the virtual environment:

```bash
bot-env\Scripts\activate.bat
```

Then we must use ```pip```:

```bash
pip install -U discord.py
```