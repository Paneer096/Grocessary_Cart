# Grocessary_Cart 

Point of Sale (POS) terminal desktop application built using Python, **PySide6 (Qt for Python)**, and **Qt Designer**. This system simulates a real-world supermarket register by processing barcode inputs, tracking item quantities dynamically, generating real-time receipt views, and maintaining an inventory database.

---

##  Features

* **Modern Dark Mode UI:** Designed with a clean, dark aesthetic (`#1e1e24`) and high-contrast typography for optimal readability.
* **Smart Quantity Grouping:** Automatically detects repeated item scans and bundles them together (e.g., `Apple (x3)`) rather than cluttering the screen with duplicate rows.
* **Monospace Alignment:** Uses native monospace font structures (`Consolas`/`Courier New`) inside the receipt view so that item totals and alignment dots line up perfectly on the right margin.
* **Persistent Totals:** Keeps a precise, real-time running tab of the basket total displayed in a distinct, bold currency layout.
* **Automated UX Micro-tweaks:** Focuses the cursor on the input field on startup and auto-scrolls down to show the freshest scanned items.

---

##  Project Architecture & Data Flow

The application splits its responsibilities cleanly between the layout blueprint, the core runtime logic, and the database layer:

1.  **`pos_design.ui` (The Blueprint):** An XML-based UI configuration file designed in Qt Designer. It maps out precise layouts, widget properties, and baseline styling rules (QSS).
2.  **`inventory.py` (The Database):** A backend Python module that stores product specifications (item names, prices) and maps them to unique barcode lookup strings.
3.  **`main.py` (The Core Logic):** The primary runtime controller that handles application execution, user interaction events, state management, and real-time receipt generation.

---

##  Prerequisites

Ensure you have Python installed, then install the required PySide6 framework bindings:

```bash
pip install PySide6
