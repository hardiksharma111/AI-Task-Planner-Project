# dependency_resolver.py
# Using Depth-First Search (DFS) for Task Scheduling

def find_schedule(tasks, dependencies):
    visited = set()
    stack = []
    
    def dfs(task):
        if task in visited:
            return
        visited.add(task)
        # Check if this task has any prerequisites (dependencies)
        for prereq in dependencies.get(task, []):
            dfs(prereq)
        # Once all prerequisites are visited, add this task to the schedule
        stack.append(task)

    for task in tasks:
        dfs(task)
    
    return stack

# --- Real-World Student Example ---
# Task List
all_tasks = ["Train ML Model", "Clean Data", "Collect Data", "Write Report"]

# Dependencies: { Task: [Prerequisites] }
# Meaning: "Train ML Model" requires "Clean Data" first.
task_dependencies = {
    "Train ML Model": ["Clean Data"],
    "Clean Data": ["Collect Data"],
    "Write Report": ["Train ML Model"]
}

optimized_schedule = find_schedule(all_tasks, task_dependencies)

print("--- Intelligent Study Path ---")
for i, task in enumerate(optimized_schedule, 1):
    print(f"{i}. {task}")