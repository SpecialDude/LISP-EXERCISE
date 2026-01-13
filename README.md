# CBT Simulator — A Reverse-Engineering Challenge

This project is a **console-based CBT (Computer-Based Test) simulator** written in Python.

But here’s the twist 👀  
You are given **full access** to:
- the source code
- the test database
- everything the program uses to run

And yet, the program *tries* to protect the test questions.

Your challenge?

> **Can you understand how it works… and still cheat?**

---

## What This Project Is

- A terminal-based CBT practice application  
- A **learning experiment disguised as a normal program**
- A small reverse-engineering and code-reading challenge  
- A hands-on way to explore:
  - how programs load data at runtime
  - basic obfuscation techniques
  - tamper detection ideas
  - the limits of client-side control

This project is intentionally transparent.  
Nothing is truly hidden from you.

---

## What This Project Is NOT

- ❌ Not malware  
- ❌ Not real anti-cheat software  
- ❌ Not secure by design  
- ❌ Not meant to prevent a determined user  

If you control the code and the data, **you can always cheat**.  
That’s not a flaw — that’s the point.

---

## The Challenge Mindset

You are encouraged to:
- read the code
- inspect the database
- modify files
- experiment freely
- break things and fix them

If you manage to:
- extract the questions
- bypass checks
- manipulate scores
- or completely rewrite the logic

…then congratulations — you learned something valuable.

---

## How It Works (High Level)

- Test questions are stored in an encoded form
- Core components are reconstructed at runtime
- The program performs basic integrity checks
- All logic runs locally on your machine

No servers.  
No secrets.  
Just Python.

---

## Usage

1. Download the files in the **release folder**
2. Run the program from a **safe or empty directory**
3. Execute:

```bash
python main.py
