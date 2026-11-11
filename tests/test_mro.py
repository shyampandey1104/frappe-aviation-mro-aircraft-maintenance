import unittest
from mro.engine import AviationMROEngine, AircraftAsset

class TestAviationMRO(unittest.TestCase):
    def test_inspection_status_and_release(self):
        engine = AviationMROEngine()
        aircraft = AircraftAsset(
            tail_number="VT-AGY",
            aircraft_model="Airbus A320neo",
            serial_number_msn="MSN-10492",
            total_flight_hours=520.0,
            total_flight_cycles=280,
            last_a_check_hours=0.0,
            last_c_check_hours=0.0
        )

        order = engine.evaluate_inspection_status(
            aircraft=aircraft,
            work_order_id="MRO-WO-9021",
            hangar="Hangar 3B - BOM",
            ame_license="AME-DGCA-8921"
        )

        self.assertEqual(order.check_type, "A_CHECK")
        self.assertTrue(order.is_overdue)
        self.assertEqual(order.hours_remaining_until_mandatory_grounding, 0.0)

        crs = engine.issue_certificate_of_release(
            crs_id="CRS-2026-004",
            aircraft=aircraft,
            check_type="A_CHECK",
            ame_sign_date_str="2026-06-15"
        )

        self.assertTrue(crs.is_airworthy)
        self.assertEqual(aircraft.last_a_check_hours, 520.0)

if __name__ == "__main__":
    unittest.main()
