import numpy as np

# 파일 경로 설정
file_path = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/auab_v_potential.cube"

# CUBE 파일 읽기
with open(file_path, 'r') as file:
    lines = file.readlines()

# 헤더 부분 스킵 (첫 6줄)
header = lines[:6]

# 데이터 부분 추출
data = []
for line in lines[6:]:
    data.extend(map(float, line.split()))

# 데이터 배열로 변환
data = np.array(data)

# z축 좌표와 퍼텐셜 값 추출
z = data[::4]  # z축 좌표 (4번째마다)
potential = data[3::4]  # 퍼텐셜 값 (4번째마다)

# 퍼텐셜 값을 eV 단위로 변환 (1 Ry = 13.6057 eV)
potential_ev = potential * 13.6057

# 진공 퍼텐셜 계산 (최대 퍼텐셜 값)
vacuum_potential = np.max(potential_ev)
print(f"Vacuum Potential: {vacuum_potential:.4f} eV")

# 그래프 그리기
import matplotlib.pyplot as plt

plt.plot(z, potential_ev, label='Potential (eV)')
plt.xlabel('z (Bohr)')
plt.ylabel('Potential (eV)')
plt.axhline(y=vacuum_potential, color='r', linestyle='--', label='Vacuum Level')
plt.legend()
plt.show()