# Aiogram 3.x Telegram Bot Project

## Overview

This project is a modular, extensible Telegram bot built using [aiogram 3.x](https://docs.aiogram.dev/en/latest/) what was inspired by django`s work logic, an asynchronous Python framework for Telegram Bot API. The codebase is organized for scalability, maintainability, and ease of adding new features, handlers, and middlewares.

## Features
- **Adding handlers**: it`s just requires for a list with a with dict {"handler":handler,"filters":filters} rout for returning dict like that,what means you can write your own event handling logic, i don't recommend that
- **Command and message handling**: add a handler to the dispatcher or router and add routing logic inside the target/routing.py
- **Callback query handling**: just write new handlers and add them to the target/routing.py/callback_routes
- **Custom middlewares**: just write them and include inside the config/middlewares.py/middlewares_list.
- **Keyboard builder**: Utility for creating and managing inline and reply keyboards.
- **FSM support**: Basic finite state machine (FSM) states for user interaction flows.
- **Default Error handling**: Centralized error logging and handling.
- **Admin notifications**: Notifies admins when the bot starts.
- **Modular routing**: Easily add new routers, handlers, and middlewares.

## Project Structure

```
main.py                  # Entry point, bot startup logic
config/                  # Configuration, setup, and shared utilities
  config.py              # Loads env variables, sets up bot/dispatcher
  keyboard_builder.py    # Keyboard builder utility
  middlewares.py         # Middleware list
  setups.py              # Setup functions for handlers, routers, etc.
dispatcher/              # Main dispatcher and handlers
  routing.py             # Message/callback routing setup
  handlers/              # Message, callback, and error handlers
middlewares/             # Custom middlewares (e.g., throttling)
router/                  # Additional routers and handlers
utils/                   # Utilities (e.g., FSM states)
.env                     # Environment variables (TOKEN, ADMINS)
```

## Requirements

- Python 3.11+
- [aiogram 3.x](https://docs.aiogram.dev/en/latest/)
- [environs](https://pypi.org/project/environs/) (for environment variable management)

Install dependencies:

```bash
pip install aiogram environs
```

## Usage

1. **Configure environment variables**:
   - Copy `.env` and set your `TOKEN` and `ADMINS` (comma-separated Telegram user IDs).
2. **Run the bot**:
   ```bash
   python main.py
   ```

## Extending the Bot

- Add new message or callback handlers in `dispatcher/handlers/` or `router/handlers/`.
- Register new routes in `dispatcher/routing.py` or `router/routing.py`.
- Add middlewares in `middlewares/` and register them in `config/middlewares.py`.
- Use `config/keyboard_builder.py` to create and manage custom keyboards.