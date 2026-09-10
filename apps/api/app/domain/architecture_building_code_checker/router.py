from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.architecture_building_code_checker.schemas import AgenticArchitectureBuildingCodeCheckerSessionCreate, AgenticArchitectureBuildingCodeCheckerSessionResponse
from app.domain.architecture_building_code_checker.service import AgenticArchitectureBuildingCodeCheckerService

router = APIRouter(prefix="/api/v1/architecture_building_code_checker", tags=["Agentic Architecture Building Code Checker Domain"])

@router.post("/sessions", response_model=AgenticArchitectureBuildingCodeCheckerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticArchitectureBuildingCodeCheckerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Architecture Building Code Checker.
    """
    return AgenticArchitectureBuildingCodeCheckerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticArchitectureBuildingCodeCheckerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticArchitectureBuildingCodeCheckerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
