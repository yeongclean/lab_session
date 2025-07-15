import numpy as np
import matplotlib.pyplot as plt

# Au 데이터 파일 경로 설정
au_file_path = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/auab_pdos2.dat"
# Pt 데이터 파일 경로 설정
pt_file_path = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/ptab2_pdos.dat"

# Au 데이터 로드 (공백과 주석 처리 가능)
au_data = np.loadtxt(au_file_path, comments="#")
# Pt 데이터 로드 (공백과 주석 처리 가능)
pt_data = np.loadtxt(pt_file_path, comments="#")

# Au 데이터 확인
print(f"Au Data shape: {au_data.shape}")
print(f"First 5 rows of Au data:\n{au_data[:5]}")

# Pt 데이터 확인
print(f"Pt Data shape: {pt_data.shape}")
print(f"First 5 rows of Pt data:\n{pt_data[:5]}")

# Au Energy (column 1) 및 d 오비탈 PDOS (column 2)
E_au = au_data[:, 0]   # 에너지 값 (eV)
d_DOS_au = au_data[:, 1]  # d 오비탈 PDOS 값

# Pt Energy (column 1) 및 d 오비탈 PDOS (column 2)
E_pt = pt_data[:, 0]   # 에너지 값 (eV)
d_DOS_pt = pt_data[:, 1]  # d 오비탈 PDOS 값

# Fermi Energy 설정
fermi_energy_au = 0.1411  # eV
fermi_energy_pt = 0.2354  # eV

# 에너지 - 페르미 준위로 보정
E_corrected_au = E_au - fermi_energy_au
E_corrected_pt = E_pt - fermi_energy_pt

# 그래프 그리기 (x축과 y축을 바꿔서)
plt.figure(figsize=(8, 6))
plt.plot(d_DOS_au, E_corrected_au, color='green', label='Au d orbital PDOS')
plt.plot(d_DOS_pt, E_corrected_pt, color='blue', label='Pt d orbital PDOS')
plt.axhline(y=0, color='r', linestyle='--', label='Fermi Energy')
plt.ylabel('Energy - Fermi Level (eV)')
plt.xlabel('PDOS')
plt.title('Au and Pt - CO (PDOS)')
plt.legend()
plt.grid(True)
plt.show()