from typing import Dict, Any
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/zapier", tags=["zapier"])

@router.post("/webhook")
async def zapier_webhook(data: Dict[str, Any]):
    """
    Handle incoming webhooks from Zapier
    """
    try:
        # Process the webhook data
        # Add your Zapier-specific logic here
        return {"status": "success", "message": "Webhook processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/actions")
async def list_actions():
    """
    List available Zapier actions
    """
    return {
        "actions": [
            {
                "name": "create_project",
                "description": "Create a new project in FastlanceAI",
                "parameters": ["title", "description", "budget"]
            },
            {
                "name": "update_project_status",
                "description": "Update project status",
                "parameters": ["project_id", "status"]
            }
        ]
    } 