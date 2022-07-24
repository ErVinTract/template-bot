Telegram bot example
==============================

This is trivial bot example.
Each part can be replaced keeping the overall structure the same :)

### How to start

1. Copy repository in your directory

2. Update `pip` and `setuptools` packages

```shell
pip install -U setuptools pip 
```

3. Install all the libraries necessary for the bot to work

```shell
pip install -r requirements.txt
```

4. Create and fill `bot.ini` file ([example](bot.ini.example))

5. Start bot to check

```shell
python3 -m bot
```

6. Edit systemd service file and copy it to a proper location

### How to use i18n

1. Go to /tgbot/services/locales/ 

2. Edit text's in *.ftl
   Example:

'''bash
welcome-text = Hello, { $user }
other-text = Description of this product: { $description }
'''
