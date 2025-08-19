# Playwright Behave Chess Test Project

## Project Description
This is a test automation project for a simple chess timing web application.  
The project uses **Playwright** for browser automation and **Behave** for behavior-driven development (BDD) tests.  
Users can add player names, start timers for moves, and interact with the game through a browser interface.

---

## Features Tested
- Add names for two players and display timers.
- Prevent adding a player without a name.
- Verify timers are running correctly.
- Pause and resume the game.
- Validate visibility of buttons and game elements.

---

## Prerequisites
- Python 3.11+
- Git
- A GitHub repository for version control

---

## Installation & Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-folder>

---
## Create and activate a virtual environment:
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
---
## Install dependencies:
pip install -r requirements.txt
playwright install
---
## Running Tests
python -m behave


