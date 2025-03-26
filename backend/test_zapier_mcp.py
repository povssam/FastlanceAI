from zapier_mcp import perform_action

def test_actions():
    # Example 1: Create a project
    print("Testing 'create_project' action...")
    project_params = {
        "title": "New Video Project",
        "description": "Looking for a video editor",
        "budget": "500-1000"
    }
    try:
        result = perform_action("create_project", project_params)
        print("Result:", result)
    except Exception as e:
        print(f"Error: {str(e)}")
    print("-" * 50)

    # Example 2: Update project status
    print("Testing 'update_project_status' action...")
    status_params = {
        "project_id": "123",
        "status": "in_progress"
    }
    try:
        result = perform_action("update_project_status", status_params)
        print("Result:", result)
    except Exception as e:
        print(f"Error: {str(e)}")
    print("-" * 50)

if __name__ == "__main__":
    test_actions() 