# MRZBSCS Toolkit

**MRZBSCS** is a terminal-based cybersecurity toolkit developed in Python. It provides an interactive menu for performing network scanning, brute-force attacks, vulnerability assessment, MAC address manipulation, and more — all in one place.

## Requirements

Make sure the following tools are installed on your system:

- `nmap`
- `nikto`
- `searchsploit` (part of exploitdb)
- `wafw00f`
- `ncrack`
- `chkrootkit`
- `metasploit-framework` (for `msfvenom`)
- `sqlmap`
- `crunch`
- `lynis`
- `wpscan`
- `ike-scan`
- `macchanger`
- `figlet`

On Debian/Ubuntu-based systems, you can install most of them using:

```bash
sudo apt update
sudo apt install nmap nikto exploitdb wafw00f ncrack chkrootkit metasploit-framework sqlmap crunch lynis wpscan ike-scan macchanger figlet
```

## Running the Tool

To start the tool, run:

```bash
python3 mrzbscs.py
```

It will launch an interactive menu with numbered options. You can select tools like `nmap`, `nikto`, `sqlmap`, and `msfvenom` with input prompts. The `exit` option is highlighted in red to terminate the session.

## Disclaimer

This tool is intended for **educational and authorized penetration testing only**. Do **not** use it against systems without explicit permission. Unauthorized use may be **illegal**. The developer takes **no responsibility** for any misuse or consequences.
