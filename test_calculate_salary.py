import pytest
from function import calculate_salary

@pytest.mark.parametrize("work_days, ot_hours, late_days, expected", [
    #ไม่มาทำงานเลย
    (0, 0, 0, 0),
    #วันทำงานเกิน 30 วัน
    (31, 0, 0, "work_days must be between 0 and 30"),
    #ค่าทศนิยม
    (0.5, 0.5, 0.5, "please input only integer upper 0"),
    #จำนวน ot เกินกว่าจำนวนวันทำงาน*3
    (30,100,0, "ot_hours must be between 0 and 90"),
    #จำนวน late เกินกว่าจำนวนวันทำงาน
    (30,0,31, "late_days must be between 0 and 30"),
    #ค่าตเป็นอักขระ
    ("a", "b", "c", "please input only integer upper 0"),
    #ค่าติดลบ
    (-1, -1, -1, "please input only integer upper 0"),

])
def test_calculate_salary(work_days, ot_hours, late_days, expected):
    assert calculate_salary(work_days, ot_hours, late_days) == expected

