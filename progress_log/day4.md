# Day 4 — Dashboard & Data Visualization

## What I Completed
- Created `dashboard.py` inside the `pages/` folder
- Built a dashboard page for AI Momentum
- Added:
  - total habits count
  - completed habits count
  - mood summary
  - energy score
  - focus score
  - progress visuals and analytics
- Connected data from:
  - `habits.py`
  - `mood.py`
- Improved the UI with a modern dashboard layout

---

## Problems Faced
- Understanding how different pages share data
- Confusion about how the dashboard accesses habits and mood information
- Understanding `len()` and `sum()` functions

---

## How I Solved Them
- Asked AI to explain how `session_state` works across multiple pages
- Learned that `session_state` acts like shared app memory
- Broke the dashboard logic into smaller parts and understood each section slowly

---

## What I Learned
- `session_state` can connect data between different pages
- Dashboards mostly read and visualize stored data
- `len()` counts total items in a list
- `sum()` can count completed checkbox values (`True` = 1)
- Data visualization improves user understanding and engagement
- Real applications use connected systems instead of isolated pages

---

## Main Concept Learned Today
Apps become more useful when they can collect, connect, and visualize user data clearly.

---

## Personal Reflection
Today the project started feeling like a real productivity platform instead of separate pages. I understood how multiple parts of an app communicate with each other using shared memory.