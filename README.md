# BSBK Bank — Voice‑Driven Banking Assistant

A Python, microphone‑controlled demo “banking assistant” that lets a user create an account, deposit/withdraw, transfer funds, check balance, and request/clear loans — entirely via speech.

> **Heads‑up:** This is a learning/demo project. It writes plaintext data (including passwords) to local files and is **not** production‑ready or secure. Use on an offline test machine only.

---

## ✨ What it does

- **Conversational flow** using your microphone and speakers (or headphones)
  - Text‑to‑speech: `pyttsx3`
  - Speech‑to‑text: Google Web Speech via `speech_recognition`
- **Account lifecycle**
  - Create a new account (PAN, Aadhaar, age, purpose, initial deposit)
  - Assigns an _account number_ (currently Python’s `id(name)`, i.e., not stable across runs)
  - Password can be spoken or typed
  - Generates a simple **PDF e‑passbook** (`fpdf`)
- **Transactions**
  - **Deposit** (charges a 5% fee)
  - **Withdrawal** (charges a 5% fee)
  - **Transfer** between two accounts
  - **Balance** inquiry
  - **Statement/history** (prints events logged in the `data` file)
- **Loans**
  - Loan intake flow (`g_loan` → `loan_san`)
  - Educational loan example uses **10% annual interest** (simple interest, day‑count 365)
  - Loan clearing (`loan_ret`) computes interest from sanction date and deducts from balance
  - Experimental “third‑party provider” flow stubs (`t_bank_sys`, `p_bank_sys`, etc.)

All actions are navigated by speaking intents like “new account”, “deposit”, “withdrawal”, “transfer”, “loan”, “balance”, “statement”, “change password”, or “exit”.

---

## 📂 Project layout & data files

The single Python script defines a `Bank` class and persists state in several local text files:

| File name | Purpose | Format (per line) |
|---|---|---|
| `General info(account).AI` | Human‑readable account creation log | free text |
| `Registered data.AI` | Registered user snapshot (name, acct #, password) | free text |
| `balance_update.AI` | **Source of truth for balances** | `<name> <balance>` |
| `passwords.AI` | **Passwords in plaintext** | `<name> <password>` |
| `Account_number.Ai` | Mapping of names to account numbers | `<name> <account_id>` |
| `loan data.AI` | Loan principal | `<name> <amount>` |
| `loan_up.AI` | Names with **active** loans | `<name>` |
| `loan_san_date.AI` | Loan sanction dates | `<name> YYYY-MM-DD>` |
| `loan_down.AI` | Names with **cleared** loans | `<name>` |
| `data` | General event log / history | free text |

> The app auto‑creates these files on first run if they don’t exist, but you can also create empty files beforehand to avoid permission issues.

---

## 🛠️ Requirements

- Python 3.8+
- Microphone + speakers
- Internet access (for Google Speech Recognition and `gTTS` if you add it later)

### Python packages

```bash
pip install pyttsx3 SpeechRecognition gTTS pyaudio word2number tqdm fpdf
```

> **PyAudio install tips**
>
> - **Windows:** If `pip install pyaudio` fails, download a matching wheel from e.g. _https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio_ and install with `pip install <wheel.whl>`.
> - **macOS:** `brew install portaudio` then `pip install pyaudio`.
> - **Linux:** `sudo apt-get install portaudio19-dev` then `pip install pyaudio`.

---

## 🚀 Run it

Save your script as `bank.py` (or keep your current filename) ensuring these last lines are present:

```python
if __name__ == "__main__":
    a = Bank()
    a.bot()
```

Then run:

```bash
python bank.py
```

Grant mic permissions when prompted. The assistant will greet you and ask whether you need instructions.

---

## 🗣️ Voice commands (examples)

Say any of the following when asked what you need:

- “**new account**” — start account creation
- “**deposit**” — deposit money (5% fee)
- “**withdrawal**” — withdraw money (5% fee)
- “**transfer**” — transfer between accounts
- “**loan**” — go to loan module (take or clear loan)
- “**balance**” — check balance
- “**statement**” — see recent history entries
- “**change password**” — reset password (no identity proof in demo)
- “**exit** / **quit**” — leave

Many prompts accept follow‑ups like “yes”, “no”, or specific amounts spoken as words (e.g., “five thousand”). Amount phrases are parsed via `word2number`.

---

## 💸 Fees, rules & assumptions (from code)

- **Deposit fee:** 5% (`self.fee = 0.05`)
- **Withdrawal fee:** 5%
- **Minimum first deposit to open account:** 3000
- **Age:** must be ≥ 18
- **Loan interest (educational loan example):** simple interest 10% per annum with 365‑day basis; interest = `principal * 10% * (days/365)`
- **Account numbers:** `id(self.name)` (unstable across runs; demo only)

---

## 🧩 Main class & methods

- `Bank.bot()` — Entry point; plays the intro, reads existing files, and routes user intent
- `gen()` — New account creation; collects PAN/Aadhaar/age/purpose/initial deposit, sets password, generates PDF
- `deposit()` — Authenticates then credits net amount (after fee); logs to files
- `withdrawl()` — Authenticates then debits amount + fee (spelling in code is “withdrawl”)
- `transfer()` — Moves funds name→name if both active and source has funds
- `balance()` — Speaks and prints name, balance, account number
- `history()` — Prompts for name/password and prints matching `data` lines
- `change_password()` — Overwrites password with a new one (no verification beyond name)
- `g_loan()` → `loan_san()` — Loan intake & sanctioning (educational loan example implemented)
- `loan_ret()` — Clears an existing loan by deducting principal + interest
- Experimental partner/provider flows: `t_bank_sys()`, `p_bank_sys()`, `fixed_loan()`, `fixed_transfer()`

---

## ⚠️ Security, privacy & stability notes

This code is intentionally simple for learning purposes and **not** safe for real money or personal data:

- **Passwords stored in plaintext** (`passwords.AI`) and echoed in other logs
- **Account number** is derived from Python object identity (`id(name)`); not persistent across sessions
- **No encryption**, **no input validation**, **no authentication hardening**
- **Loan/fee logic** is simplistic and may have edge cases for negative balances/insufficient funds
- **Blocking I/O** and deep recursion in some branches may lead to difficult‑to‑debug states
- Speech recognition uses Google’s web API; audio is sent to Google for transcription

If you want to make this safer:
- Replace flat files with a database (SQLite/Postgres)
- Hash passwords (`bcrypt`/`argon2`), never log them
- Stable account numbering and constraints
- Add proper identity/KYC checks and audit trails
- Separate UI/voice layer from business logic; add tests
- Internationalize speech recognition (current locale is largely `'en-IN'`)

---

## 🧪 Troubleshooting

- **Mic not detected / permission denied**: Check OS privacy settings and default input device
- **`pyaudio` build errors**: See install tips above; ensure PortAudio is installed
- **Recognition timeout**: You generally get ~10–15 seconds per prompt; speak promptly
- **`speech_recognition.RequestError`**: No internet or Google API unreachable
- **Garbled numbers**: Speak amounts clearly (“two thousand five hundred”) or type when asked
- **Stale balances**: Inspect/repair the `balance_update.AI` file format (`<name> <balance>`) and rerun

---

## 🗺️ Suggested next steps (roadmap)

- Extract a `storage.py` layer (CRUD for users, balances, loans)
- Add CLI / GUI frontend, with voice as an optional layer
- Replace object‑id account numbers with generated UUIDs
- Add unit tests and integration tests
- Implement multi‑currency and rounding rules
- Graceful, non‑recursive control flow and improved error handling
- Package as a module with entry points and config

---

## 📜 License

Personal/educational use only. Do **not** use to handle real personal data or real money.
