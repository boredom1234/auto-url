@echo off
(
    echo Running command: cloudflared tunnel --url 127.0.0.1:8002
    echo.
    cloudflared tunnel --url 127.0.0.1:8002
) > output.txt 2>&1

timeout /t 5 >nul
