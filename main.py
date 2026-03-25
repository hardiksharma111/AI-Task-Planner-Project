# main.py
from scripts.task_classifier import model
from scripts.dependency_resolver import find_schedule

def run_planner():
    print("--- 🤖 FocusPath: AI Task Analysis ---")
    
    # Task: [Hours, Difficulty, Days_Left, Has_Prereq]
    new_tasks_data = {
        "Learn ML Theory": [4, 5, 10, 1],
        "Build Neural Network": [12, 9, 3, 0],
        "Write Final Report": [6, 4, 2, 1]
    }

    for name, features in new_tasks_data.items():
        prediction = model.predict([features])
        print(f"Task: {name:<22} | Predicted Priority: {prediction[0]}")

    all_task_names = list(new_tasks_data.keys())
    dependencies = {
        "Build Neural Network": ["Learn ML Theory"],
        "Write Final Report": ["Build Neural Network"]
    }

    optimized_order = find_schedule(all_task_names, dependencies)

    print("\n--- ✅ Final Optimized Study Path ---")
    for i, task in enumerate(optimized_order, 1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    run_planner()