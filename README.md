# HestiaMail Discord Bot

A Discord bot to manage email accounts using the HestiaMail API. Add, delete, change passwords, and list email accounts directly from your Discord server.

## Features

- Add email accounts
- Delete email accounts
- Change email passwords
- List all email accounts
- Purge messages in a channel (admin only)

## Requirements

- Python 3.8+
- `discord.py` library
- HestiaMail API

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hestiamail-discord-bot.git
   cd hestiamail-discord-bot
    ```

2. Install dependencies:
   ```bash
   pip install discord.py requests
   ```

3. Configure `hestiamailapi.py`:
   - Replace placeholders:
     - `api-url-here`
     - `username-here`
     - `domain-here`
     - `hash-here` with actual values.

4. Update the bot token in `hestiamailapidiscordbot.py`:
   - Replace `"bot-token"` with your Discord bot token.

## Run the Bot
```bash
python hestiamailapidiscordbot.py
```

## License

This project is licensed under the MIT License.