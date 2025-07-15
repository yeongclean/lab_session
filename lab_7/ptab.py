import numpy as np
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/ptab2_pdos.dat"
# 데이터 로드 (공백과 주석 처리 가능)
data = np.loadtxt(file_path, comments="#")

# 데이터 확인
print(f"Data shape: {data.shape}")
print(f"First 5 rows:\n{data[:5]}")

# Energy (column 1) 및 d 오비탈 PDOS (column 2)
E = data[:, 0]   # 에너지 값 (eV)
d_DOS = data[:, 1]  # d 오비탈 PDOS 값

# Fermi Energy 설정
fermi_energy = 0.2354  # eV

# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(E, d_DOS, label='d orbital PDOS')
plt.axvline(x=fermi_energy, color='r', linestyle='--', label='Fermi Energy')
plt.xlabel('Energy (eV)')
plt.ylabel('PDOS')
plt.title('Pt - CO 2 (PDOS)')
plt.legend()
plt.grid(True)
plt.show()

