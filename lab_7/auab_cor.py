import numpy as np
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/auab_pdos2.dat"
# 데이터 로드 (공백과 주석 처리 가능)
data = np.loadtxt(file_path, comments="#")

# 데이터 확인
print(f"Data shape: {data.shape}")
print(f"First 5 rows:\n{data[:5]}")

# Energy (column 1) 및 d 오비탈 PDOS (column 2)
E = data[:, 0]   # 에너지 값 (eV)
d_DOS = data[:, 1]  # d 오비탈 PDOS 값

# Fermi Energy 설정
fermi_energy = 0.1411  # eV

# 에너지 - 페르미 준위로 보정
E_corrected = E - fermi_energy

# 그래프 그리기 (x축과 y축을 바꿔서)
plt.figure(figsize=(8, 6))
plt.plot(d_DOS, E_corrected, label='d orbital PDOS')
plt.axhline(y=0, color='r', linestyle='--', label='Fermi Energy')
plt.ylabel('Energy - Fermi Level (eV)')
plt.xlabel('PDOS')
plt.title('Au - CO (PDOS) 2')
plt.legend()
plt.grid(True)
plt.show()