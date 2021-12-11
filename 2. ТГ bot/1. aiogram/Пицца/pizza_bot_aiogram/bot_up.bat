@echo off

call %~dp0Pizza_bot_aiogram\venv\Scripts\activate

cd %~dp0Pizza_bot_aiogram

set TOKEN=2023366758:AAFObAUVQaFss1A7FpvRRKHWX2zrCfDNyhM

python main.py

pause