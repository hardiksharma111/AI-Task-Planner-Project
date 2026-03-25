import pandas as pd
from scripts.task_classifier import model
from scripts.dependency_resolver import find_schedule

def run_planner():
    try:
        # Load user tasks
        df = pd.read_csv('tasks.csv')
        df.columns = df.columns.str.lower() # Case-insensitive headers
        
        print("--- 📂 tasks.csv loaded successfully! ---")
        
        # 1. AI Analysis (ML)
        # We use .values to avoid "Feature Name" warnings
        features = df[['hours', 'difficulty', 'days_left', 'has_prereq']].values
        df['priority'] = model.predict(features)
        
        print("\n--- 🤖 AI Priority Predictions ---")
        for idx, row in df.iterrows():
            print(f"Task: {row['task_name']:<20} | Priority: {row['priority']}")

        # 2. Logic Sorting (DFS Algorithm)
        task_names = df['task_name'].tolist()
        dependencies = {
            row['task_name']: [row['depends_on']] 
            for _, row in df.iterrows() if pd.notna(row['depends_on'])
        }

        optimized_order = find_schedule(task_names, dependencies)

        print("\n--- ✅ Final Optimized Study Path ---")
        for i, task in enumerate(optimized_order, 1):
            print(f"{i}. {task}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_planner()