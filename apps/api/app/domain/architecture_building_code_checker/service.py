from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.architecture_building_code_checker.models import AgenticArchitectureBuildingCodeCheckerSession, AgenticArchitectureBuildingCodeCheckerItem
from app.domain.architecture_building_code_checker.schemas import AgenticArchitectureBuildingCodeCheckerSessionCreate, AgenticArchitectureBuildingCodeCheckerItemCreate

class AgenticArchitectureBuildingCodeCheckerService:
    @staticmethod
    def create_session(db: Session, data: AgenticArchitectureBuildingCodeCheckerSessionCreate) -> AgenticArchitectureBuildingCodeCheckerSession:
        db_obj = AgenticArchitectureBuildingCodeCheckerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticArchitectureBuildingCodeCheckerSession:
        return db.query(AgenticArchitectureBuildingCodeCheckerSession).filter(AgenticArchitectureBuildingCodeCheckerSession.id == session_id).first()
