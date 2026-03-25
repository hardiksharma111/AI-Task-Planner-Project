# 🤖 FocusPath: AI-Powered Task Planner 🚀

**FocusPath** is an intelligent scheduling system designed to help students manage complex project deadlines. It combines **Machine Learning** to predict task importance and **Graph Algorithms** to ensure tasks are completed in the correct logical order.

---

## 🌟 Key Features
* **AI Priority Prediction:** Uses a `Decision Tree Classifier` to analyze task difficulty, hours, and deadlines to assign a Priority Level (High/Medium/Low).
* **Automated Dependency Mapping:** Uses a `Depth-First Search (DFS)` algorithm to ensure prerequisite tasks (like "Learning Theory") are scheduled before final tasks (like "Project Submission").
* **User-Friendly Interface:** No coding required to update tasks! Simply edit the `tasks.csv` file in Excel or any text editor.

---

## 📂 Project Structure
```text
AI_Task_Planner-Project/
├── main.py                # The central integrator (Run this!)
├── tasks.csv              # Your editable task list (Input)
├── requirements.txt       # Necessary Python libraries
├── scripts/
│   ├── __init__.py        # Makes scripts a Python package
│   ├── task_classifier.py  # Machine Learning logic (Scikit-Learn)
│   └── dependency_resolver.py # Pathfinding logic (DFS Algorithm)
└── README.md              # Project documentation