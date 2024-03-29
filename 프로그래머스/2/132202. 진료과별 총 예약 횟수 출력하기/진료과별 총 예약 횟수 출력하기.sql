SELECT MCDP_CD AS '진료과코드', COUNT(APNT_NO) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05-%'
GROUP BY MCDP_CD
ORDER BY COUNT(APNT_YMD), MCDP_CD
# 2022년 5월 / 진료과코드 별 조회 / 예약한 환자 수 기준 오름차순 -> 진료과 코드 기준 오름차순