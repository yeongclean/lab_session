import numpy as np
import matplotlib.pyplot as plt

# 파일 경로 설정 (C와 O의 s, p 오비탈 PDOS 파일)
c_s_file = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/ptab.pdos.dat.pdos_atm#13(C)_wfc#1(s)"
c_p_file = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/ptab.pdos.dat.pdos_atm#13(C)_wfc#2(p)"
o_s_file = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/ptab.pdos.dat.pdos_atm#14(O)_wfc#1(s)"
o_p_file = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/ptab.pdos.dat.pdos_atm#14(O)_wfc#2(p)"

# 데이터 로드 함수
def load_pdos(file):
    data = np.loadtxt(file)
    energy = data[:, 0]  # 첫 번째 열: 에너지 (eV)
    pdos = data[:, 1]  # 두 번째 열: PDOS 값
    return energy, pdos

# 데이터 로드
energy_c_s, pdos_c_s = load_pdos(c_s_file)
energy_c_p, pdos_c_p = load_pdos(c_p_file)
energy_o_s, pdos_o_s = load_pdos(o_s_file)
energy_o_p, pdos_o_p = load_pdos(o_p_file)

# 그래프 그리기
plt.figure(figsize=(8, 6))

plt.plot(energy_c_s, pdos_c_s, label="C s-orbital", linestyle="--", color="blue")
plt.plot(energy_c_p, pdos_c_p, label="C p-orbital", linestyle="-", color="blue")
plt.plot(energy_o_s, pdos_o_s, label="O s-orbital", linestyle="--", color="red")
plt.plot(energy_o_p, pdos_o_p, label="O p-orbital", linestyle="-", color="red")

# Fermi Energy 기준선 (보통 E_F = 0 eV로 설정)
plt.axvline(x=0.0, color="black", linestyle="--", label="Fermi Level")

# 그래프 설정
plt.xlabel("Energy (eV)")
plt.ylabel("Projected DOS")
plt.title("Projected Density of States (C, O)")
plt.legend()
plt.grid()

# 그래프 표시
plt.show()