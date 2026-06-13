# ⚖️ YAMA-BLOCKER: The Abyss Judgment Sandbox

![License](https://img.shields.io/badge/license-MIT-red.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![PrivEsc](https://img.shields.io/badge/Privilege%20Escalation-Detection-orange)

> **"Yama watches. Yama judges. No process escapes The Abyss."**

---

## 📌 Overview

**YAMA-BLOCKER** is a **context-aware, privilege-separation sandbox engine** written in pure Python. It simulates a kernel-like execution environment where every syscall is monitored, anomalies are detected, and unauthorized privilege escalations are **terminated instantly** — just like the Hindu god of death, Yama, who judges every soul.

Unlike traditional sandboxes that rely on OS-level containers, YAMA-BLOCKER uses Python’s `contextvars` to create **thread-safe, nested execution contexts** with per-process privilege tracking.

---

## 🚀 Key Features

| Feature | Description |
|--------|-------------|
| 🧠 **Context-Aware Sandboxing** | Uses `contextvars` to isolate privileges across threads/processes |
| ⚡ **Real-time Syscall Monitoring** | Simulates system calls with heuristic privilege checks |
| 🔥 **PrivEsc Detection** | Automatically blocks `sudo`, `su -`, `chmod +s`, and root escalation attempts |
| 🎨 **Custom Visual Theme** | 5 unique ANSI colors (Cobalt, Hellfire, Acid, Ghost, Abyss) + boot animation |
| 🛡️ **No External Dependencies** | Pure Python 3.7+ standard library only |
| 🔁 **Context Manager API** | Clean `with YamaSandbox():` syntax |

---

## 🧰 Tech Stack

- **Language:** Python 3.7+
- **Libraries:** `os`, `time`, `sys`, `contextvars`, `contextlib`
- **No external packages** — production ready with zero bloat

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/yama-blocker.git
cd yama-blocker

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the engine
python3 yama_blocker.py
