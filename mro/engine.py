"""Aviation MRO (Maintenance, Repair & Overhaul) Aircraft Maintenance & Airworthiness Engine."""

from datetime import datetime, date
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class AircraftAsset:
    tail_number: str
    aircraft_model: str
    serial_number_msn: str
    total_flight_hours: float
    total_flight_cycles: int
    last_a_check_hours: float
    last_c_check_hours: float


@dataclass
class MaintenanceCheckOrder:
    work_order_id: str
    tail_number: str
    check_type: str
    is_overdue: bool
    hours_remaining_until_mandatory_grounding: float
    assigned_hangar: str
    authorized_ame_license_no: str


@dataclass
class CertificateOfReleaseToService:
    crs_id: str
    tail_number: str
    check_type: str
    certified_flight_hours: float
    certified_flight_cycles: int
    ame_sign_off_date: str
    is_airworthy: bool


class AviationMROEngine:
    """Aviation MRO controller compliant with DGCA CAR 145 / FAA Part 145 airworthiness standards."""

    A_CHECK_INTERVAL_HOURS = 500.0
    C_CHECK_INTERVAL_HOURS = 4000.0

    def evaluate_inspection_status(
        self,
        aircraft: AircraftAsset,
        work_order_id: str,
        hangar: str,
        ame_license: str
    ) -> MaintenanceCheckOrder:
        hours_since_a = aircraft.total_flight_hours - aircraft.last_a_check_hours
        hours_since_c = aircraft.total_flight_hours - aircraft.last_c_check_hours

        if hours_since_c >= self.C_CHECK_INTERVAL_HOURS:
            check = "C_CHECK"
            remaining = max(0.0, self.C_CHECK_INTERVAL_HOURS - hours_since_c)
            overdue = hours_since_c >= self.C_CHECK_INTERVAL_HOURS
        else:
            check = "A_CHECK"
            remaining = max(0.0, self.A_CHECK_INTERVAL_HOURS - hours_since_a)
            overdue = hours_since_a >= self.A_CHECK_INTERVAL_HOURS

        return MaintenanceCheckOrder(
            work_order_id=work_order_id,
            tail_number=aircraft.tail_number,
            check_type=check,
            is_overdue=overdue,
            hours_remaining_until_mandatory_grounding=remaining,
            assigned_hangar=hangar,
            authorized_ame_license_no=ame_license
        )

    def issue_certificate_of_release(
        self,
        crs_id: str,
        aircraft: AircraftAsset,
        check_type: str,
        ame_sign_date_str: str
    ) -> CertificateOfReleaseToService:
        if check_type == "A_CHECK":
            aircraft.last_a_check_hours = aircraft.total_flight_hours
        elif check_type == "C_CHECK":
            aircraft.last_c_check_hours = aircraft.total_flight_hours
            aircraft.last_a_check_hours = aircraft.total_flight_hours

        return CertificateOfReleaseToService(
            crs_id=crs_id,
            tail_number=aircraft.tail_number,
            check_type=check_type,
            certified_flight_hours=aircraft.total_flight_hours,
            certified_flight_cycles=aircraft.total_flight_cycles,
            ame_sign_off_date=ame_sign_date_str,
            is_airworthy=True
        )
